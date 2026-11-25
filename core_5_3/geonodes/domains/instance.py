"""
This file is part of the geonodes distribution (https://github.com/al1brn/geonodes).
Copyright (c) 2025 Alain Bernard.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

$ DOC transparent

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : domains
------------------
- Actual domains

updates
-------
- creation : 2024/07/23
- update :   2024/09/04
- update :   2025/01/12
"""

__author__ = "Alain Bernard"
__email__  = "lesideesfroides@gmail.com"
__copyright__ = "Copyright (c) 2025, Alain Bernard"
__license__ = "GNU GPL V3"
__version__ = "3.0.0"
__blender_version__ = "4.3.0"


from .domain import Domain
from ...root.node import Node
from ...common.scripterror import NodeError


class Instance(Domain):
    """ > Instance domain of <!Instances>

    !!! note
      The geometry has only one domain sharing the same name:

        - <!Instances> : name of geometry class
        - **Instance** : name of domain class
        - <!Instances#insts> : name of the domain property of class <!Instances>
    """

    DOMAIN_NAME = 'INSTANCE'

    @property
    def count(self):
        """ > Socket 'Instance Count' of node <&Node Domain Size>

        Returns
        -------
        Integer
        """
        return self._geo.domain_size().instance_count

    # ====================================================================================================
    # Properties

    # ----- Scale

    @property
    def scale(self):
        """ > Scale property

        - getter : <&Node Instance Scale>
        - setter : <&Node Scale Instances>

        Scale can be set either by a <!Vector> argument or by a dict with keys
        in ('Scale', 'Center', 'Local Space')

        ``` python
        instances = Instances()
        instances.insts.scale = (1, 2, 3)
        instances.insts.scale = {'Scale': (1, 2, 3), 'Center': (10, 11, 12), 'Local Space': True}
        ```

        Returns
        -------
        Vector
        """
        return Node('Instance Scale')._out

    @scale.setter
    def scale(self, value):
        keys = ['Scale', 'Center', 'Local Space']
        sockets = {'Instances': self._geo, 'Selection': self.get_selection()}
        if isinstance(value, dict):
            for k, v in value.items():
                if k not in keys:
                    raise NodeError(f"Node 'Scale Instances' error: invalid key '{k}' to set instance scale.", valid_keys=keys)
                sockets[k] = v
        else:
            sockets['Scale'] = value

        return self._jump(Node('Scale Instances', named_sockets=sockets)._out)

    # ----- Rotation

    @property
    def rotation(self):
        """ > Rotation property

       - getter : <&Node Instance Rotation>
       - setter : <&Node Rotate Instances>

        Rotation can be set either by a <!Rotation> argument or by a dict with keys
        in ('Rotation', 'Pivot Point', 'Local Space')

        ``` python
        instances = Instances()
        instances.insts.rotation = (1, 2, 3)
        instances.insts.rotation = {'Rotation': (1, 2, 3), 'Pivot Point': (10, 11, 12), 'Local Space': True}
        ```

        Returns
        -------
        Rotation
        """
        return Node('Instance Rotation')._out

    @rotation.setter
    def rotation(self, value):
        keys = ['Rotation', 'Pivot Point', 'Local Space']
        sockets = {'Instances': self._geo, 'Selection': self.get_selection()}
        if isinstance(value, dict):
            for k, v in value.items():
                if k not in keys:
                    raise NodeError(f"Node 'Rotate Instances' error: invalid key '{k}' to set instance rotation.", valid_keys=keys)
                sockets[k] = v
        else:
            sockets['Rotation'] = value

        return self._jump(Node('Rotate Instances', named_sockets=sockets)._out)
