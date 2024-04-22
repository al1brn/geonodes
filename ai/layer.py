#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 12:12:40 2024

@author: alain
"""

import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------------------------------------
# Sigmoid
# s(x) = 1/(1 + e^-ax)
# s'(x) = ae^-ax/(1 + e^ax)^2 = a(s - s^2) = as(1-s)

def sigmoid(v, alpha=5):
    return 1/(1 + np.exp((-alpha)*v))

def sigmoid_der(v, alpha=5):
    s = sigmoid(v, alpha)
    return alpha*s*(1-s)

# ----------------------------------------------------------------------------------------------------
# Error function

def distance(target, v):
    return v - target

# ----------------------------------------------------------------------------------------------------
# Layer
#
# forward    :  yj = s(wij.xi + bj)
# derivative : dyj/dwij = s'(wij.xi + bj).xi
# 

class Layer:
    def __init__(self, in_count=10, out_count=10, seed=None):
        if seed is None:
            self.rng = np.random.default_rng()
        else:
            self.rng = np.random.default_rng(seed)
            
        self.w = self.rng.uniform(-1,  +1., (out_count, in_count))
        self.b = self.rng.uniform(-1., +1., out_count)
        
    def __str__(self):
        return f"<Layer {self.in_count} -> {self.out_count}>"
    
    def __repr__(self):
        s = str(self)
        for i in range(self.out_count):
            s += "\n   " + " ".join([f"{v:5.2f}" for v in self.w[i]]) 
        return s
        
    @property
    def in_count(self):
        return self.w.shape[1]

    @property
    def out_count(self):
        return self.w.shape[0]
    
    def forward(self, x):
        v = np.matmul(self.w, x) + self.b
        return sigmoid(v)
    
    def backward(self, x, y, t, lmb=.01):
        e = sigmoid_der(x)[None]*((y - t)[:, None])
        self.w -= lmb*e
    
    def step(self, x, target, lmb=.01):
        
        # ----------------------------------------------------------------------------------------------------
        # Forward
        
        v = np.matmul(self.w, x) + self.b
        y = sigmoid(v)
        
        # ----------------------------------------------------------------------------------------------------
        # Error
        
        e = y - target
        
        # ----------------------------------------------------------------------------------------------------
        # Backward
        
        self.w -= lmb*((sigmoid_der(v)*e)[:, None]*x[None])
        
        
    def train(self, count, target_f):
        print(repr(self))
        print(f"Train {count} loops")
        
        for i in range(count):
            x = self.rng.uniform(-1, 1, self.in_count)
            t = target_f(x)
            self.step(x, t)
            if i % (count // 10) == 0:
                print(f"{i:3d}: {t - self.forward(x)}")
                
        print(repr(self))
                
        
        
    
    
def target_f(v):
    return np.array((.5*v[0] + .5*v[1]), (.5*v[2] + .5*v[3]))
        
    
layer = Layer(4, 2)
print(repr(layer))

#x = layer.rng.uniform(-1, 1, 4)
#layer.step(x, target_f(x))
layer.train(10, target_f)


        
