#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 10:30:38 2024

@author: alain

-----------------------------------------------------
geonodes module
- Generates nodes with python
- Use numpy to manage vertices
-----------------------------------------------------

module : globalfunctions
------------------
- Global functions

Methods which are independant of the tree type

created : 2024/07/21
"""

from geonodes.nodes.nodeclass import Node

# =============================================================================================================================
# Math node operations

def add(value=None, value_1=None, use_clamp=None, node_label=None, node_color=None):
	""" Math operation

	Node 'Math' (ShaderNodeMath)

	Arguments
	---------
	- value : value
	- value_1 : value_1

	Returns
	---------
		value
	"""

	return Node('Math', value=value, value_1=value_1, use_clamp=use_clamp, operation='ADD', node_label=node_label, node_color=node_color).value

def subtract(value=None, value_1=None, use_clamp=None, node_label=None, node_color=None):
	""" Math operation

	Node 'Math' (ShaderNodeMath)

	Arguments
	---------
	- value : value
	- value_1 : value_1

	Returns
	---------
		value
	"""

	return Node('Math', value=value, value_1=value_1, use_clamp=use_clamp, operation='SUBTRACT', node_label=node_label, node_color=node_color).value

def multiply(value=None, value_1=None, use_clamp=None, node_label=None, node_color=None):
	""" Math operation

	Node 'Math' (ShaderNodeMath)

	Arguments
	---------
	- value : value
	- value_1 : value_1

	Returns
	---------
		value
	"""

	return Node('Math', value=value, value_1=value_1, use_clamp=use_clamp, operation='MULTIPLY', node_label=node_label, node_color=node_color).value

def divide(value=None, value_1=None, use_clamp=None, node_label=None, node_color=None):
	""" Math operation

	Node 'Math' (ShaderNodeMath)

	Arguments
	---------
	- value : value
	- value_1 : value_1

	Returns
	---------
		value
	"""

	return Node('Math', value=value, value_1=value_1, use_clamp=use_clamp, operation='DIVIDE', node_label=node_label, node_color=node_color).value

def multiply_add(value=None, multiplier=None, addend=None, use_clamp=None, node_label=None, node_color=None):
	""" Math operation

	Node 'Math' (ShaderNodeMath)

	Arguments
	---------
	- value : value
	- multiplier : multiplier
	- addend : addend

	Returns
	---------
		value
	"""

	return Node('Math', value=value, multiplier=multiplier, addend=addend, use_clamp=use_clamp, operation='MULTIPLY_ADD', node_label=node_label, node_color=node_color).value

def power(base=None, exponent=None, use_clamp=None, node_label=None, node_color=None):
	""" Math operation

	Node 'Math' (ShaderNodeMath)

	Arguments
	---------
	- base : base
	- exponent : exponent

	Returns
	---------
		value
	"""

	return Node('Math', base=base, exponent=exponent, use_clamp=use_clamp, operation='POWER', node_label=node_label, node_color=node_color).value

def log(value=None, use_clamp=None, node_label=None, node_color=None):
	""" Math operation

	Node 'Math' (ShaderNodeMath)

	Arguments
	---------
	- value : value

	Returns
	---------
		value
	"""

	return Node('Math', value=value, use_clamp=use_clamp, operation='LOGARITHM', node_label=node_label, node_color=node_color).value

def sqrt(value=None, use_clamp=None, node_label=None, node_color=None):
	""" Math operation

	Node 'Math' (ShaderNodeMath)

	Arguments
	---------
	- value : value

	Returns
	---------
		value
	"""

	return Node('Math', value=value, use_clamp=use_clamp, operation='SQRT', node_label=node_label, node_color=node_color).value

def inverse_sqrt(value=None, use_clamp=None, node_label=None, node_color=None):
	""" Math operation

	Node 'Math' (ShaderNodeMath)

	Arguments
	---------
	- value : value

	Returns
	---------
		value
	"""

	return Node('Math', value=value, use_clamp=use_clamp, operation='INVERSE_SQRT', node_label=node_label, node_color=node_color).value

def abs(value=None, use_clamp=None, node_label=None, node_color=None):
	""" Math operation

	Node 'Math' (ShaderNodeMath)

	Arguments
	---------
	- value : value

	Returns
	---------
		value
	"""

	return Node('Math', value=value, use_clamp=use_clamp, operation='ABSOLUTE', node_label=node_label, node_color=node_color).value

def exp(value=None, use_clamp=None, node_label=None, node_color=None):
	""" Math operation

	Node 'Math' (ShaderNodeMath)

	Arguments
	---------
	- value : value

	Returns
	---------
		value
	"""

	return Node('Math', value=value, use_clamp=use_clamp, operation='EXPONENT', node_label=node_label, node_color=node_color).value

def min(value=None, value_1=None, use_clamp=None, node_label=None, node_color=None):
	""" Math operation

	Node 'Math' (ShaderNodeMath)

	Arguments
	---------
	- value : value
	- value_1 : value_1

	Returns
	---------
		value
	"""

	return Node('Math', value=value, value_1=value_1, use_clamp=use_clamp, operation='MINIMUM', node_label=node_label, node_color=node_color).value

def max(value=None, value_1=None, use_clamp=None, node_label=None, node_color=None):
	""" Math operation

	Node 'Math' (ShaderNodeMath)

	Arguments
	---------
	- value : value
	- value_1 : value_1

	Returns
	---------
		value
	"""

	return Node('Math', value=value, value_1=value_1, use_clamp=use_clamp, operation='MAXIMUM', node_label=node_label, node_color=node_color).value

def less_than(value=None, value_1=None, threshold=None, use_clamp=None, node_label=None, node_color=None):
	""" Math operation

	Node 'Math' (ShaderNodeMath)

	Arguments
	---------
	- value : value
	- value_1 : value_1
	- threshold : threshold

	Returns
	---------
		value
	"""

	return Node('Math', value=value, value_1=value_1, threshold=threshold, use_clamp=use_clamp, operation='LESS_THAN', node_label=node_label, node_color=node_color).value

def greater_than(value=None, value_1=None, threshold=None, use_clamp=None, node_label=None, node_color=None):
	""" Math operation

	Node 'Math' (ShaderNodeMath)

	Arguments
	---------
	- value : value
	- value_1 : value_1
	- threshold : threshold

	Returns
	---------
		value
	"""

	return Node('Math', value=value, value_1=value_1, threshold=threshold, use_clamp=use_clamp, operation='GREATER_THAN', node_label=node_label, node_color=node_color).value

def sign(value=None, use_clamp=None, node_label=None, node_color=None):
	""" Math operation

	Node 'Math' (ShaderNodeMath)

	Arguments
	---------
	- value : value

	Returns
	---------
		value
	"""

	return Node('Math', value=value, use_clamp=use_clamp, operation='SIGN', node_label=node_label, node_color=node_color).value

def compare(value=None, value_1=None, epsilon=None, use_clamp=None, node_label=None, node_color=None):
	""" Math operation

	Node 'Math' (ShaderNodeMath)

	Arguments
	---------
	- value : value
	- value_1 : value_1
	- epsilon : epsilon

	Returns
	---------
		value
	"""

	return Node('Math', value=value, value_1=value_1, epsilon=epsilon, use_clamp=use_clamp, operation='COMPARE', node_label=node_label, node_color=node_color).value

def smooth_min(value=None, value_1=None, distance=None, use_clamp=None, node_label=None, node_color=None):
	""" Math operation

	Node 'Math' (ShaderNodeMath)

	Arguments
	---------
	- value : value
	- value_1 : value_1
	- distance : distance

	Returns
	---------
		value
	"""

	return Node('Math', value=value, value_1=value_1, distance=distance, use_clamp=use_clamp, operation='SMOOTH_MIN', node_label=node_label, node_color=node_color).value

def smooth_max(value=None, value_1=None, distance=None, use_clamp=None, node_label=None, node_color=None):
	""" Math operation

	Node 'Math' (ShaderNodeMath)

	Arguments
	---------
	- value : value
	- value_1 : value_1
	- distance : distance

	Returns
	---------
		value
	"""

	return Node('Math', value=value, value_1=value_1, distance=distance, use_clamp=use_clamp, operation='SMOOTH_MAX', node_label=node_label, node_color=node_color).value

def round(value=None, use_clamp=None, node_label=None, node_color=None):
	""" Math operation

	Node 'Math' (ShaderNodeMath)

	Arguments
	---------
	- value : value

	Returns
	---------
		value
	"""

	return Node('Math', value=value, use_clamp=use_clamp, operation='ROUND', node_label=node_label, node_color=node_color).value

def floor(value=None, use_clamp=None, node_label=None, node_color=None):
	""" Math operation

	Node 'Math' (ShaderNodeMath)

	Arguments
	---------
	- value : value

	Returns
	---------
		value
	"""

	return Node('Math', value=value, use_clamp=use_clamp, operation='FLOOR', node_label=node_label, node_color=node_color).value

def ceil(value=None, use_clamp=None, node_label=None, node_color=None):
	""" Math operation

	Node 'Math' (ShaderNodeMath)

	Arguments
	---------
	- value : value

	Returns
	---------
		value
	"""

	return Node('Math', value=value, use_clamp=use_clamp, operation='CEIL', node_label=node_label, node_color=node_color).value

def trunc(value=None, use_clamp=None, node_label=None, node_color=None):
	""" Math operation

	Node 'Math' (ShaderNodeMath)

	Arguments
	---------
	- value : value

	Returns
	---------
		value
	"""

	return Node('Math', value=value, use_clamp=use_clamp, operation='TRUNC', node_label=node_label, node_color=node_color).value

def fract(value=None, use_clamp=None, node_label=None, node_color=None):
	""" Math operation

	Node 'Math' (ShaderNodeMath)

	Arguments
	---------
	- value : value

	Returns
	---------
		value
	"""

	return Node('Math', value=value, use_clamp=use_clamp, operation='FRACT', node_label=node_label, node_color=node_color).value

def modulo(value=None, value_1=None, use_clamp=None, node_label=None, node_color=None):
	""" Math operation

	Node 'Math' (ShaderNodeMath)

	Arguments
	---------
	- value : value
	- value_1 : value_1

	Returns
	---------
		value
	"""

	return Node('Math', value=value, value_1=value_1, use_clamp=use_clamp, operation='MODULO', node_label=node_label, node_color=node_color).value

def floored_modulo(value=None, value_1=None, use_clamp=None, node_label=None, node_color=None):
	""" Math operation

	Node 'Math' (ShaderNodeMath)

	Arguments
	---------
	- value : value
	- value_1 : value_1

	Returns
	---------
		value
	"""

	return Node('Math', value=value, value_1=value_1, use_clamp=use_clamp, operation='FLOORED_MODULO', node_label=node_label, node_color=node_color).value

def wrap(value=None, max=None, min=None, use_clamp=None, node_label=None, node_color=None):
	""" Math operation

	Node 'Math' (ShaderNodeMath)

	Arguments
	---------
	- value : value
	- max : max
	- min : min

	Returns
	---------
		value
	"""

	return Node('Math', value=value, max=max, min=min, use_clamp=use_clamp, operation='WRAP', node_label=node_label, node_color=node_color).value

def snap(value=None, increment=None, use_clamp=None, node_label=None, node_color=None):
	""" Math operation

	Node 'Math' (ShaderNodeMath)

	Arguments
	---------
	- value : value
	- increment : increment

	Returns
	---------
		value
	"""

	return Node('Math', value=value, increment=increment, use_clamp=use_clamp, operation='SNAP', node_label=node_label, node_color=node_color).value

def pingpong(value=None, scale=None, use_clamp=None, node_label=None, node_color=None):
	""" Math operation

	Node 'Math' (ShaderNodeMath)

	Arguments
	---------
	- value : value
	- scale : scale

	Returns
	---------
		value
	"""

	return Node('Math', value=value, scale=scale, use_clamp=use_clamp, operation='PINGPONG', node_label=node_label, node_color=node_color).value

def sin(value=None, use_clamp=None, node_label=None, node_color=None):
	""" Math operation

	Node 'Math' (ShaderNodeMath)

	Arguments
	---------
	- value : value

	Returns
	---------
		value
	"""

	return Node('Math', value=value, use_clamp=use_clamp, operation='SINE', node_label=node_label, node_color=node_color).value

def cos(value=None, use_clamp=None, node_label=None, node_color=None):
	""" Math operation

	Node 'Math' (ShaderNodeMath)

	Arguments
	---------
	- value : value

	Returns
	---------
		value
	"""

	return Node('Math', value=value, use_clamp=use_clamp, operation='COSINE', node_label=node_label, node_color=node_color).value

def tan(value=None, use_clamp=None, node_label=None, node_color=None):
	""" Math operation

	Node 'Math' (ShaderNodeMath)

	Arguments
	---------
	- value : value

	Returns
	---------
		value
	"""

	return Node('Math', value=value, use_clamp=use_clamp, operation='TANGENT', node_label=node_label, node_color=node_color).value

def asin(value=None, use_clamp=None, node_label=None, node_color=None):
	""" Math operation

	Node 'Math' (ShaderNodeMath)

	Arguments
	---------
	- value : value

	Returns
	---------
		value
	"""

	return Node('Math', value=value, use_clamp=use_clamp, operation='ARCSINE', node_label=node_label, node_color=node_color).value

def acos(value=None, use_clamp=None, node_label=None, node_color=None):
	""" Math operation

	Node 'Math' (ShaderNodeMath)

	Arguments
	---------
	- value : value

	Returns
	---------
		value
	"""

	return Node('Math', value=value, use_clamp=use_clamp, operation='ARCCOSINE', node_label=node_label, node_color=node_color).value

def atan(value=None, use_clamp=None, node_label=None, node_color=None):
	""" Math operation

	Node 'Math' (ShaderNodeMath)

	Arguments
	---------
	- value : value

	Returns
	---------
		value
	"""

	return Node('Math', value=value, use_clamp=use_clamp, operation='ARCTANGENT', node_label=node_label, node_color=node_color).value

def atan2(value=None, value_1=None, use_clamp=None, node_label=None, node_color=None):
	""" Math operation

	Node 'Math' (ShaderNodeMath)

	Arguments
	---------
	- value : value
	- value_1 : value_1

	Returns
	---------
		value
	"""

	return Node('Math', value=value, value_1=value_1, use_clamp=use_clamp, operation='ARCTAN2', node_label=node_label, node_color=node_color).value

def sinh(value=None, use_clamp=None, node_label=None, node_color=None):
	""" Math operation

	Node 'Math' (ShaderNodeMath)

	Arguments
	---------
	- value : value

	Returns
	---------
		value
	"""

	return Node('Math', value=value, use_clamp=use_clamp, operation='SINH', node_label=node_label, node_color=node_color).value

def cosh(value=None, use_clamp=None, node_label=None, node_color=None):
	""" Math operation

	Node 'Math' (ShaderNodeMath)

	Arguments
	---------
	- value : value

	Returns
	---------
		value
	"""

	return Node('Math', value=value, use_clamp=use_clamp, operation='COSH', node_label=node_label, node_color=node_color).value

def tanh(value=None, use_clamp=None, node_label=None, node_color=None):
	""" Math operation

	Node 'Math' (ShaderNodeMath)

	Arguments
	---------
	- value : value

	Returns
	---------
		value
	"""

	return Node('Math', value=value, use_clamp=use_clamp, operation='TANH', node_label=node_label, node_color=node_color).value

def radians(value=None, use_clamp=None, node_label=None, node_color=None):
	""" Math operation

	Node 'Math' (ShaderNodeMath)

	Arguments
	---------
	- value : value

	Returns
	---------
		value
	"""

	return Node('Math', value=value, use_clamp=use_clamp, operation='RADIANS', node_label=node_label, node_color=node_color).value

def degrees(value=None, use_clamp=None, node_label=None, node_color=None):
	""" Math operation

	Node 'Math' (ShaderNodeMath)

	Arguments
	---------
	- value : value

	Returns
	---------
		value
	"""

	return Node('Math', value=value, use_clamp=use_clamp, operation='DEGREES', node_label=node_label, node_color=node_color).value
