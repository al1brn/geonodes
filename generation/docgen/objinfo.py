"""
Created on Tue Sep 10 07:44:18 2024

@author: alain


$ DOC START

Python object info

Documentation is based on structure information on objects to document

$ DOC END

created : 2024 09 14

"""

from importlib import import_module
import inspect
from pprint import pprint
from pathlib import Path
import re

from .parser import parse_meta_comment, extract_source, replace_source, del_margin, extract_lists

# =============================================================================================================================
# List item info

EMPTY  ='_EMPTY'
            
class ListItem:
    
    
    def __init__(self, name, type=None, default=EMPTY, description=None, **kwargs):
        """ An information line into a list
        
        This class is used to information displayed in a single lines.
        
        The line is intended to be displayed as `name (type = default) : description`.
        
        Properties
        ----------
        - name (str) : name attribute
        - type (str)  : type attribute
        - default (str) : default attribute
        - description (str) : description        
        """
        
        self.name        = name
        self.type        = type
        self.default     = default
        self.description = description
        
        for k, v in kwargs:
            setattr(self, v)
        
    def __str__(self):
        s = f"- {self.name}"
        if self.has_type or self.has_default:
            s += " ("
            if self.has_type:
                s += self.type
            if self.has_default:
                s += f" = {self.default}"
            s += ")"
        
        if self.description is not None:
            s += f" : {self.description}"
            
        return s
            
    @property
    def has_type(self):
        """ Check if <#type> is not None
        
        Returns
        -------
        - bool
        """
        return self.type is not None
    
    @property
    def has_default(self):
        """ Check if <#default> is different from <#EMPTY>
        
        Returns
        -------
        - bool
        """
        return self.default != EMPTY
    
    @property
    def has_description(self):
        """ Check if <#description> is not None
        
        Returns
        -------
        - bool
        """
        return self.description is not None
        
    @classmethod
    def FromParameter(cls, param, description=None):
        """ Create an instance from the python paramer description.
        
        Returns
        -------
        - ListItem
        """
        name    = param.name
        type    = EMPTY if param.annotation == param.empty else param.annotation
        default = EMPTY if param.default == param.empty else param.default
        return cls(name, type=type, default=default, description=None)

# =============================================================================================================================
# Base information

class Object_:
    
    obj_type = None
    
    def __init__(self, name, comment=None, **kwargs):
        """ Root class for informations on python objects
        
        The minimum information is <#name> and <#comment> can be completed
        by sub classes.
        
        Properties
        ----------
        - name (str) : module name, class name, property name...
        - comment (str) : comment in __doc__
        - obj_type (str) : (read only) name of the object type 
        
        Arguments
        ---------
        - name (str) : object name
        - comment (str = None) : comment
        - kwargs : additional properties
        """
        
        self.name    = name
        self.comment = del_margin(comment)
        self.hidden  = False
        
        for k, v in kwargs.items():
            setattr(self, k, v)
            
    def __str__(self):
        return f"<{type(self).__name__} {self.name}>"
            
    def get(self, prop_name, default=None):
        """ Get an optional property
        
        Arguments
        ---------
        - prop_name (str) : name of the property to read
        - default (any = None) : default value if the property doesn't exist
        
        Returns
        -------
        - any : the property or None if it doesn't exist
        """

        if hasattr(self, prop_name):
            return getattr(self, prop_name)
        else:
            return default
        
    # ====================================================================================================
    # Create from a python object
        
    @classmethod
    def FromObject(cls, object, name=None):
        return None
    
    # ====================================================================================================
    # Parse the comment

    def parse_comment(self):
        """ Collect extra information from the comment
        
        The default comment parser extracts meta information for doc generator:
        - $ DOC START : ignore lines above
        - $ DO END : ignore lines after
        - $ SET prop = 123 : pass properties to the doc generator 
        
        Returns
        -------
        - str : self.comment
        """
        
        if self.comment is None:
            return None
        
        comment, props = parse_meta_comment(self.comment)
        if len(props):
            self._meta = props
            
        self.comment = comment
        
        return self.comment
    
    # =============================================================================================================================
    # Print the content
        
    def print(self):
        print(str(self))
        

