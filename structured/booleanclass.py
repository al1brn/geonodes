import numpy as np

import bpy
from geonodes.structured.treeclass import Tree, Node
from geonodes.structured.socketclass import DataSocket

# =============================================================================================================================
# Boolean

class Boolean(DataSocket):
    SOCKET_TYPE = 'BOOLEAN'

    @property
    def math(self):
        from geonodes.structured import math
        return math

    # ----------------------------------------------------------------------------------------------------
    # Operations

    def __neg__(self):
        return self.math.bnot(self)

    def __or__(self, other):
        return self.math.bor(self, other)

    def __ror__(self, other):
        return self.math.bor(other, self)

    def __and__(self, other):
        return self.math.band(self, other)

    def __rand__(self, other):
        return self.math.band(other, self)

    # ----------------------------------------------------------------------------------------------------
    # Random

    @classmethod
    def Random(cls, probability=None, id=None, seed=None):
        return cls(Tree.CURRENT.Node('Random Value', {'Probability': probability, 'ID': id, 'Seed': seed}, data_type='BOOLEAN')._out)
