"""Node parameter introspection and argument information."""

import bpy

IGNORE_PARAMS = ['color_ramp', 'paired_output']

# ====================================================================================================
# Node parameter
# ====================================================================================================

class NodeParam:
    def __init__(self, bnode, name, value, param_type):
        self.bnode      = bnode
        self.name       = name
        self.value      = value
        self.param_type = param_type
        self.enums      = None

    def __str__(self):
        enums = f" {self.enums}" if self.enums is not None else ""
        return f"<Parameter {self.name} {self.param_type}{enums}>"

    @classmethod
    def Parameter(cls, bnode, name):

        if name in IGNORE_PARAMS:
            return None

        value = getattr(bnode, name)
        param_type = None

        s = str(value)

        # ----- It is an object

        if s.startswith('<'):

            # ----- VectorFont
            if isinstance(value, bpy.types.VectorFont):
                value = None
                param_type = 'FONT'

            if param_type is None:
                return None

        # ----- Let's initialize the param

        if param_type is None:
            param_type = 'VALUE'
        param = cls(bnode, name, value, param_type)

        # ----- It could be an enum list

        if isinstance(value, (str, set)):
            enums = param.get_enum_list()
            if enums is not None:
                prop = bnode.bl_rna.properties[name]
                param.param_type = 'ENUM_FLAG' if prop.is_enum_flag else 'ENUM'
                param.enums      = enums

        # ----- Done

        return param

    @property
    def current_value(self):
        return getattr(self.bnode, self.name)

    @current_value.setter
    def current_value(self, value):
        setattr(self.bnode, self.name, value)

    # ====================================================================================================
    # Get the valid values of an enum params

    def get_enum_list(self, user_version: bool = False) -> tuple | None:
        """ Get the list of valid values of a node parameter.

        The list can vary when node parameters are changed.

        Parameters
        ----------
        - user_version (bool = False) user version

        Returns
        -------
        tuple of valid values or None if the parameter is not a enum parameter
        """
        if not isinstance(self.value, (str, set)):
            return None
        
        prop = self.bnode.bl_rna.properties[self.name]
        if prop.type != 'ENUM':
            return None
        
        # Invalid enum values raise TypeError or ValueError depending on the property.
        try:
            setattr(self.bnode, self.name, {'GERR'} if prop.is_enum_flag else 'GERR')

        except (TypeError, ValueError) as e:
            msg = str(e)
            token = 'not found in '
            i = msg.find(token)
            if i < 0:
                return None

            vals = eval(msg[i + len(token):])
            # Only one possible value : ('VALUE') is evaluated as a str, not a singleton of a str
            if isinstance(vals, str):
                vals = (vals,)

            if user_version:
                transco = {enum_item.identifier: enum_item.name for enum_item in prop.enum_items}
                return tuple([transco[v] for v in vals])
            else:
                return vals

        return None

    # ====================================================================================================
    # Depends upon another parameter

    def dependance_with(self, other):

        assert other.param_type == 'ENUM' and self.param_type == 'ENUM'


        for first, second in [(self, other), (other, self)]:

            first_value = first.current_value
            second_value = second.current_value

            var_enums = {}
            ref = None
            all_same = True
            for value in first.get_enum_list():
                first.current_value = value
                var_enums[value] = second.get_enum_list()
                if ref is None:
                    ref = var_enums[value]
                else:
                    all_same = all_same and (ref == var_enums[value])

            first.current_value = first_value
            second.current_value = second_value

            if not all_same:
                return {
                    "master": first.name,
                    "slave": second.name,
                    "var_enums": var_enums,
                }

        return {}

    # ====================================================================================================
    # Argument information

    @property
    def comment(self):

        if self.param_type == 'ENUM':
            s = f"{self.name} : Literal{list(self.get_enum_list(user_version=True))}\n    parameter `{self.name}`\n"
            if s == 'Literal[]':
                return 'str'
            else:
                return s

        elif self.param_type == 'ENUM_FLAG':
            return f"{self.name} : set[Literal{list(self.get_enum_list(user_version=True))}]\n    parameter `{self.name}`\n"
            
        elif self.param_type == 'FONT':
            return f"{self.name} : Blender VectorFont | str\n    VectorFont, or name of a valid font in bpy.types.fonts (see `utils.get_font`)\n"

        else:
            return f"{self.name} : {type(self.value).__name__}\n    parameter `{self.name}`\n"
        
        # OLD


        if self.param_type == 'ENUM':
            return f"{self.name} (str): parameter '{self.name}' in {self.get_enum_list(user_version=True)}"

        elif self.param_type == 'FONT':
            return f"{self.name} (Blender VectorFont | str): VectorFont, or name of a valid font in bpy.types.fonts (see `utils.get_font`)"

        else:
            return f"{self.name} ({type(self.value).__name__}): parameter '{self.name}'"

    @property
    def arg_value(self):
        if self.param_type == 'VALUE':
            if isinstance(self.value, str):
                return f"'{self.value}'"
            else:
                return str(self.value)

        elif self.param_type == 'ENUM':
            return f"'{self.value}'"

        elif self.param_type == 'ENUM_FLAG':
            return repr(self.value)

        elif self.param_type == 'FONT':
            return None

        else:
            assert(False)

    @property
    def set_value(self):
        if self.param_type == 'FONT':
            return f"utils.get_font({self.name})"
        else:
            return self.name