# =============================================================================================================================
# Property Info
            
class Property_(Object_):
    
    obj_type = 'property'
    
    def __init__(self, name, comment=None, type=None, default=EMPTY, fget=None, fset=None, **kwargs):
        """ Information on property
        
        Properties
        ----------
        - type (str) : type of the property
        - default (str) : default value
        - fget (Function_) : getter <!Function_>
        - fset (Function_) : setter <!Function_>
        
        Arguments
        ---------
        - name (str) : object name
        - comment (str = None) : comment
        - type (str = None) : type of the property
        - default (str = EMPTY) : default value
        - fget (Function_ = None) : getter <!Function_>
        - fset (Function_ = None) : setter <!Function_>        
        """
        super().__init__(name, comment, type=type, default=default, fget=fget, fset=fset, **kwargs)
        
    @classmethod
    def FromObject(cls, object, name=None, verbose=False):
        """ Create a Property_ instance from a property
        
        > [!NOTE]
        > If name is None, the name is read from fget
        
        Arguments
        ---------
        - object (property) : the object the scan
        - name (str = None) : name
        """
        if name is None:
            try:
                name = object.fget.__name__
            except:
                print(f"WARNNG: impossible to get the property name of object of type '{type(object)}'")
                name = 'UNDEFINED'
            
        fget, fset = None, None
        try:
            fget = None if object.fget is None else Function_.FromObject(object.fget)
        except:
            pass

        try:
            fset = None if object.fset is None else Function_.FromObject(object.fset)
        except:
            pass
        
        if verbose:
            print("Property", name)
        
        return cls(name, inspect.getdoc(object), fget=fget, fset=fset)
    
    @classmethod
    def FromStatic(cls, object, name=None):
        """ Creare a Property_ instance from a static property in a module or a class
        
        Arguments
        ---------
        - object
        - name (str = None)
        
        Returns
        -------
        - Property_
        """        
        stype = object.__name__ if hasattr(object, '__name__') else type(object).__name__
        try:
            sdef = str(object)
        except:
            sdef = '???'
            
        if len(sdef) > 30:
            sdef = sdef[:30] + '...'
            
        return cls(name, type=stype, default=sdef)
    
    # =============================================================================================================================
    # Print the content
    
    def print(self):
        fget = '-' if self.fget is None else 'X'
        fset = '-' if self.fset is None else 'X'
        stype = '' if self.type == EMPTY else self.type
        sdef  = '' if self.default == EMPTY else self.default
        print(f"P {self.name} {fget}{fset} {stype} ({sdef})")
    
# =============================================================================================================================
# Function info
        
