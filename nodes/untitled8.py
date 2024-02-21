#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 18:19:41 2024

@author: alain
"""

from pprint import pprint

import inspect

class Foo:
    def __init__(self):
        """ Documentation
        """
        pass
        
    def bar(self, value, test, name="Name", offset=10):
        """ Bar doc
        class_name : Name_of_the_class
        """
        pass
    
    @staticmethod
    def static_bar(value, test, name="Static name"):
        """ Static bar doc
        """
    
    def no_doc(self):
        pass
    
    @property
    def baz(self):
        """ Get a baz
        
        class_name : baz_getter_class
        
        Other comment
        """
        pass
        
    @baz.setter
    def baz(self):
        """ Set a baz
        class_name : baz_setter_class
        """
        pass
    
def add_static_doc(tree_type, the_class, class_name=None):
    
    # ----------------------------------------------------------------------------------------------------
    # Extract key_word : comment template from the documentation
    
    def analyze_doc(s):
        lines = s.split("\n")

        dct = {}
        keep = []
        for line in lines:
            kv = line.split(':')
            is_kw = False
            if len(kv) > 1:
                kw = kv[0].strip()
                if kw in ['class_name']:
                    dct[kw] = kv[1].strip()
                    is_kw = True
                    
            if not is_kw:
                keep.append(line)
                
        dct['descr'] = "\n".join(keep)
        return dct
    
    # ----------------------------------------------------------------------------------------------------
    # Loop on the documented methods and property
    
    if class_name is None:
        class_name = the_class.__name__
    
    for name in dir(the_class):
        
        f = getattr(the_class, name)
        cat = type(f).__name__
        f_doc = f.__doc__
        if f_doc is None:
            continue
        
        print('-'*50)
        
        if cat == 'function':
            defs = f.__defaults__
            is_static = defs is not None and defs[0] == 'Static name'
            print("Function", name, type(f).__name__, is_static)
            
        elif cat == 'property':
            print("Property", name)
            
        dct = analyze_doc(f.__doc__)
        print(f.__doc__)
        print('.'*50)
        print(dct['descr'])
        #print('.'*50)
        #pprint(analyze_doc(f.__doc__))
        #print()
            

print('='*50)            


add_static_doc(None, Foo)


print()
meth = Foo.bar
smeth  = Foo.static_bar
k = '__defaults__'
print(k)
print(f"   - ", getattr(meth, k))
print(f"   S ", getattr(smeth, k))
print()


print(Foo().__class__.__dict__['bar'])
#print(type(type(Foo.bar.__class__.__dict__['bar'])))




