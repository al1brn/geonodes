#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 18:20:59 2023

@author: alain
"""

from time import time

class Timer:
    def __init__(self, message, total, delta=300):
        print()
        print(f"{message}, total: {total:,d}")
        self.total      = total
        self.top        = time()
        self.last       = 0.
        self.last_index = 0
        self.delta      = delta
        
    @property
    def duration(self):
        return time() - self.top
    
    @staticmethod
    def stime(dt):
        dt = int(dt)
        if True:
            m = dt//60
            s = dt % 60
            if m >= 60:
                return f"{m//60:2d}h{m%60:02d}"
            else:
                return f"{m:2d}:{s:02d}"
        else:
            if dt >= 60:
                m = dt//60
                s = dt % 60
                if m >= 60:
                    return f"{m//60:2d}h{m%60:02d}"
                else:
                    return f"{m:2d}:{s:02d}"
            else:
                return f"{dt:3d} s"
        
    def track(self, index):

        dt = self.duration
        if dt - self.last < self.delta and index != 10:
            return
        
        self.progress(index)
        
    def progress(self, index, message=None):
        if index == 0:
            return
        
        p = index/self.total
        dt = self.duration
        
        if True:
            ninds = index - self.last_index
            if ninds == 0:
                rem = (self.total - index)/index*dt
            else:
                rem = (self.total - index)/ninds*(dt - self.last)
        else:
            rem = (self.total - index)/index*dt
            
            
        if message is not None:
            print(message)
            
        print(f"{index:9,d}/{self.total:9,d} ({p*100:3.0f} %) {self.stime(dt)} -> {self.stime(rem)}, total: {self.stime(dt + rem)}")
        
        self.last       = dt
        self.last_index = index
        
    def done(self):
        print(f"Done in {self.stime(self.duration)}")
        print()


if __name__ == '__main__':
    
    for i in [0, 1, 10, 59, 60, 61, 120, 200, 299, 300, 301, 500, 3500, 3599, 3600, 3601, 3659, 3660, 3661, 7000]:
        print(Timer.stime(i))
    
    count = 10000000000
    
    timer = Timer("Test", count, delta=10)
    for i in range(count):
        timer.track(i)
        if i > 500000000:
            break
    timer.done()
    
    