class Function_(Object_):
    
    obj_type = 'function'
    
    def __init__(self, name, comment=None, signature=None, decorators=None, arguments=None, raises=None, returns=None, **kwargs):
        """ Description of a function

        Properties
        ----------
        - signature (str) : function signature
        - decorators(list) : list of decorators
        - arguments (list) : list of <!ListItem>
        - raises (list) : list of <!ListItem>
        - returns (list) : list of <!ListItem>
        
        Arguments
        ---------
        - name (str) : object name
        - comment (str = None) : comment
        - signature (str = None) : function signature
        - decorators(list = None) : list of decorators
        - arguments (list = None) : list of <!ListItem>
        - raises (list = None) : list of <!ListItem>
        - returns (list = None) : list of <!ListItem>
        """
        super().__init__(name, comment, signature=signature, **kwargs)
        
        self.decorators = [] if decorators is None else decorators
        self.arguments  = [] if arguments  is None else arguments
        self.raises     = [] if raises     is None else raises
        self.returns    = [] if returns    is None else returns
        
    @classmethod
    def FromObject(cls, object, name=None, verbose=False):
        """ Create a Function_ instance from a function
        
        > [!NOTE]
        > If **name** argument is none, `object.__name__` is taken.
        
        Arguments
        ---------
        - object (function) : the object to scan
        - name (str = None) : name of the object
        """
        
        if name is None:
            name = object.__name__
            
        if verbose:
            print(f"Function", name)
            
        try:
            sig = inspect.signature(object)        
        except:
            sig = '()'

        function_ = cls(name, inspect.getdoc(object), signature=str(sig))
        
        # ----- Parse the parameters in the signature if it exists
        
        if not isinstance(sig, str):
            for param in sig.parameters.values():
                function_.arguments.append(ListItem.FromParameter(param))
                
        # ----- Parse the comment
            
        function_.parse_comment()

        return function_
    
    def parse_comment(self):
        """ Function comment parser
        
        The parser looks for list names Arguments, Raises and Returns.
        """
        
        if super().parse_comment() is None:
            return None
        
        # ----------------------------------------------------------------------------------------------------
        # Extract the lists from the comment
        
        comment, lists = extract_lists(self.comment, 'arguments', 'raises', 'returns')
        
        # ----------------------------------------------------------------------------------------------------
        # Arguments : can complete information from signature
        
        for list_name in ('arguments', 'raises', 'returns'):
            
            list_ = lists.get(list_name)
            
            if list_ is not None:
                for arg in list_:
                    
                    name = arg['name']
                    cur = None
                    
                    # ----- Already documented ?
                    
                    for a in getattr(self, list_name):
                        if a.name == name:
                            cur = a
                            break
                        
                    # ----- No, let's create it
                    
                    if cur is None:
                        cur = ListItem(name)
                        getattr(self, list_name).append(cur)
                        
                    # ---- Complete with a lesser priority
                    
                    if not cur.has_type and arg.get('type') is not None:
                        cur.type = arg['type']
                    if not cur.has_default and arg.get('default') is not None:
                        cur.default = arg['default']
                    if not cur.has_description and arg.get('description') is not None:
                        cur.comment = arg['description']
                
        self.comment = comment

    # =============================================================================================================================
    # Print the content
    
    def print(self):
        print(f"Function {self.name}{self.signature}")
        if self.comment is not None:
            print("-"*20)
            print(self.comment)
            print("-"*20)
            
        for list_name in ('arguments', 'raises', 'returns'):
            if len(getattr(self, list_name)):
                print(list_name)
                print("-"*len(list_name))
                for arg in getattr(self, list_name):
                    print(str(arg))
                    
# =============================================================================================================================
# Root class for Info with members
        
class Parent(Object_):
    def __init__(self, name, comment=None, **kwargs):
        """ Root class from Class and Module.
        
        This class creat a <#members> dictionary
        
        Properties
        ----------
        - members (dict) : dictionary of members
        """
        super().__init__(name, comment, **kwargs)
        self.members = {}
        
    def __str__(self):
        return f"<{type(self).__name__} {self.name} {len(self.members)}>"
    
    def __repr__(self):
        return str(self) + "\n- " + "\n- ".join([str(member) for member in self.members.values()])
        
    def add_member(self, object_):
        if object_ is None:
            return
        self.members[object_.name] = object_
        return object_
    
# =============================================================================================================================
# Class Info
        
