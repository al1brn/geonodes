#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Blender Python Geometry module

Created on Sat Nov 18 08:30:10 2023

@author: alain.bernard
@email: alain@ligloo.net

-----

Primer numbers
"""

import numpy as np
import re, sys


# ----------------------------------------------------------------------------------------------------
# With regular expression !

def is_prime_A(n):
    # see http://www.noulakaz.net/weblog/2007/03/18/a-regular-expression-to-check-for-prime-numbers/
    return re.match(r'^1?$|^(11+?)\1+$', '1' * n) == None


def get_primes_A(up_to=1000):
    return list(filter(is_prime_A, range(3, up_to, 2)))

# ----------------------------------------------------------------------------------------------------
# Brut algorithm

def get_primes(up_to):
    A = [  3,   5,   7,  11,  13,  17,  19,  23,  29,  31,  37,  41,  43,  47,  53,  59,  61,  67,  71,  73,  79,  83,  89,  97, 
         101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227,
         229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 
         373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 
         521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661,
         673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 
         839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009]
    
    if up_to <= 1000:
        return A
    
    up_to = min(up_to, 10000000)
    a = np.resize(A, 1000)
    index = len(A)
    
    B = A
    
    for n in range(a[-1] + 2, up_to, 2):
        ok = True
        for d in B:
            if n % d == 0:
                ok = False
                break
            
        if ok:
            if index == len(a):
                a = np.resize(a, len(a) + 1000)
            a[index] = n
            index += 1
            
            if n == 1018057: # More than 100000, we must use another B
                # a[445] = 3163 -> 3163**2 = 10004569
                B = a[:446]
                
    return a[:index]


if __name__ == '__main__':
    from time import time
    
    n = 100000
    t0 = time()
    a = get_primes(n)
    t = time() - t0
    print(f"Primes up to {n}: {len(a)} in {t:.2f} s = {a[:10]}...{a[-10:]}")
    print(f"{a[0]=}, {a[10]=}, {a[100]=}, {a[1000]=}")



