
# ==============================================================================================================
# Global functions

def compare(self, b=None, c=None, angle=None, epsilon=None, data_type='FLOAT', mode='ELEMENT', operation='EQUAL'):
    """ Method compare using node NodeCompare

    Arguments
    ---------
        a               : Float: self socket
        b               : Float
        c               : Float
        angle           : Float
        epsilon         : Float

        data_type       : str
        mode            : str
        operation       : str

    Returns
    -------
        Boolean
    """

    return nodes.NodeCompare(a=self, b=b, c=c, angle=angle, epsilon=epsilon, data_type=data_type, mode=mode, operation=operation).output

def join_strings(self, *strings):
    """ Method join_strings using node NodeJoinStrings

    Arguments
    ---------
        delimiter       : String: self socket
        strings         : String (multi input)

    Returns
    -------
        String
    """

    return nodes.NodeJoinStrings(*strings, delimiter=self).output

def accumulate_field(self, group_index=None, data_type='FLOAT', domain='POINT'):
    """ Method accumulate_field using node NodeAccumulateField

    Arguments
    ---------
        value           : Vector: self socket
        group_index     : Integer

        data_type       : str
        domain          : str

    Returns
    -------
        Sockets [leading (Float), trailing (Float), total (Float)]
    """

    return nodes.NodeAccumulateField(value=self, group_index=group_index, data_type=data_type, domain=domain).output

def field_at_index(self, value=None, data_type='FLOAT', domain='POINT'):
    """ Method field_at_index using node NodeFieldatIndex

    Arguments
    ---------
        index           : Integer: self socket
        value           : Float

        data_type       : str
        domain          : str

    Returns
    -------
        Float
    """

    return nodes.NodeFieldatIndex(index=self, value=value, data_type=data_type, domain=domain).output

def collection_info(self, separate_children=None, reset_children=None, transform_space='ORIGINAL'):
    """ Method collection_info using node NodeCollectionInfo

    Arguments
    ---------
        collection      : Collection: self socket
        separate_children : Boolean
        reset_children  : Boolean

        transform_space : str

    Returns
    -------
        Geometry
    """

    return nodes.NodeCollectionInfo(collection=self, separate_children=separate_children, reset_children=reset_children, transform_space=transform_space).output

def object_info(self, as_instance=None, transform_space='ORIGINAL'):
    """ Method object_info using node NodeObjectInfo

    Arguments
    ---------
        object          : Object: self socket
        as_instance     : Boolean

        transform_space : str

    Returns
    -------
        Sockets [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)]
    """

    return nodes.NodeObjectInfo(object=self, as_instance=as_instance, transform_space=transform_space).output

def scene():
    """ Method scene using node NodeSceneTime

    Arguments
    ---------

    Returns
    -------
        Sockets [seconds (Float), frame (Float)]
    """

    return nodes.NodeSceneTime().output