class Class_(Parent):
    
    obj_type = 'class'
    
    def __init__(self, name, comment=None, bases=None, **kwargs):
        """ Information on a class
        
        Properties
        ----------
        - bases (list) : list of base classes
        - _init (Function_) : <!Function_> description for __init__ function if it exists 
        
        Arguments
        ---------
        - name (str) : class name
        - comment (str) : comment
        - bases (list) : list of base classes
        - kwargs : complementary information
        """
        super().__init__(name, comment, **kwargs)
        self.bases = [] if bases is None else bases
        self._init = None
        
    @classmethod
    def FromObject(cls, object, name=None, verbose=False):
        """ Create an Class_ instance from a python class

        > [!NOTE]
        > If **name** argument is none, `object.__name__` is taken.
        
        The method `__init__` is not stored in the <#members> dictionary but in <#_init> property.
        
        > [!CAUTION]
        > All dunder methods are ignored in this version
        
        Arguments
        ---------
        - object (function) : the object to scan
        - name (str = None) : name of the object
        """
        
        if name is None:
            name = object.__name__
            
        if verbose:
            print("Class", name)
        
        class_ = cls(object.__name__, inspect.getdoc(object), [b.__name__ for b in object.__bases__])

        for m_name, m_obj in inspect.getmembers(object):
            
            is_init = m_name == '__init__'
            if is_init:
                class_._init = Function_.FromObject(m_obj)
                
            else:
                if m_name[:2] == '__':
                    continue
                
                if inspect.isclass(m_obj):
                    class_.add_member(Class_.FromObject(m_obj, name=m_name))
                
                elif inspect.isfunction(m_obj):
                    class_.add_member(Function_.FromObject(m_obj, name=m_name))
                
                elif inspect.ismethod(m_obj):
                    class_.add_member(Function_.FromObject(m_obj.__func__, name=m_name))
                
                else:
                    class_.add_member(Property_.FromStatic(m_obj, name=m_name))

        return class_
            
    # =============================================================================================================================
    # Print the content
    
    def print(self):
        print('='*50)
        print(f"Class {self.name} {self.bases}")
        print()
        if self.comment is not None:
            print(self.comment)
            print("-"*20)
        if self._init is not None:
            self._init.print()

        print()
        for obj_ in self.members.values():
            obj_.print()

# =============================================================================================================================
# Class Info

class Module_(Parent):
    
    obj_type = 'module'
    
    PACKAGES = {}
    
    def __init__(self, name, comment=None, package=None, **kwargs):
        """ Information on a module
        
        Arguments
        ---------
        - name (str) : class name
        - comment (str) : comment
        - package (str) : package
        - kwargs : complementary information        
        """
        super().__init__(name, comment, **kwargs)
        self.package = str(package)
        self.PACKAGES[self.package] = self
        
    def is_same_package(self, package):
        return package.split('.')[0] == self.package.split('.')[0]
        
    @classmethod
    def FromObject(cls, object, name=None, verbose=False):
        """ Create an Module_ instance from a python module

        > [!NOTE]
        > If **name** argument is none, `object.__name__` is taken.
        
        Arguments
        ---------
        - object (function) : the object to scan
        - name (str = None) : name of the object
        """
        
        package = str(object.__package__)
        if package in cls.PACKAGES:
            return cls.PACKAGES[package]
            
        if name is None:
            name = object.__name__
            
        if verbose:
            print(f"Module '{name}', package '{package}'...")
        
        module_ = cls(object.__name__, inspect.getdoc(object), package=package)
        for m_name, m_obj in inspect.getmembers(object):

            if m_name[:2] == '__':
                continue
            if m_name in module_.members:
                continue
            
            
            if inspect.ismodule(m_obj):
                package = str(m_obj.__package__)
                if not module_.is_same_package(package):
                    if verbose:
                        print(f"Module '{module_.name}' ignore sub module '{m_name}': package '{package}' not in '{module_.package}'")
                    continue
                
                module_.add_member(Module_.FromObject(m_obj, name=m_name))
            
            elif inspect.isfunction(m_obj):
                module_.add_member(Function_.FromObject(m_obj, name=m_name))
            
            elif inspect.isclass(m_obj):
                module_.add_member(Class_.FromObject(m_obj, name=m_name, verbose=verbose))
            
            else:
                module_.add_member(Property_.FromStatic(m_obj, name=m_name))
            
        return module_
    
    # =============================================================================================================================
    # Print the content

    def print(self):
        print('='*50)
        print(f"Module {self.name} {len(self.members)}")
        if self.comment is not None:
            print(self.comment)
            print("-"*20)
        #if self._init is not None:
        #    self._init.print()
        
        print()
        print("Modules")
        print('-------')
        for oi in self.members.values():
            if oi.obj_type == 'module':
                print(f"- {oi.name}")
        print()
        
        print()
        print("Properties")
        print('----------')
        for oi in self.members.values():
            if oi.obj_type == 'property':
                oi.print()
        print()
        
        print("Classes")
        print('-------')
        for oi in self.members.values():
            if oi.obj_type == 'class':
                print(str(oi))
        print()

        print("Functions")
        print('---------')
        for oi in self.members.values():
            if oi.obj_type == 'function':
                print(str(oi))
        print()

        
        
        
        
    


