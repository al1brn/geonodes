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

module : geometries
------------------
- geometries inheriting from Geometry

Blender Geometry nodes exposes only one type of geometry.
***geonodes*** makes use of one class per type of geometry.

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


from inspect import Arguments
import bpy
from bpy.types import Property, PythonConstraint, SmoothModifier

from .scripterror import NodeError
from . import constants
from . import utils
from .treeclass import Tree, Node, Layout
from .socket_class import NodeCache, Socket
from .geometry_class import Geometry
from .domains import Vertex, Edge, Face, Corner, SplinePoint, Spline, CloudPoint, Instance, Layer

from . import generated

# =============================================================================================================================
# Mesh Geometry

class Mesh(Geometry, generated.Mesh):
    """ > Mesh Geometry

    The **Mesh** exposes all methods specific to meshes.
    Since there is no ambiguity, the word **mesh** is omitted in the **snake_case** name of
    the methods:

    ``` python
    mesh = Mesh.Line() # Node 'Mesh Line'
    cloud = mesh.to_points() # Node 'Mesh to Points'
    ```

    Nodes requiring a domain parameter, are implemented in one of the four domains of Mesh: <#points>,
    <#faces>, <#edges> or <#corners>.

    Properties
    ----------
    - points (Vertex) : POINT domain
    - faces (Face) : FACE domain
    - edges (Edge) : EDGE domain
    - corners (Corner) : CORNER domain
    """

    def _reset(self):

        super()._reset()

        self.points  = Vertex(self)
        self.edges   = Edge(self)
        self.faces   = Face(self)
        self.corners = Corner(self)

    # =============================================================================================================================
    # Operations

    def __sub__(self, other):
        if isinstance(other, tuple):
            return Mesh.Difference(*other, mesh_1=self)
        else:
            return Mesh.Difference(other, mesh_1=self)

    def __truediv__(self, other):
        if isinstance(other, tuple):
            return Mesh.Intersect(self, *other)
        else:
            return Mesh.Intersect(self, other)

    def __mul__(self, other):
        if isinstance(other, tuple):
            return Mesh.Union(self, *other)
        else:
            return Mesh.Union(self, other)

# =============================================================================================================================
# Curve Geometry

class Curve(Geometry, generated.Curve):
    """ > Curve Geometry

    The **Curve** class exposes all methods specific to curves.
    Since there is no ambiguity, the word **curve** is omitted in the name of
    the methods:

    ``` python
    curve = Curve.Line() # Node 'Curve Line'
    mesh= curve.fill() # Node 'Fill Curve'
    ```

    Nodes requiring a domain parameter, are implemented in one of the two domains of **Curve** <#points>,
    <#splines>.

    Properties
    ----------
    - points (SplinePoint) : POINT domain
    - splines (Spline) : CURVE (or SPLINE) domain
    """

    def _reset(self):

        super()._reset()

        self.points  = SplinePoint(self)
        self.splines = Spline(self)

# =============================================================================================================================
# Cloud Geometry

class Cloud(Geometry, generated.Cloud):
    """ > Cloud of Points Geometry

    > [!NOTE]
    > In Blender, the name can vary between **Point Cloud** and **Points**.
    > In GeoNodes, the geometry is named **Cloud**.

    The **Cloud** exposes all methods specific to points cloud.
    Since there is no ambiguity, the word **points** is omitted in the name of
    the methods:

    ``` python
    curves = cloud.to_curves() # Node 'Points to Curves'
    ```

    Nodes requiring a domain parameter, are implemented in the domain <#points>.

    Properties
    ----------
    - points (CloudPoint) : POINT domain
    """

    def _reset(self):

        super()._reset()

        self.points  = CloudPoint(self)

# =============================================================================================================================
# Instances Geometry

class Instances(Geometry, generated.Instances):
    """ > Instances Geometry

    > [!NOTE]
    > The name of geometry class is plural : **Instances** when the name of the
    > domain is singular : <!Instance>. The named of the domain property is <#insts>.

    The **Instances** class exposes all methods specific to instances.
    Since there is no ambiguity, the word **instances** is omitted in the name of
    the methods:

    ``` python
    realized = instances.realize() # Node 'Realize Instances'
    ```
    Nodes requiring a domain parameter, are implemented in the domain <#insts>.

    Properties
    ----------
    - insts (Instance) : INSTANCES domain
    """

    def _reset(self):

        super()._reset()
        self.insts  = Instance(self)

# =============================================================================================================================
# Grease Pencil Geometry

class GreasePencil(Geometry, generated.GreasePencil):
    """ > Grease Pencil Geometry

    Properties
    ----------
    - layers (Layer) : LAYER domain

    """
    def _reset(self):

        super()._reset()
        self.layers = Layer(self)

# =============================================================================================================================
# Volume Geometry

class Volume(Geometry, generated.Volume):
    """ > Volume Geometry

    The **Volume** class exposes all methods specific to volume.
    Since there is no ambiguity, the word **volume** is omitted in the name of
    the methods:

    ``` python
    cube = Volume.Cube() # Node 'Volume Cube'
    ```
    """
    def _reset(self):
        super()._reset()
