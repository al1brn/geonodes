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
        """ capture_handle_positions
        

        | Node: CurveHandlePositions 
        

            v = spline.capture_handle_positions(self, relative, domain='CURVE') 
        

        Arguments
        =========
        

            Parameters arguments
            --------------------
            - self   
            - domain:'CURVE' 
        

            Sockets arguments
            -----------------
            - relative : Boolean 
        

        Node creation
        =============
        

            node = nodes.CurveHandlePositions(relative=relative) 
        

        Returns
        =======
                Sockets [left (Vector), right (Vector)] 
        """

        attr_name = 'capture_handle_positions_' + domain
        if not hasattr(self, attr_name):
            node = nodes.CurveHandlePositions(relative=relative)
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name)

    def capture_tangent(self, domain='CURVE'):
        """ capture_tangent
        

        | Node: CurveTangent 
        

            v = spline.capture_tangent(self, domain='CURVE') 
        

        Arguments
        =========
        

            Parameters arguments
            --------------------
            - self   
            - domain:'CURVE' 
        

        Node creation
        =============
        

            node = nodes.CurveTangent() 
        

        Returns
        =======
                Vector 
        """

        attr_name = 'capture_tangent_' + domain
        if not hasattr(self, attr_name):
            node = nodes.CurveTangent()
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name).tangent

    def capture_tilt(self, domain='CURVE'):
        """ capture_tilt
        

        | Node: CurveTilt 
        

            v = spline.capture_tilt(self, domain='CURVE') 
        

        Arguments
        =========
        

            Parameters arguments
            --------------------
            - self   
            - domain:'CURVE' 
        

        Node creation
        =============
        

            node = nodes.CurveTilt() 
        

        Returns
        =======
                Float 
        """

        attr_name = 'capture_tilt_' + domain
        if not hasattr(self, attr_name):
            node = nodes.CurveTilt()
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name).tilt

    def capture_endpoint_selection(self, start_size=None, end_size=None, domain='CURVE'):
        """ capture_endpoint_selection
        

        | Node: EndpointSelection 
        

            v = spline.capture_endpoint_selection(self, start_size, end_size, domain='CURVE') 
        

        Arguments
        =========
        

            Parameters arguments
            --------------------
            - self   
            - domain:'CURVE' 
        

            Sockets arguments
            -----------------
            - start_size : Integer 
            - end_size   : Integer 
        

        Node creation
        =============
        

            node = nodes.EndpointSelection(start_size=start_size, end_size=end_size) 
        

        Returns
        =======
                Boolean 
        """

        attr_name = 'capture_endpoint_selection_' + domain
        if not hasattr(self, attr_name):
            node = nodes.EndpointSelection(start_size=start_size, end_size=end_size)
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name).selection

    def capture_handle_type_selection(self, handle_type='AUTO', mode={'RIGHT', 'LEFT'}, domain='CURVE'):
        """ capture_handle_type_selection
        

        | Node: HandleTypeSelection 
        

            v = spline.capture_handle_type_selection(self, handle_type, mode, domain='CURVE') 
        

        Arguments
        =========
        

            Parameters arguments
            --------------------
            - self         
            - handle_type : 'AUTO' in [FREE, AUTO, VECTOR, ALIGN] 
            - mode        : {'RIGHT', 'LEFT'} 
            - domain      :'CURVE' 
        

        Node creation
        =============
        

            node = nodes.HandleTypeSelection(handle_type=handle_type, mode=mode) 
        

        Returns
        =======
                Boolean 
        """

        attr_name = 'capture_handle_type_selection_' + domain
        if not hasattr(self, attr_name):
            node = nodes.HandleTypeSelection(handle_type=handle_type, mode=mode)
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name).selection

    def capture_cyclic(self, domain='CURVE'):
        """ capture_cyclic
        

        | Node: IsSplineCyclic 
        

            v = spline.capture_cyclic(self, domain='CURVE') 
        

        Arguments
        =========
        

            Parameters arguments
            --------------------
            - self   
            - domain:'CURVE' 
        

        Node creation
        =============
        

            node = nodes.IsSplineCyclic() 
        

        Returns
        =======
                Boolean 
        """

        attr_name = 'capture_cyclic_' + domain
        if not hasattr(self, attr_name):
            node = nodes.IsSplineCyclic()
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name).cyclic

    def capture_length(self, domain='CURVE'):
        """ capture_length
        

        | Node: SplineLength 
        

            v = spline.capture_length(self, domain='CURVE') 
        

        Arguments
        =========
        

            Parameters arguments
            --------------------
            - self   
            - domain:'CURVE' 
        

        Node creation
        =============
        

            node = nodes.SplineLength() 
        

        Returns
        =======
                Sockets [length (Float), point_count (Integer)] 
        """

        attr_name = 'capture_length_' + domain
        if not hasattr(self, attr_name):
            node = nodes.SplineLength()
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name)

    def capture_parameter(self, domain='CURVE'):
        """ capture_parameter
        

        | Node: SplineParameter 
        

            v = spline.capture_parameter(self, domain='CURVE') 
        

        Arguments
        =========
        

            Parameters arguments
            --------------------
            - self   
            - domain:'CURVE' 
        

        Node creation
        =============
        

            node = nodes.SplineParameter() 
        

        Returns
        =======
                Sockets [factor (Float), length (Float), index (Integer)] 
        """

        attr_name = 'capture_parameter_' + domain
        if not hasattr(self, attr_name):
            node = nodes.SplineParameter()
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name)

    def capture_resolution(self, domain='CURVE'):
        """ capture_resolution
        

        | Node: SplineResolution 
        

            v = spline.capture_resolution(self, domain='CURVE') 
        

        Arguments
        =========
        

            Parameters arguments
            --------------------
            - self   
            - domain:'CURVE' 
        

        Node creation
        =============
        

            node = nodes.SplineResolution() 
        

        Returns
        =======
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
        """ spline_ID
        

        | Node: ID 
        

            v = spline.spline_ID(self) 
        

        Arguments
        =========
        

            Parameters arguments
            --------------------
            - self 
        

        Node creation
        =============
        

            node = nodes.ID() 
        

        Returns
        =======
                Integer 
        """

        return self.capture_ID(domain='SPLINE')

    @property
    def spline_index(self):
        """ spline_index
        

        | Node: Index 
        

            v = spline.spline_index(self) 
        

        Arguments
        =========
        

            Parameters arguments
            --------------------
            - self 
        

        Node creation
        =============
        

            node = nodes.Index() 
        

        Returns
        =======
                Integer 
        """

        return self.capture_index(domain='SPLINE')

    @property
    def spline_position(self):
        """ spline_position
        

        | Node: Index 
        

            v = spline.spline_position(self) 
        

        Arguments
        =========
        

            Parameters arguments
            --------------------
            - self 
        

        Node creation
        =============
        

            node = nodes.Index() 
        

        Returns
        =======
                Integer 
        """

        return self.capture_position(domain='SPLINE')

    @property
    def left_handle_position(self, relative=None):
        """ left_handle_position
        

        | Node: CurveHandlePositions 
        

            v = spline.left_handle_position(self, relative) 
        

        Arguments
        =========
        

            Parameters arguments
            --------------------
            - self 
        

            Sockets arguments
            -----------------
            - relative : Boolean 
        

        Node creation
        =============
        

            node = nodes.CurveHandlePositions(relative=relative) 
        

        Returns
        =======
                Vector 
        """

        return self.capture_handle_positions(domain='CURVE').left

    @property
    def right_handle_position(self, relative=None):
        """ right_handle_position
        

        | Node: CurveHandlePositions 
        

            v = spline.right_handle_position(self, relative) 
        

        Arguments
        =========
        

            Parameters arguments
            --------------------
            - self 
        

            Sockets arguments
            -----------------
            - relative : Boolean 
        

        Node creation
        =============
        

            node = nodes.CurveHandlePositions(relative=relative) 
        

        Returns
        =======
                Vector 
        """

        return self.capture_handle_positions(domain='CURVE').right

    @property
    def tangent(self):
        """ tangent
        

        | Node: CurveTangent 
        

            v = spline.tangent(self) 
        

        Arguments
        =========
        

            Parameters arguments
            --------------------
            - self 
        

        Node creation
        =============
        

            node = nodes.CurveTangent() 
        

        Returns
        =======
                Vector 
        """

        return self.capture_tangent(domain='CURVE')

    @property
    def tilt(self):
        """ tilt
        

        | Node: CurveTilt 
        

            v = spline.tilt(self) 
        

        Arguments
        =========
        

            Parameters arguments
            --------------------
            - self 
        

        Node creation
        =============
        

            node = nodes.CurveTilt() 
        

        Returns
        =======
                Float 
        """

        return self.capture_tilt(domain='CURVE')

    @property
    def endpoint_selection(self, start_size=None, end_size=None):
        """ endpoint_selection
        

        | Node: EndpointSelection 
        

            v = spline.endpoint_selection(self, start_size, end_size) 
        

        Arguments
        =========
        

            Parameters arguments
            --------------------
            - self 
        

            Sockets arguments
            -----------------
            - start_size : Integer 
            - end_size   : Integer 
        

        Node creation
        =============
        

            node = nodes.EndpointSelection(start_size=start_size, end_size=end_size) 
        

        Returns
        =======
                Boolean 
        """

        return self.capture_endpoint_selection(domain='CURVE')

    @property
    def handle_type_selection(self, handle_type='AUTO', mode={'RIGHT', 'LEFT'}):
        """ handle_type_selection
        

        | Node: HandleTypeSelection 
        

            v = spline.handle_type_selection(self, handle_type, mode) 
        

        Arguments
        =========
        

            Parameters arguments
            --------------------
            - self         
            - handle_type : 'AUTO' in [FREE, AUTO, VECTOR, ALIGN] 
            - mode        : {'RIGHT', 'LEFT'} 
        

        Node creation
        =============
        

            node = nodes.HandleTypeSelection(handle_type=handle_type, mode=mode) 
        

        Returns
        =======
                Boolean 
        """

        return self.capture_handle_type_selection(domain='CURVE')

    @property
    def cyclic(self):
        """ cyclic
        

        | Node: IsSplineCyclic 
        

            v = spline.cyclic(self) 
        

        Arguments
        =========
        

            Parameters arguments
            --------------------
            - self 
        

        Node creation
        =============
        

            node = nodes.IsSplineCyclic() 
        

        Returns
        =======
                Boolean 
        """

        return self.capture_cyclic(domain='CURVE')

    @property
    def length(self):
        """ length
        

        | Node: SplineLength 
        

            v = spline.length(self) 
        

        Arguments
        =========
        

            Parameters arguments
            --------------------
            - self 
        

        Node creation
        =============
        

            node = nodes.SplineLength() 
        

        Returns
        =======
                Float 
        """

        return self.capture_length(domain='CURVE').length

    @property
    def point_count(self):
        """ point_count
        

        | Node: SplineLength 
        

            v = spline.point_count(self) 
        

        Arguments
        =========
        

            Parameters arguments
            --------------------
            - self 
        

        Node creation
        =============
        

            node = nodes.SplineLength() 
        

        Returns
        =======
                Integer 
        """

        return self.capture_length(domain='CURVE').point_count

    @property
    def factor(self):
        """ factor
        

        | Node: SplineParameter 
        

            v = spline.factor(self) 
        

        Arguments
        =========
        

            Parameters arguments
            --------------------
            - self 
        

        Node creation
        =============
        

            node = nodes.SplineParameter() 
        

        Returns
        =======
                Float 
        """

        return self.capture_parameter(domain='CURVE').factor

    @property
    def parameter_length(self):
        """ parameter_length
        

        | Node: SplineParameter 
        

            v = spline.parameter_length(self) 
        

        Arguments
        =========
        

            Parameters arguments
            --------------------
            - self 
        

        Node creation
        =============
        

            node = nodes.SplineParameter() 
        

        Returns
        =======
                Float 
        """

        return self.capture_parameter(domain='CURVE').length

    @property
    def parameter_index(self):
        """ parameter_index
        

        | Node: SplineParameter 
        

            v = spline.parameter_index(self) 
        

        Arguments
        =========
        

            Parameters arguments
            --------------------
            - self 
        

        Node creation
        =============
        

            node = nodes.SplineParameter() 
        

        Returns
        =======
                Integer 
        """

        return self.capture_parameter(domain='CURVE').index

    @property
    def resolution(self):
        """ resolution
        

        | Node: SplineResolution 
        

            v = spline.resolution(self) 
        

        Arguments
        =========
        

            Parameters arguments
            --------------------
            - self 
        

        Node creation
        =============
        

            node = nodes.SplineResolution() 
        

        Returns
        =======
                Integer 
        """

        return self.capture_resolution(domain='CURVE')


    # ----------------------------------------------------------------------------------------------------
    # Stacked methods

    def set_cyclic(geometry=None, selection=None, cyclic=None):
        """ set_cyclic
        

        | Node: SetSplineCyclic 
        

            spline.set_cyclic(geometry, selection, cyclic) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - geometry  : Geometry 
            - selection : Boolean 
            - cyclic    : Boolean 
        

        Node creation
        =============
        

            node = nodes.SetSplineCyclic(geometry=geometry, selection=selection, cyclic=cyclic) 
        

        Returns
        =======
                self 
        """

        return self.stack(nodes.SetSplineCyclic(geometry=geometry, selection=selection, cyclic=cyclic))

    def set_resolution(geometry=None, selection=None, resolution=None):
        """ set_resolution
        

        | Node: SetSplineResolution 
        

            spline.set_resolution(geometry, selection, resolution) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - geometry   : Geometry 
            - selection  : Boolean 
            - resolution : Integer 
        

        Node creation
        =============
        

            node = nodes.SetSplineResolution(geometry=geometry, selection=selection, resolution=resolution) 
        

        Returns
        =======
                self 
        """

        return self.stack(nodes.SetSplineResolution(geometry=geometry, selection=selection, resolution=resolution))