# =============================================================================================================================
# Structures describing documented objects

def new_struct(obj, name, comment=None, subs=None, **kwargs):
    struct = {'obj' : obj, 'name': name, 'comment': comment, **kwargs}
    if subs is not None:
        struct['subs'] = subs
    return struct

def new_file(name, comment=None, subs=None):
    return new_struct('file', name, comment, subs={} if subs is None else subs)

def new_class(name, comment=None, subs=None, inherits=None):
    return new_struct('class', name, comment, subs={} if subs is None else subs, inherits=[] if inherits is None else inherits)

def new_function(name, comment=None, decorators=None, args=None, arguments=None, raises=None, returns=None):
    
    function = new_struct('function', name, comment)
    
    function['decorators'] = [] if decorators is None else decorators
    function['args']       = [] if args       is None else args
    function['arguments']  = [] if arguments  is None else arguments
    function['raises']     = [] if raises     is None else raises
    function['returns']    = [] if returns    is None else returns
    
    return function

def new_property(name, comment=None, type=None, default=None, setter=None, getter=None):
    prop = new_struct('property', name, comment, type=type, default=default)
    if getter is not None:
        prop['getter'] = getter
    if setter is not None:
        prop['setter'] = setter
    return prop


def struct_search(struct, **kwargs):
    
    ok = True
    for key, value in kwargs.items():
        if struct.get(key) != value:
            ok = False
            break
        
    if ok:
        return struct
    
    if struct.get('subs'):
        for sub in struct['subs'].values():
            stc = struct_search(sub, **kwargs)
            if stc is not None:
                return stc
            
    return None

def struct_iter(struct, f, *args, **kwargs):
    
    ok = True
    for key, value in kwargs.items():
        if struct.get(key) != value:
            ok = False
            break
        
    if ok:
        res = f(struct, *args)
        if res == True:
            return struct
        
    if struct.get('subs'):
        for sub in struct['subs'].values():
            stc = struct_iter(sub, f, *args, **kwargs)
            if stc is not None:
                return stc
            
    return None

def struct_list(struct, name_only=True, **kwargs):

    structs = []

    def add(stc):
        if name_only:
            structs.append(stc['name'])
        else:
            structs.append(stc)
            
    struct_iter(struct, add, **kwargs)
    
    return structs

# =============================================================================================================================
# Parse comment (for meta tage)

