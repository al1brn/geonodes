"""Handwritten shadernodes specialization of Vector."""
from ...root.vector import Vector as RootVector
from ...root.node import Node


class Vector(RootVector):
    __slots__ = ()

    def out(self, name=None, **props):
        """Send to a group output, material displacement, or a named color AOV."""
        if self._tree._is_group:
            return super().out(name=name, **props)
        if name is None:
            self._tree.set_displacement(self)
        else:
            self._tree.aov_output(name=name, color=self)

    def displacement_out(self, target='ALL'):
        """ > Plug the value to 'Displacement' socket of <&ShaderNode Material Output> node

        > ShaderNodes only
        """
        self._tree.set_displacement(self, target=target)

    @classmethod
    def Tangent(cls, axis='Z', direction_type='RADIAL', uv_map=''):
        """ > Node <&ShaderNode Tangent>

        > ShaderNodes only

        Parameters
        ----------
        axis : str
            Node.axis in ('X', 'Y', 'Z')

        direction_type : str
            Node.direction_type in ('RADIAL', 'UV_MAP')

        uv_map : str
            Node.uv_map


        Returns
        -------
        Vector
        """
        node = Node('Tangent', axis=axis, direction_type=direction_type, uv_map=uv_map)
        return node._out

    @classmethod
    def UVMap(cls, uv_map='', from_instancer=False):
        """ > Node <&ShaderNode UV Map>

        > ShaderNodes only

        Parameters
        ----------
        uv_map : str
            Node.uv_map

        from_instancer : bool
            Node.from_instancer


        Returns
        -------
        Vector
        """
        node = Node('UV Map', from_instancer=from_instancer, uv_map=uv_map)
        return node._out

    def bump(self, strength=None, distance=None, height=None, invert=False):
        """ > Node <&ShaderNode Bump>

        > ShaderNodes only

        !!! note
            Self Vector is plugged to 'Normal' socket

        Parameters
        ----------
        strength : Float
            socket 'Strength' (Strength)

        distance : Float
            socket 'Distance' (Distance)

        height : Float
            socket 'Height' (Height)

        invert : bool
            Node.invert


        Returns
        -------
        Vector
        """
        node = Node('Bump', named_sockets={'Strength': strength, 'Distance': distance, 'Height': height, 'Normal': self}, invert=invert)
        return node._out

    def displacement(self, height=None, midlevel=None, scale=None, space='OBJECT'):
        """ > Node <&ShaderNode Displacement>

        > ShaderNodes only

        !!! note
            Self Vector is plugged to 'Normal' socket

        Parameters
        ----------
        height : Float
            socket 'Height' (Height)

        midlevel : Float
            socket 'Midlevel' (Midlevel)

        scale : Float
            socket 'Scale' (Scale)

        space : str
            Node.space in ('OBJECT', 'WORLD')


        Returns
        -------
        Vector
        """
        node = Node('Displacement', named_sockets={'Height': height, 'Midlevel': midlevel, 'Scale': scale, 'Normal': self}, space=space)
        return node._out

    @classmethod
    def NormalMap(cls, strength=None, color=None, space='TANGENT', uv_map=''):
        """ > Constructor node <&ShaderNode Normal Map>

        > ShaderNodes only

        Parameters
        ----------
        strength : Float
            socket 'Strength' (Strength)

        color : Color
            socket 'Color' (Color)

        space : str
            Node.space in ('TANGENT', 'OBJECT', 'WORLD', 'BLENDER_OBJECT', 'BLENDER_WORLD')

        uv_map : str
            Node.uv_map


        Returns
        -------
        Vector
        """
        node = Node('Normal Map', named_sockets={'Strength': strength, 'Color': color}, space=space, uv_map=uv_map)
        return node._out

    def vector_displacement(self, midlevel=None, scale=None, space='TANGENT'):
        """ > Node <&ShaderNode Vector Displacement>

        > ShaderNodes only

        Parameters
        ----------
        midlevel : Float
            socket 'Midlevel' (Midlevel)

        scale : Float
            socket 'Scale' (Scale)

        space : str
            Node.space in ('TANGENT', 'OBJECT', 'WORLD')


        Returns
        -------
        Vector
        """
        node = Node('Vector Displacement', named_sockets={'Vector': self, 'Midlevel': midlevel, 'Scale': scale}, space=space)
        return node._out
