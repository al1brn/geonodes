"""Handwritten geonodes specialization of Bundle."""
from ...root.bundle import Bundle as RootBundle
from ...common.sockettype import SocketType


class Bundle(RootBundle):
    __slots__ = ()

    def __getitem__(self, key):
        """Read an item by path, optionally with an explicit socket type."""
        if self._is_list:
            return super().__getitem__(key)
        if isinstance(key, tuple):
            if len(key) != 2:
                raise ValueError('Bundle item access expects (path, socket_type).')
            path, socket_type = key
            socket_type = SocketType.convert_type_for_node(
                socket_type, 'NodeGetBundleItem', 'socket_type')
            return self.get_item(path=path, socket_type=socket_type)
        return self.get_item(path=key)

    def __setitem__(self, path, value):
        """Store an item through set_item, which updates this bundle."""
        self.set_item(path=path, item=value)