def parse_meta_comment(comment):
    """ Parse the comment itsel to extract meta tags
    
    Tags are `$` starting at the beginin of the line followed by a command line:
        
    - DOC START : extract comment from here
    - DOC END : don't extract after after
    - SET property value : property value pair
    """
    
    meta = r"^\$ *(?P<command>[\w]*) *(?P<param>.*)\n"
    
    props = {}
    
    index = 0
    while True:

        m = re.search(meta, comment[index:], flags=re.MULTILINE)

        if m is None:
            return comment, props
        
        command = m.group('command').upper()
        param   = m.group('param')
        if param is not None:
            param = param.strip()
        
        # ----------------------------------------------------------------------------------------------------
        # DOC command
        
        if command == 'DOC':
            if param is None or param == '' or param.upper() == 'START':
                comment = comment[index + m.span()[1]:]
                index = 0
                
            elif param.upper() == 'END':
                return comment[:index + m.span()[0]], props
            
            else:
                print(f"CAUTION: invalid meta command {m.group(1)}, DOC option must be in ('START','END') not '{param}'")
                index += m.span()[1]
                
        # ----------------------------------------------------------------------------------------------------
        # SET command
        
        elif command == 'SET':
            
            try:
                exec(param, None, props)
            except Exception as e:
                print(f"CAUTION: invalid meta command {m.group(1)}, impossible to exec instruction:\n> {param}'\n{str(e)}")
            
            comment = comment[:index + m.span()[0]] + comment[index + m.span()[1]:]
            index += m.span()[0]
                
    return comment, props

    

# =============================================================================================================================
# Parse python source code

