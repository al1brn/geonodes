#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 08:59:49 2024

@author: alain
"""

class Numeric:
    def __add__(self, value):
        return self.math(value, operation='ADD')
    
class Integer(Numeric):
    pass

class Float(Numeric):
    pass

        