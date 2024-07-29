#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/07/26

@author: alain

-----------------------------------------------------
geonodes module
- Scripting Geometry Nodes
-----------------------------------------------------

module : colorclass
-------------------
- Implement color data socket

classes
-------
- Color         : DataSocket of type 'RGBA'

functions
---------

updates
-------
- creation : 2024/07/23
"""

import numpy as np

import bpy
from . import utils
from .treeclass import Tree, Node
#from .socketclass import ValueSocket
from .vectorclass import VectorLike

# =============================================================================================================================
# =============================================================================================================================
# Color
# =============================================================================================================================
# =============================================================================================================================

class Color(VectorLike):

    SOCKET_TYPE = 'RGBA'

    def __init__(self, value=(0., 0., 0., 1.), name=None, tip=None):
        bsock = utils.get_bsocket(value)
        if bsock is None:
            if name is None:
                a = utils.value_to_array(value, (3,))
                if utils.has_bsocket(a):
                    bsock = Node('Combine RGB', {0: a[0], 1: a[1], 2:a[2], 3:a[3]})._out
                else:
                    bsock = Node('Color', color=value[:3])._out
            else:
                bsock = Tree.new_input('NodeSocketColor', name, value=value, description=tip)

        super().__init__(bsock)

    # ====================================================================================================
    # Constructors

    @classmethod
    def Combine(cls, a=0, b=0, c=0, alpha=1, mode='RGB'):
        # mode in ('RGB', 'HSV', 'HSL')
        return Node('Combine Color', {0: a, 1: b, 2: c, 3: alpha}, mode='RGB')._out

    @classmethod
    def CombineRGB(cls, red=0, green=0, blue=0, alpha=1):
        return cls.Combine(red, green, blue, alpha, mode='RGB')

    @classmethod
    def CombineHSV(cls, hue=0, saturation=0, value=0, alpha=1):
        return cls.Combine(hue, saturation, value, alpha, mode='HSV')

    @classmethod
    def CombineHSL(cls, hue=0, saturation=0, lightness=0, alpha=1):
        return cls.Combine(hue, saturation, lightness, alpha, mode='HSL')

    @classmethod
    def Blackbody(cls, temperature=None):
        return Node('Blackbody', {'Temperature': temperature})._out

    @classmethod
    def ColorRamp(cls, fac=None, keep=None):
        col = Node('Color Ramp', {'Fac': fac}, _keep=keep)._out
        col.alpha_ = col.node.alpha
        return col

    # ====================================================================================================
    # Properties

    # ----- Separate color

    @property
    def RGB(self):
        return self._cache('Separate Color', {'Color': self}, mode='RGB', cache_name='RGB')

    @property
    def HSV(self):
        return self._cache('Separate Color', {'Color': self}, mode='HSV', cache_name='HSV')

    @property
    def HSL(self):
        return self._cache('Separate Color', {'Color': self}, mode='HSL', cache_name='HSL')

    @property
    def red(self):
        return self.RGB.red

    @property
    def green(self):
        return self.RGB.red

    @property
    def blue(self):
        return self.RGB.red

    @property
    def alpha(self):
        node = self._cached_nodes.get('RGB')
        if node is None:
            node = self._cached_nodes.get('HSV')
        if node is None:
            node = self._cached_nodes.get('HSL')
        if node is None:
            node = self.RGB

        return node.alpha

    @property
    def hue(self):
        node = self._cached_nodes.get('HSV')
        if node is None:
            node = self._cached_nodes.get('HSL')
        if node is None:
            node = self.HSV
        return node.red

    @property
    def saturation(self):
        node = self._cached_nodes.get('HSV')
        if node is Node:
            node = self._cached_nodes.get('HSL')
        if node is None:
            node = self.HSV
        return node.green

    @property
    def value(self):
        return self.HSV.blue

    @property
    def lightness(self):
        return self.HSL.blue

    # ====================================================================================================
    # Methods

    # ----- Mix

    def mix(self, factor=None, other=None, clamp_result=False, clamp_factor=True, blend_type='MIX'):
        # blend_type in ('MIX', 'DARKEN', 'MULTIPLY', 'BURN', 'LIGHTEN', 'SCREEN', 'DODGE',
        # 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'EXCLUSION', 'SUBTRACT',
        # 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE')
        return Node('Mix', {0: factor, 1: self, 2: other},
            clamp_result=False, clamp_factor=True, blend_type=blend_type, data_type='RGBA')._out

    def darken(self, factor=None, other=None, clamp_result=False, clamp_factor=True):
        return self.mix(factor=factor, other=other, clamp_result=clamp_result, clamp_factor=clamp_factor, blend_type='DARKEN')

    def multiply(self, factor=None, other=None, clamp_result=False, clamp_factor=True):
        return self.mix(factor=factor, other=other, clamp_result=clamp_result, clamp_factor=clamp_factor, blend_type='MULTIPLY')

    def burn(self, factor=None, other=None, clamp_result=False, clamp_factor=True):
        return self.mix(factor=factor, other=other, clamp_result=clamp_result, clamp_factor=clamp_factor, blend_type='BURN')

    def lighten(self, factor=None, other=None, clamp_result=False, clamp_factor=True):
        return self.mix(factor=factor, other=other, clamp_result=clamp_result, clamp_factor=clamp_factor, blend_type='LIGHTEN')

    def screen(self, factor=None, other=None, clamp_result=False, clamp_factor=True):
        return self.mix(factor=factor, other=other, clamp_result=clamp_result, clamp_factor=clamp_factor, blend_type='SCREEN')

    def dodge(self, factor=None, other=None, clamp_result=False, clamp_factor=True):
        return self.mix(factor=factor, other=other, clamp_result=clamp_result, clamp_factor=clamp_factor, blend_type='DODGE')

    def add(self, factor=None, other=None, clamp_result=False, clamp_factor=True):
        return self.mix(factor=factor, other=other, clamp_result=clamp_result, clamp_factor=clamp_factor, blend_type='ADD')

    def overlay(self, factor=None, other=None, clamp_result=False, clamp_factor=True):
        return self.mix(factor=factor, other=other, clamp_result=clamp_result, clamp_factor=clamp_factor, blend_type='OVERLAY')

    def soft_light(self, factor=None, other=None, clamp_result=False, clamp_factor=True):
        return self.mix(factor=factor, other=other, clamp_result=clamp_result, clamp_factor=clamp_factor, blend_type='SOFT_LIGHT')

    def linear_light(self, factor=None, other=None, clamp_result=False, clamp_factor=True):
        return self.mix(factor=factor, other=other, clamp_result=clamp_result, clamp_factor=clamp_factor, blend_type='LINEAR_LIGHT')

    def difference(self, factor=None, other=None, clamp_result=False, clamp_factor=True):
        return self.mix(factor=factor, other=other, clamp_result=clamp_result, clamp_factor=clamp_factor, blend_type='DIFFERENCE')

    def exclusion(self, factor=None, other=None, clamp_result=False, clamp_factor=True):
        return self.mix(factor=factor, other=other, clamp_result=clamp_result, clamp_factor=clamp_factor, blend_type='EXCLUSION')

    def subtract(self, factor=None, other=None, clamp_result=False, clamp_factor=True):
        return self.mix(factor=factor, other=other, clamp_result=clamp_result, clamp_factor=clamp_factor, blend_type='SUBTRACT')

    def divide(self, factor=None, other=None, clamp_result=False, clamp_factor=True):
        return self.mix(factor=factor, other=other, clamp_result=clamp_result, clamp_factor=clamp_factor, blend_type='DIVIDE')

    def mix_hue(self, factor=None, other=None, clamp_result=False, clamp_factor=True):
        return self.mix(factor=factor, other=other, clamp_result=clamp_result, clamp_factor=clamp_factor, blend_type='HUE')

    def mix_saturation(self, factor=None, other=None, clamp_result=False, clamp_factor=True):
        return self.mix(factor=factor, other=other, clamp_result=clamp_result, clamp_factor=clamp_factor, blend_type='SATURATION')

    def mix_color(self, factor=None, other=None, clamp_result=False, clamp_factor=True):
        return self.mix(factor=factor, other=other, clamp_result=clamp_result, clamp_factor=clamp_factor, blend_type='COLOR')

    def mix_value(self, factor=None, other=None, clamp_result=False, clamp_factor=True):
        return self.mix(factor=factor, other=other, clamp_result=clamp_result, clamp_factor=clamp_factor, blend_type='VALUE')

    # ----- RGB curves

    def curves(self, fac=None, keep=None):
        return Node('RGB Curves', {'Fac': fac, 'Color': self}, _keep=keep)._out

    # ----- Comparison

    def equal(self, other, epsilon=None):
        # operation in ('EQUAL', 'NOT_EQUAL', 'BRIGHTER', 'DARKER')
        return Node("Compare", {'A': self, 'B': other, 'Epsilon': epsilon}, data_type='RGBA', operation='EQUAL')._out

    def not_equal(self, other, epsilon=None):
        return Node("Compare", {'A': self, 'B': other, 'Epsilon': epsilon}, data_type='RGBA', operation='NOT_EQUAL')._out

    def brighter(self, other):
        return Node("Compare", {'A': self, 'B': other}, data_type='RGBA', operation='BRIGHTER')._out

    def darker(self, other):
        return Node("Compare", {'A': self, 'B': other}, data_type='RGBA', operation='DARKER')._out
