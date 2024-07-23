import numpy as np

import bpy
from geonodes.structured.scripterror import NodeError
from geonodes.structured import constants
from geonodes.structured import utils
from geonodes.structured.treeclass import Tree, Node

# =============================================================================================================================
# A Socket

class DataSocket:

    SOCKET_TYPE = None

    def __init__(self, value):

        self._tree = Tree.CURRENT

        bsocket = utils.get_bsocket(value)
        if bsocket is None:
            self._bsocket = self._tree.InputBSocket(self.SOCKET_TYPE, value=value)
        else:
            self._bsocket = bsocket
        self._reset()

    def _reset(self):
        pass

    def __str__(self):
        return f"Socket {self.SOCKET_TYPE} - bsocket: {self._bsocket}"

    def _jump(self, bsocket):
        self._bsocket = bsocket
        self._reset()
        return self

    @classmethod
    @property
    def DATA_TYPE_1(cls):
        dt = constants.DATA_TYPES_1.get(cls.SOCKET_TYPE)
        if dt is None:
            raise NodeError(f"Impossible to get a data type 1 for socket type {cls.SOCKET_TYPE} in {constants.DATA_TYPES_1}")
        else:
            return dt

    @classmethod
    @property
    def DATA_TYPE_2(cls):
        dt = constants.DATA_TYPES_2.get(cls.SOCKET_TYPE)
        if dt is None:
            raise NodeError(f"Impossible to get a data type 2 for socket type {cls.SOCKET_TYPE} in {constants.DATA_TYPES_2}")
        else:
            return dt

    # =============================================================================================================================
    # Constructors

    @classmethod
    def NamedAttribute(cls, name):
        node = Node('Named Attribute', {'Name': name}, data_type=cls.DATA_TYPE_1)
        attr = node.attribute
        attr.exists = node.exists
        return attr

    # =============================================================================================================================
    # Methods

    def switch(self, condition=None, other=None):
        return self._tree.Node('Switch', {'Switch': condition, 'True': self, 'False': other}, input_type=self.DATA_TYPE_1)._out
