#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 09:42:01 2023

@author: alain
"""

import numpy as np

def get_group(obj, num=0):
    for group in obj.vertex_groups:
        name = group.name
        if name[:11] == "BagaVertGrp":
            if len(name) == 11:
                if num == 0:
                    return group
                else:
                    continue
            else:
                n = int(name[-3:])
                if n == num:
                    return group
    return None

def get_groups(obj):
    groups = []
    for group in obj.vertex_groups:
        name = group.name
        if name[:11] == "BagaVertGrp":
            groups.append(group)

    return groups


def create_group(obj):
    return obj.vertex_groups.new(name="BagaVertGrp")

def set_weights(obj, group, weight):
    group.add([i for i in range(len(obj.data.vertices))], weight, 'REPLACE')

def add_weights(obj, group, weight):
    group.add([i for i in range(len(obj.data.vertices))], weight, 'ADD')

def sub_weights(obj, group, weight):
    group.add([i for i in range(len(obj.data.vertices))], weight, 'SUBTRACT')


        
        
        
        
    