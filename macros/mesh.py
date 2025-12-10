if False:
    from ..core.treeclass import Tree, Layout, Panel
    from ..core.geometries import Geometry, Mesh, Curve, Cloud, GreasePencil, Volume, Instances
    from ..core.sock_boolean import Boolean
    from ..core.sock_bundle import Bundle
    from ..core.sock_closure import Closure
    from ..core.sock_color import Color
    from ..core.sock_float import Float
    from ..core.sock_material import Material
    from ..core.sock_matrix import Matrix
    from ..core.sock_menu import Menu
    from ..core.sock_object import Object
    from ..core.sock_rotation import Rotation
    from ..core.sock_shader import Shader
    from ..core.sock_string import String
    from ..core.sock_vector import Vector

from geonodes import *

__all__ = ["move_selection", "move_coordinate", "build_flat_cap"]


# ===========================================================================
# Move selection
# ===========================================================================

def move_selection(
    mesh:       Mesh, 
    selection:  Boolean, 
    offset:     Float,
    axis :      str = 'Z',
    summit:     Float = None,
    title:      str = "move_selection",
    ):
    """ Move cylinder or conepoints at a given coordinate.
    
    This macro is intended to move a circular ring of a cone or a cylinder.
    
    Arguments
    ---------
    - mesh (Mesh) : the mesh
    - selection (Boolean) : selection to apply
    - offset (Float) : the displacement value
    - axis (str = 'Z' in ('X', 'Y', 'Z') : axis to move along
    - summit (Float = None) : cone summit
    - title (str) : Layout title
    
    Returns
    -------
    - Mesh
    """
    
    if title is not None:
        title += f", axis={axis}"
    
    with Layout(title, color='MACRO'):
    
        if axis.upper() == 'X':
            if summit is None:
                mesh[selection].offset = (offset, 0, 0)
                
            else:
                x, y, z = nd.position.xyz
                slope = offset/(x - summit)
                mesh[selection].offset = (offset, slope*y, slope*z)
        
        elif axis.upper() == 'Y':
            if summit is None:
                mesh[selection].offset = (0, offset, 0)
                
            else:
                x, y, z = nd.position.xyz
                slope = offset/(y - summit)
                mesh[selection].offset = (slope*x, offset, slope*z)
        
        elif axis.upper() == 'Z':
            if summit is None:
                mesh[selection].offset = (0, 0, offset)
                
            else:
                x, y, z = nd.position.xyz
                slope = offset/(z - summit)
                mesh[selection].offset = (slope*x, slope*y, offset)
            
        else:
            raise NodeError(f"Error in macro 'move_selection'. Axis must be in ('X', 'Y', 'Z'), not '{axis}'")
            
    return mesh

# ===========================================================================
# Move coordinate
# ===========================================================================
        
def move_coordinate(
    mesh:       Mesh, 
    coord:      Float, 
    offset:     Float,
    axis :      str = 'Z',
    summit:     Float = None,
    epsilon:    Float = None,
    title:      str = "move_coordinate",
    ):
    """ Move cylinder or conepoints at a given coordinate.
    
    This macro is intended to move a circular ring of a cone or a cylinder.
    
    Arguments
    ---------
    - mesh (Mesh) : the mesh
    - coord (Float) : The coordinate value
    - offset (Float) : the displacement value
    - axis (str = 'Z' in ('X', 'Y', 'Z') : axis to move along
    - summit (Float = None) : cone summit
    - epsilon (Float = None) : epsilon value for compare
    - title (str) : Layout title
    
    Returns
    -------
    - Mesh
    """
    
    if title is not None:
        title += f", axis={axis}"
    
    with Layout(title, color='MACRO'):
        
        x, y, z = nd.position.xyz
            
        if axis.upper() == 'X':
            sel = x.equal(coord, epsilon=epsilon)
        
        elif axis.upper() == 'Y':
            sel = y.equal(coord, epsilon=epsilon)
        
        elif axis.upper() == 'Z':
            sel = z.equal(coord, epsilon=epsilon)
            
        return move_selection(
            mesh        = mesh, 
            selection   = sel, 
            offset      = offset,
            axis        = axis,
            summit      = summit,
            title       = None,
            )
    
# ===========================================================================
# Flat cap
# ===========================================================================

def build_flat_cap(mesh: Mesh, selection: Boolean, target: Vector = None, title="flat_cap"):

    with Layout(title, color='MACRO'):

        if target is None:
            target = mesh.points.attribute_statistic(nd.position).mean

        mesh = mesh.edges[selection].extrude(offset=(target-nd.position).normalize(), offset_scale=.002)
        top = mesh.top
        mesh = mesh.edges[top].extrude(offset=(target-nd.position))
        top = mesh.top
        mesh[top].merge_by_distance()

        return mesh

      