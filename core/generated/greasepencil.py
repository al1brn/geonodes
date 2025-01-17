from .. socket_class import Socket
from .. treeclass import Node, ColorRamp, NodeCurves
from .. treeclass import utils
from .. scripterror import NodeError

class GreasePencil(Socket):
    """"
    $DOC SET hidden
    """
    def domain_size(self):
        """ > Node <&Node Domain Size>

        Information
        -----------
        - Socket 'Geometry' : self
        - Parameter 'component' : 'GREASEPENCIL'

        Returns
        -------
        - node [layer_count (Integer)]
        """
        node = self._cache('Domain Size', sockets={'Geometry': self}, component='GREASEPENCIL')
        return node

    def to_curves(self, layers_as_instances=None):
        """ > Node <&Node Grease Pencil to Curves>

        Information
        -----------
        - Socket 'Grease Pencil' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - layers_as_instances (Boolean) : socket 'Layers as Instances' (id: Layers as Instances)

        Returns
        -------
        - Curve
        """
        node = Node('Grease Pencil to Curves', sockets={'Grease Pencil': self, 'Selection': self._sel, 'Layers as Instances': layers_as_instances})
        return node._out

    @classmethod
    def named_layer_selection(cls, name=None):
        """ > Node <&Node Named Layer Selection>

        Arguments
        ---------
        - name (String) : socket 'Name' (id: Name)

        Returns
        -------
        - Boolean
        """
        node = Node('Named Layer Selection', sockets={'Name': name})
        return node._out

    def merge_layers_by_name(self):
        """ > Node <&Node Merge Layers>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Grease Pencil' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'mode' : 'MERGE_BY_NAME'

        Returns
        -------
        - GreasePencil
        """
        node = Node('Merge Layers', sockets={'Grease Pencil': self, 'Selection': self._sel}, mode='MERGE_BY_NAME')
        self._jump(node._out)
        return self._domain_to_geometry

    def merge_layers_by_id(self, group_id=None):
        """ > Node <&Node Merge Layers>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Grease Pencil' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'mode' : 'MERGE_BY_ID'

        Arguments
        ---------
        - group_id (Integer) : socket 'Group ID' (id: Group ID)

        Returns
        -------
        - GreasePencil
        """
        node = Node('Merge Layers', sockets={'Grease Pencil': self, 'Selection': self._sel, 'Group ID': group_id}, mode='MERGE_BY_ID')
        self._jump(node._out)
        return self._domain_to_geometry

    def merge_layers(self, mode='MERGE_BY_NAME'):
        """ > Node <&Node Merge Layers>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Grease Pencil' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - mode (str): parameter 'mode' in ['MERGE_BY_NAME', 'MERGE_BY_ID']

        Returns
        -------
        - GreasePencil
        """
        utils.check_enum_arg('Merge Layers', 'mode', mode, 'merge_layers', ('MERGE_BY_NAME', 'MERGE_BY_ID'))
        node = Node('Merge Layers', sockets={'Grease Pencil': self, 'Selection': self._sel}, mode=mode)
        self._jump(node._out)
        return self._domain_to_geometry

