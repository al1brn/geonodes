from pprint import pprint

from ..core import utils

class Mapping:

    def __init__(self):
        self.nodes = {}

    def add(self, node_name, target='Global', impl='func', fname=None, is_static=False, is_class=False):
        impls = self.nodes.get(node_name)
        if impls is None:
            impls = {}
            self.nodes[node_name] = impls

        tgt = impls.get(target)
        if tgt is None:
            tgt = []
            impls[target] = tgt

        if fname is None:
            fname = utils.snake_case(node_name)

        tgt.append({'impl': impl, 'fname': fname, 'is_static': is_static, 'is_class': is_class})

    def func(self, node_name, fname=None, is_prop=False):
        if is_prop:
            self.add(node_name, target='Global', impl='getter', fname=fname)
        else:
            self.add(node_name, target='Global', impl='func', fname=fname)

    def method(self, node_name, target, fname=None, is_static=False, is_class=False):
        self.add(node_name, target=target, impl='method', fname=fname, is_static=is_static, is_class=is_class)

    def getter(self, node_name, target, fname=None, is_static=False, is_class=False):
        self.add(node_name, target=target, impl='getter', fname=fname, is_static=is_static, is_class=is_class)

    def setter(self, node_name, target, fname=None):
        self.add(node_name, target=target, impl='setter', fname=fname, is_static=False, is_class=False)

    # ====================================================================================================
    # Print the result

    def dump(self):
        pprint(self.nodes)


# =============================================================================================================================
# Mapping


m = Mapping()
