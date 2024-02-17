#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Blender Python Geometry module

Created on Sun Aug 27 07:51:19 2023

@author: alain.bernard
@email: alain@ligloo.net

-----

Encapsulate a numpy array to provide cache mechanism.
It replaces np.append(a, x by a[index] = x which offers far better performances when numerous
appends are required.

"""

import numpy as np

class CachedArray:
    def __init__(self, shape=(), dtype=float, cache=1000):
        """ Initialize a cached array.
        
        Arguments
        ---------
            - shape (int or tuple) : the shape of the array
            - dtype (type=float) : data type
            - cache (int=100000) : size of the cache
        """
        
        self._a    = np.zeros(shape=shape, dtype=dtype)
        self.a_len = len(self._a)
        self.cache = cache
        
    @classmethod
    def FromArray(cls, a, cache=100000):
        """ Initialize from an existing array.

        Arguments
        ---------
            - a (array) : the array
            - cache (int=100000) : size of the cache
            
        Returns
        -------
            - CachedArray
        """
        
        ca = cls(np.shape(a), dtype=a.dtype, cache=cache)
        ca._a[:] = a
        return ca
        
    def __str__(self):
        return f"<Cached array: len: {len(self)}, item_shape: {self.item_shape}, dtype: {self._a.dtype}, actual len: {len(self._a)}, grow increment: {self.cache}>"

    # ====================================================================================================
    # Clone
    
    def clone(self):
        return CachedArray.FromArray(self.a, cache=self.cache)

    # ====================================================================================================
    # Shape
        
    def __len__(self):
        return self.a_len
    
    def __getitem__(self, index):
        return self._a[:self.a_len][index]
    
    def __setitem__(self, index, value):
        self._a[:self.a_len][index] = value
        
    @property
    def shape(self):
        return (self.a_len,) + np.shape(self.a)[1:]
    
    @property
    def size(self):
        return np.prod(self.shape, dtype=int)
    
    @property
    def item_shape(self):
        return np.shape(self._a)[1:]
    
    @property
    def a(self):
        return self._a[:self.a_len]
    
    # ====================================================================================================
    # Append

    def append(self, a):
        """ Append a value or an array of values to the array.
        
        Arguments
        ---------
            - a (array) : the value or array of values to append
        """
        
        if np.shape(a) == self.item_shape:
            a = [a]
            
        new_len = self.a_len + len(a)
        if new_len > len(self._a):
            self._a = np.resize(self._a, (new_len + self.cache,) + self.item_shape)
            
        self._a[self.a_len:new_len] = a
        self.a_len = new_len
        
    # ====================================================================================================
    # Append
        
    def extend(self, count, default=None):
        """ Extend the length.
        
        Arguments
        ---------
            - count (int) : number of items to create
            - default (any) : default value for the created items
            
        Returns
        -------
            - slice : the slice of the created items
        """
        
        new_len = self.a_len + count
        if new_len > len(self._a):
            self._a = np.resize(self._a, (new_len + self.cache,) + self.item_shape)
            
        slc = slice(self.a_len, self.a_len + count)
        self.a_len += count
        
        if default is not None:
            self._a[slc] = default
        
        return slc
    
        
    # ====================================================================================================
    # Squeeze
        
    def squeeze(self):
        """ Resize the internal array to the user size.
        
        This operation frees the cache
        """
        
        self._a = np.resize(self._a, (self.a_len,) + self.item_shape)
        
    # ====================================================================================================
    # Delete items
    
    def clear(self):
        """ Clear the content
        
        Arguments
        ---------
            - index (selection to delete)
        """
        if len(self._a) > 3*self.cache:
            self._a = np.zeros((0,) + self.item_shape, self._a.dtype)
        self.a_len = 0
        
        
        
    def delete(self, index):
        """ Delete items.
        
        Arguments
        ---------
            - index (selection to delete)
        """
        
        indices = np.arange(self.a_len)[index]
        if np.shape(indices) == ():
            n = 1
        else:
            n = len(indices)
            if n == 0:
                return
        
        self._a = np.delete(self._a, indices, axis=0)
        self.a_len -= n
        
    # ====================================================================================================
    # serialization
    
    def serialize(self, ser_array):
        """ Serialize into anpother cached array.
        
        To use only with 2 dimensions arrays !
        
        Caution : serialization makes use of a CachedArray to optimize the perfs when
        serialization uses an array.
        
        Arguments
        ---------
            - ser_array (CachedArray) : the array where to store the cached array
            
        Returns
        -------
            - tuple of ints : offset index, len, item len
        """
        
        if len(self.shape) != 2:
            raise RuntimeError(f"CachedArray.serialize : only for for 2D-arrays, not {self.shape}")
            
        offset = len(ser_array)
        ser_array.append(np.reshape(self.a, self.size))
        
        assert(self.size == len(self)*self.item_shape[0])
        
        return offset, len(self), self.item_shape[0]
    
    def Unserialize(array, offset, length, vdim):
        """Unserialize from a cached array.
        
        Return None if length is null.
        
        Caution : serialization makes use of a CachedArray to optimize the perfs when
        serialization uses an array.
        
        Arguments
        ---------
            - array (array) : the array to read
            - offset (int) : starting index into the array
            - length (int) : first value of the shape
            - vdim (int) : second value of the shape
            
        Returns
        -------
            - CachedArray of the type of array with shape (length, vdim) 
        """
        
        if length == 0:
            return None
        
        shape = (length, vdim)
        size  = length*vdim
        
        ca = CachedArray(shape, dtype=array.dtype)
        
        ca._a[:] = np.reshape(array[offset:offset+size], shape)
        
        return ca
        
            
if __name__ == '__main__':
    
    def test_perf():
    
        from time import time
        
        count = 50000
        
        # ----- Reference test
        
        rng = np.random.default_rng(0)
        a   = np.zeros((0, 3), float)
        
        t0 = time()
        for i in range(count):
            v = rng.uniform(-1, 1, (rng.integers(10, 30), 3))
            a = np.append(a, v, axis=0)
        t1 = time()-t0
        print(f"Ref shape {a.shape}: {t1:.1f} s")
    
        # ----- Cache test
        
        rng = np.random.default_rng(0)
        ca  = CachedArray((0, 3), float, 1000)
        
        t0 = time()
        for i in range(count):
            v = rng.uniform(-1, 1, (rng.integers(10, 30), 3))
            ca.append(v)
        t2 = time()-t0
        print(f"Ref shape {a.shape}: {t2:.1f} s, diff: {np.linalg.norm(a - ca.a):.5f}")
    
        # ----- Extend test
        
        rng = np.random.default_rng(0)
        ca  = CachedArray((0, 3), float, 1000)
        
        t0 = time()
        for i in range(count):
            v = rng.uniform(-1, 1, (rng.integers(10, 30), 3))
            slc = ca.extend(len(v))
            ca[slc] = v
        t3 = time()-t0
        print(f"Ref shape {a.shape}: {t3:.1f} s, diff: {np.linalg.norm(a - ca.a):.5f}")
        
    def test_lib():
        ca0 = CachedArray((10, 3), int)
        ca0._a[:] = np.reshape(np.arange(30), (10, 3))

        ca1 = CachedArray((7, 6), int)
        ca1._a[:] = np.reshape(np.arange(42) + 100, (7, 6))
        
        print(ca0.a)
        print(ca1.a)
        
        ser_a = CachedArray(0, int, 100000)
        
        p0 = ca0.serialize(ser_a)
        p1 = ca1.serialize(ser_a)
        
        print("Param 0", p0)
        print("Param 1", p1)
        
        print(ser_a)
        print(ser_a.a)
        
        ser_a.squeeze()
        
        na1 = CachedArray.Unserialize(ser_a._a, *p1)
        na0 = CachedArray.Unserialize(ser_a._a, *p0)
        
        print(na0.a)
        print(na1.a)
        
        print(np.shape(na0._a), np.shape(na1._a))

    #test_perf()
    #test_lib()
        
        

        
        
    
            
            
        
        
        
        