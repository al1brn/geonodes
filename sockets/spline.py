import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Spline

class Spline(Geometry):
    """ Class Spline
    

    | Inherits from: Geometry 
    

    Attribute capture
    =================
    - capture_cyclic                : cyclic (Boolean) 
    - capture_endpoint_selection    : selection (Boolean) 
    - capture_handle_positions      : Sockets      [left (Vector), right (Vector)] 
    - capture_handle_type_selection : selection (Boolean) 
    - capture_length                : Sockets      [length (Float), point_count (Integer)] 
    - capture_parameter             : Sockets      [factor (Float), length (Float), index (Integer)] 
    - capture_resolution            : resolution (Integer) 
    - capture_tangent               : tangent (Vector) 
    - capture_tilt                  : tilt (Float) 
    

    Attributes
    ==========
    - cyclic                : Boolean = capture_cyclic(domain='CURVE') 
    - endpoint_selection    : Boolean = capture_endpoint_selection(domain='CURVE') 
    - factor                : Float = capture_parameter(domain='CURVE').factor 
    - handle_type_selection : Boolean = capture_handle_type_selection(domain='CURVE') 
    - left_handle_position  : Vector = capture_handle_positions(domain='CURVE').left 
    - length                : Float = capture_length(domain='CURVE').length 
    - parameter_index       : Integer = capture_parameter(domain='CURVE').index 
    - parameter_length      : Float = capture_parameter(domain='CURVE').length 
    - point_count           : Integer = capture_length(domain='CURVE').point_count 
    - resolution            : Integer = capture_resolution(domain='CURVE') 
    - right_handle_position : Vector = capture_handle_positions(domain='CURVE').right 
    - spline_ID             : Integer = capture_ID(domain='SPLINE') 
    - spline_index          : Integer = capture_index(domain='SPLINE') 
    - spline_position       : Integer = capture_position(domain='SPLINE') 
    - tangent               : Vector = capture_tangent(domain='CURVE') 
    - tilt                  : Float = capture_tilt(domain='CURVE') 
    

    Stacked methods
    ===============
    - set_cyclic     : Spline 
    - set_resolution : Spline 
    """


    # ----------------------------------------------------------------------------------------------------
    # Attribute capture

    def capture_handle_positions(self, relative=None, domain='CURVE'):
        """Call node CurveHandlePositions (GeometryNodeInputCurveHandlePositions)

        Sockets arguments
        -----------------
            relative       : Boolean

        Returns
        -------
            Sockets [left (Vector), right (Vector)]
        """

        attr_name = 'capture_handle_positions_' + domain
        if not hasattr(self, attr_name):
            node = nodes.CurveHandlePositions(relative=relative)
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name)

    def capture_tangent(self, domain='CURVE'):
        """Call node CurveTangent (GeometryNodeInputTangent)

        Returns
        -------
            Vector
        """

        attr_name = 'capture_tangent_' + domain
        if not hasattr(self, attr_name):
            node = nodes.CurveTangent()
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name).tangent

    def capture_tilt(self, domain='CURVE'):
        """Call node CurveTilt (GeometryNodeInputCurveTilt)

        Returns
        -------
            Float
        """

        attr_name = 'capture_tilt_' + domain
        if not hasattr(self, attr_name):
            node = nodes.CurveTilt()
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name).tilt

    def capture_endpoint_selection(self, start_size=None, end_size=None, domain='CURVE'):
        """Call node EndpointSelection (GeometryNodeCurveEndpointSelection)

        Sockets arguments
        -----------------
            start_size     : Integer
            end_size       : Integer

        Returns
        -------
            Boolean
        """

        attr_name = 'capture_endpoint_selection_' + domain
        if not hasattr(self, attr_name):
            node = nodes.EndpointSelection(start_size=start_size, end_size=end_size)
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name).selection

    def capture_handle_type_selection(self, handle_type='AUTO', mode={'LEFT', 'RIGHT'}, domain='CURVE'):
        """Call node HandleTypeSelection (GeometryNodeCurveHandleTypeSelection)

        Parameters arguments
        --------------------
            handle_type    : 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
            mode           : {'LEFT', 'RIGHT'}

        Returns
        -------
            Boolean
        """

        attr_name = 'capture_handle_type_selection_' + domain
        if not hasattr(self, attr_name):
            node = nodes.HandleTypeSelection(handle_type=handle_type, mode=mode)
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name).selection

    def capture_cyclic(self, domain='CURVE'):
        """Call node IsSplineCyclic (GeometryNodeInputSplineCyclic)

        Returns
        -------
            Boolean
        """

        attr_name = 'capture_cyclic_' + domain
        if not hasattr(self, attr_name):
            node = nodes.IsSplineCyclic()
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name).cyclic

    def capture_length(self, domain='CURVE'):
        """Call node SplineLength (GeometryNodeSplineLength)

        Returns
        -------
            Sockets [length (Float), point_count (Integer)]
        """

        attr_name = 'capture_length_' + domain
        if not hasattr(self, attr_name):
            node = nodes.SplineLength()
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name)

    def capture_parameter(self, domain='CURVE'):
        """Call node SplineParameter (GeometryNodeSplineParameter)

        Returns
        -------
            Sockets [factor (Float), length (Float), index (Integer)]
        """

        attr_name = 'capture_parameter_' + domain
        if not hasattr(self, attr_name):
            node = nodes.SplineParameter()
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name)

    def capture_resolution(self, domain='CURVE'):
        """Call node SplineResolution (GeometryNodeInputSplineResolution)

        Returns
        -------
            Integer
        """

        attr_name = 'capture_resolution_' + domain
        if not hasattr(self, attr_name):
            node = nodes.SplineResolution()
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name).resolution


    # ----------------------------------------------------------------------------------------------------
    # Attributes

    @property
    def spline_ID(self):
        """Call node ID (GeometryNodeInputID)

        Returns
        -------
            Integer
        """

        return self.capture_ID(domain='SPLINE')

    @property
    def spline_index(self):
        """Call node Index (GeometryNodeInputIndex)

        Returns
        -------
            Integer
        """

        return self.capture_index(domain='SPLINE')

    @property
    def spline_position(self):
        """Call node Index (GeometryNodeInputIndex)

        Returns
        -------
            Integer
        """

        return self.capture_position(domain='SPLINE')

    @property
    def left_handle_position(self, relative=None):
        """Call node CurveHandlePositions (GeometryNodeInputCurveHandlePositions)

        Sockets arguments
        -----------------
            relative       : Boolean

        Returns
        -------
            Vector
        """

        return self.capture_handle_positions(domain='CURVE').left

    @property
    def right_handle_position(self, relative=None):
        """Call node CurveHandlePositions (GeometryNodeInputCurveHandlePositions)

        Sockets arguments
        -----------------
            relative       : Boolean

        Returns
        -------
            Vector
        """

        return self.capture_handle_positions(domain='CURVE').right

    @property
    def tangent(self):
        """Call node CurveTangent (GeometryNodeInputTangent)

        Returns
        -------
            Vector
        """

        return self.capture_tangent(domain='CURVE')

    @property
    def tilt(self):
        """Call node CurveTilt (GeometryNodeInputCurveTilt)

        Returns
        -------
            Float
        """

        return self.capture_tilt(domain='CURVE')

    @property
    def endpoint_selection(self, start_size=None, end_size=None):
        """Call node EndpointSelection (GeometryNodeCurveEndpointSelection)

        Sockets arguments
        -----------------
            start_size     : Integer
            end_size       : Integer

        Returns
        -------
            Boolean
        """

        return self.capture_endpoint_selection(domain='CURVE')

    @property
    def handle_type_selection(self, handle_type='AUTO', mode={'LEFT', 'RIGHT'}):
        """Call node HandleTypeSelection (GeometryNodeCurveHandleTypeSelection)

        Parameters arguments
        --------------------
            handle_type    : 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
            mode           : {'LEFT', 'RIGHT'}

        Returns
        -------
            Boolean
        """

        return self.capture_handle_type_selection(domain='CURVE')

    @property
    def cyclic(self):
        """Call node IsSplineCyclic (GeometryNodeInputSplineCyclic)

        Returns
        -------
            Boolean
        """

        return self.capture_cyclic(domain='CURVE')

    @property
    def length(self):
        """Call node SplineLength (GeometryNodeSplineLength)

        Returns
        -------
            Float
        """

        return self.capture_length(domain='CURVE').length

    @property
    def point_count(self):
        """Call node SplineLength (GeometryNodeSplineLength)

        Returns
        -------
            Integer
        """

        return self.capture_length(domain='CURVE').point_count

    @property
    def factor(self):
        """Call node SplineParameter (GeometryNodeSplineParameter)

        Returns
        -------
            Float
        """

        return self.capture_parameter(domain='CURVE').factor

    @property
    def parameter_length(self):
        """Call node SplineParameter (GeometryNodeSplineParameter)

        Returns
        -------
            Float
        """

        return self.capture_parameter(domain='CURVE').length

    @property
    def parameter_index(self):
        """Call node SplineParameter (GeometryNodeSplineParameter)

        Returns
        -------
            Integer
        """

        return self.capture_parameter(domain='CURVE').index

    @property
    def resolution(self):
        """Call node SplineResolution (GeometryNodeInputSplineResolution)

        Returns
        -------
            Integer
        """

        return self.capture_resolution(domain='CURVE')


    # ----------------------------------------------------------------------------------------------------
    # Stacked methods

    def set_cyclic(geometry=None, selection=None, cyclic=None):
        """Call node SetSplineCyclic (GeometryNodeSetSplineCyclic)

        Sockets arguments
        -----------------
            geometry       : Geometry
            selection      : Boolean
            cyclic         : Boolean

        Returns
        -------
            self

        """

        return self.stack(nodes.SetSplineCyclic(geometry=geometry, selection=selection, cyclic=cyclic))

    def set_resolution(geometry=None, selection=None, resolution=None):
        """Call node SetSplineResolution (GeometryNodeSetSplineResolution)

        Sockets arguments
        -----------------
            geometry       : Geometry
            selection      : Boolean
            resolution     : Integer

        Returns
        -------
            self

        """

        return self.stack(nodes.SetSplineResolution(geometry=geometry, selection=selection, resolution=resolution))


