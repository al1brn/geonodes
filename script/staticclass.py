import numpy as np

import bpy
from gnodes import utils
from gnodes.treeclass import Tree, Node

class Static(cls):

    @classmethod
    @property
    def position(cls):
        return Node('Position')._out