def parse_file_source(text, file_name='File'):
    """ Parse a python file source

    The parser returns a dictionary giving the content of the file:

    - file
      - comment
      - subs : dict of classes and functions
    - class
      - name
      - comment
      - inherits (list)
      - subs : dict of properties and functions (methods)
    - function
      - name
      - comment
      - args (str)
      - decorators (list of strs)
      - raises: list of dicts for raises
      - arguments: list of dicts for arguments
      - returns: list of dicts for returns
    - property
      - name
      - comment
      - type
      - default
      - setter : function
      - getter : function

    The parsing is done with regular expressions.

    Arguments
    ---------
    - text (str) : source code to parse

    Returns
    -------
    - dict : classes and functions
    """

    # ----------------------------------------------------------------------------------------------------
    # Clean to properly apply regex expressions

    clean, comments, strings = clean_python(text)

    # ----------------------------------------------------------------------------------------------------
    # Documentation result

    file_subs= {}

    file = new_file(file_name, comments[0] if len(comments) else None, subs=file_subs)

    # ----------------------------------------------------------------------------------------------------
    # Look for class definitions:
    #
    # class CLASS_NAME (...):
    #     <COMMENT index>

    class_expr = r"^class\s*([\w]*)\s*(\(([^\)]*)\))*\s*:\s*([\n\s])*(<COMMENT ([0-9]+)>)?"

    starts = []
    for m in re.finditer(class_expr, clean, flags=re.MULTILINE):

        class_name = m.group(1)
        starts.append((m.span()[0], class_name))

        # ----- Comment

        icomm = m.group(6)
        comment = None if icomm is None else comments[int(icomm)]

        # Extract properties from the comment

        comment, lists = extract_lists(comment, 'properties')

        # ----- Create the class
        
        inherits = m.group(3)
        if inherits is not None:
            inherits = [s.strip() for s in m.group(3).split(',')]

        class_ = new_class(class_name, comment, inherits=inherits)

        # Add the properties declared in the comment

        props = lists.get('properties', [])
        for info in props:
            prop_name = info['name']
            class_['subs'][prop_name] = new_property(prop_name, info['description'], type=info['type'], default=info['default'])

        # ----- Put the class in the subs of the file

        file_subs[class_name] = class_


    # ----- Build the list of classes order by their appearance in the source file
    # This list will permit to know to whom further methods must be attached
    # 
    # Note that this list of positions in text doesn't include positions of functions
    # Hence, the following structure
    #
    # Class ClassName:
    #    def method
    #
    # def function_name:
    #     def sub_function
    #
    # Because of its indentation, sub_function will be interpreted as a method of ClassName
    # 
    # To solve that, this list will be updated with functions

    starts = sorted(starts, key=lambda x: x[0])

    # ----------------------------------------------------------------------------------------------------
    # Look for functions definitions:
    #
    #     @decorator
    #     def NAME(...):
    #         <COMMENT index>

    func_expr = r"^(((\s*)@([\w\.]*)\s*\n)*)(\s*)def +(\w*)\s*(\((.*)\)\s*):\s*([\n\s])*(<COMMENT ([0-9]+)>)?"

    for m in re.finditer(func_expr, clean, flags=re.MULTILINE):

        # ----------------------------------------------------------------------------------------------------
        # Name

        name = m.group(6)

        # ----------------------------------------------------------------------------------------------------
        # Decorators

        is_setter = False
        is_getter = False
        decorators= []
        for decorator in m.group(1).split('\n'):
            deco = decorator.strip()
            if deco == "":
                continue
            if deco.endswith('.setter'):
                deco = '@setter'
                is_setter = True
            if deco == '@property':
                is_getter = True
            decorators.append(deco)
            
        # ----------------------------------------------------------------------------------------------------
        # Argument string

        args = re.sub(r"  +", " ", m.group(8))
        args_list = args.split(',')
        if len(args_list) and args_list[0] in ('self', 'cls'):
            args = ','.join(args_list[1:]).strip()

        # ----------------------------------------------------------------------------------------------------
        # Indentation

        if m.group(5) is None:
            indent = 0
        else:
            indent = len(m.group(5))

        # ----------------------------------------------------------------------------------------------------
        # Comment

        icomm = m.group(11)
        comment = None if icomm is None else comments[int(icomm)]

        # Extract lists

        comment, lists = extract_lists(comment, ['raises', 'arguments', 'returns', 'properties'])

        # ----------------------------------------------------------------------------------------------------
        # Create the function dict

        function_ = new_function(name, comment, decorators=decorators, args=args)

        # Add the lists

        for title, items in lists.items():
            function_[title] = items

        # ----------------------------------------------------------------------------------------------------
        # Place the function at file level or in a class

        # ----- Indentation is null : this is function at file level

        if indent == 0:

            file_subs[name] = function_
            
            # update start positions to avoid a sub function to be interpreted as a previous class method
            
            starts = sorted(starts + [(m.span()[0], name)], key=lambda x: x[0])


        # ----- This is a class method

        else:

            # ----- Let's find the last class declared before the function

            func_start = m.span()[0]

            last_class_name = None
            for start, class_name in starts:
                if func_start < start:
                    break
                last_class_name = class_name
                
            if last_class_name is None:
                raise Exception(f"Sorry shouldn't append: wrong indentation for function '{name}'")

            class_ = file_subs[last_class_name]
            
            # it's a sub function: don't care
            if class_['obj'] != 'class':
                continue
            
            class_subs = class_['subs']

            # ----- If the method is a getter or a getter we create a class property

            if is_setter or is_getter:
                prop_ = class_subs.get(name)
                if prop_ is None:
                    prop_ = new_property(name)
                    class_subs[name] = prop_

                if is_setter:
                    prop_['setter'] = function_
                else:
                    prop_['getter'] = function_
                    if len(function_['returns']):
                        prop_['type'] = function_['returns'][0]['name']
                    if prop_['comment'] is None:
                        prop_['comment'] = function_['comment']
                        
            # ----- It is the __init__ method
            
            elif name == '__init__':
                if class_['comment'] is None:
                    class_['comment'] = function_['comment']
                    function_['comment'] = None
                    
                class_['args'] = function_.get('args')
                function_['args'] = None
                
                props = function_.get('properties', [])
                for info in props:
                    prop_name = info['name']
                    if class_['subs'].get(prop_name) is None:
                        class_['subs'][prop_name] = new_property(prop_name, info['description'], type=info['type'], default=info['default'])
                
                    
                class_['__init__'] = function_

            # ----- Otherwise we create a method

            else:
                class_subs[name] = function_
                
    # ----------------------------------------------------------------------------------------------------
    # Parse meta commands in comment
    
    def meta(struct):
        comment = struct['comment']
        if comment is None:
            return
        comment, props = parse_meta_comment(comment)
        
        struct['comment'] = comment
        for k, v in props:
            struct[k] = v
            
    struct_iter(file, meta)
    

    return file

