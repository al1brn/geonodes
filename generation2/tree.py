import bpy
from . import utils, config

class Tree:
    def __init__(self, tree_type='GeometryNodeTree', tree_name='Temporary Tree'):

        self.btree = None
        self.tree_type = tree_type
        self.tree_name = tree_name
        self.nodes = {}

    def __enter__(self):
        self.btree = bpy.data.node_groups.new(name=self.tree_name, type=self.tree_type)

        self.nodes = {}
        for type_name in dir(bpy.types):
            try:
                node = self.btree.nodes.new(type=type_name)
            except (RuntimeError, TypeError):
                continue
            self.nodes[node.name] = node.bl_idname
            self.btree.nodes.clear()

        self._group_input=None

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.btree is not None:
            bpy.data.node_groups.remove(self.btree)

        self.btree = None

    def create_node(self, name):
        blid = self.nodes.get(name, name)
        return self.btree.nodes.new(type=blid)

    @property
    def group_input(self):
        if self._group_input is None:
            self._group_input = self.create_node('Group Input')
        return self._group_input

    @property
    def valid_input_sockets(self):
        interface = self.btree.interface
        try:
            interface.new_socket(name='Fake', socket_type='FAKE')
        except TypeError as e:
            s = str(e)

        token = f'"FAKE" not found in '
        i = s.find(token)

        return eval(s[i + len(token):])

    def create_input_socket(self, socket_type, name=None):

        if name is None:
            name = socket_type

        interface = self.btree.interface
        return interface.new_socket(name=socket_type, socket_type=socket_type)