# =============================================================================================================================
# Parse source files to build the reference documentation

def parse_files(folder, key="", verbose=False):
    """ Load files from a folder.

    All the files with `.py` extension are parsed.

    Arguments
    ---------
    - folder (str) : main folder
    - root (str=None) :

    Returns
    -------
    - dict
    """

    files = {}
    root_key = Path(key)

    for fpath in Path(folder).iterdir():
        if not fpath.match("*.py"):
            continue

        file_key = str(root_key / fpath.stem)
        if verbose:
            print(f"Loading {fpath.name} in file '{file_key}'")
            
        files[file_key] = parse_file_source(fpath.read_text(), fpath.stem)

    return files

# =============================================================================================================================
# Class : capture inheritance from another class

def capture_inheritance(class_, base_, remove=True):
    """ Capture properties et methods from another class
    
    Allow to document class items as it were not inherited.
    
    > [!Note]
    > if the name of the base class is in the inherits list, it is removed from it
    
    Arguments
    ---------
    - class_ (dict) : the class to enrich
    - base_ (dict) : the class to capture properties and methods from
    - remove (bool = True) : remove base name from inheritance list
    """
    
    for sub in base_['subs'].values():
        
        # Sub is overloaded or is __init__
        
        if sub['name'] in list(class_['subs'].keys()) + ['__init__']:
            continue

        # Let's capture it
        
        class_['subs'][sub['name']] = sub
        
    # Let's suppress the entrance in inherit
    
    if remove and class_.get('inherits') is not None:
        if base_['name'] in class_['inherits']:
            class_['inherits'].remove(base_['name'])
            
    return class_

def capture_inheritances(class_, files_, include=None, exclude=[], verbose=True):
    """ Capture inheritances
    
    Allow to document class items as it were not inherited.
    
    > [!Note]
    > if the name of the base class is in the inherits list, it is removed from it
    
    Arguments
    ---------
    - class_ (dict) : the class to enrich
    - files_ (dict) : the hierarchy containing base classes to capture from
    - include (list = None) : limit capture to the given list
    - exclude (list = []) : exclude classes in the given list
    """
    
    if class_.get('inherits') is None:
        return class_
    
    to_capture = class_['inherits'] if include is None else include
    captured = []
    
    for base_name in to_capture:
        
        if base_name in exclude:
            continue
        
        base_ = struct_search(files_, obj='class', name=base_name)
        if base_ is None:
            continue
        
        if verbose:
            print(f"Capture inheritance {class_['name']} <- {base_name}")
        
        capture_inheritance(class_, base_, remove=False)
        captured.append(base_name)
        
    for base_name in captured:
        if base_name in class_['inherits']:
            class_['inherits'].remove(base_name)
            
    return class_

# =============================================================================================================================
# Tests

# -----------------------------------------------------------------------------------------------------------------------------
# Dump the content of a dict

def dump_dict(d, indent=0):

    INCR = 4

    if len(d) == 0:
        return

    print(f"{' '*indent}{d['name']} ({d['obj' ]})")
    if d['comment'] is not None:
        print(f"{' '*indent}> {d['comment'][:20]}...")
    print()

    for sub, sub_ in d.get('subs', {}).items():
        dump_dict(sub_, indent + 1*INCR)


def test():
    text = Path(__file__).read_text()

    file = parse_file(text)

    #dump_dict(file)

    pprint(file['subs']['clean_python'])
    pprint(file['subs']['Text'])


def test_folder(folder=None, sub_folders=[]):
    if folder is None:
        folder = Path(__file__).parents[0]
        print(folder)
        
    d = parse_files(folder, sub_folders=sub_folders, verbose=True)
    pprint(d)
    
    




