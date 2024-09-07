import re
from pprint import pprint
from pathlib import Path

from .pyparser import Parser

# =============================================================================================================================
# Manages the documentation of a project
#
# Documentation is organized as a hierarchy of files
#
# Documentation comes from:
# - automatic building from files
# - manual adds

# =============================================================================================================================
# Section

class Section(list):
    def __init__(self, title, comment=None, with_sections_only=False, sort_sections=False):
        """ Elementary base of a documentation
        """
        super().__init__()
        self.title              = title
        self.comment            = comment
        self.with_sections_only = with_sections_only
        self.sort_sections      = sort_sections

    # ====================================================================================================
    # Target file name

    @property
    def md_file_name(self):
        return f"{self.title.lower().replace(' ', '_')}.md"

    # ====================================================================================================
    # Link to

    @property
    def link_token(self):
        return self.title.lower().replace(' ', '-')

    def link_to(self, url=""):
        if url != "":
            url += '#'
        return f"[{self.title}]({url}{self.link_token})"

    # ====================================================================================================
    # Get a section

    def get_section(self, title):
        for section in self:
            if section.title == title:
                return section
        return None

    @property
    def sorted_sections(self):
        return sorted(self, key=lambda s: s.title)

    @property
    def alphabetical_sections(self):
        alpha = {}
        for section in self:
            first = section.title[0].upper()
            sections = alpha.get(first)
            if sections is None:
                sections = Section(letter)
                sections.sort_sections = True
                alpha[first] = sections
            sections.append(section)
        return alpha

    # ====================================================================================================
    # Yield the documentation

    def build_header(self, indent=0):
        """ Yield the header part
        """
        yield '#'*(indent + 1) + ' ' + self.title + '\n\n'
        if self.comment is not None:
            yield self.comment + '\n\n'

    def build_sections(self, indent=0):
        """ Yield the sections parts
        """
        sections = self.sorted_sections if self.sort_sections else self
        for section in sections:
            for line in section.build(indent=indent + 1):
                yield line

    def build(self, indent=0):
        """ Yield the whole section
        """

        if self.with_sections_only and len(self) == 0:
            return

        for line in self.build_header(indent=indent):
            yield line

        for line in self.build_sections(indent=indent):
            yield line

        yield "\n"

    def print(self):
        print("-"*100)
        for line in self.build():
            print(line, end='')
        print()

# =============================================================================================================================
# Argument

class Argument(Section):
    def __init__(self, name, type=None, default=None, description=None):
        super().__init__(name, comment=description)
        self.type = type
        self.default = default

    def build(self, indent=0):
        yield f"- {self.title}"
        if self.type is None:
            if self.default is not None:
                yield f" (= {self.default})"
        else:
            yield f" ({self.type}"
            if self.default is None:
                yield ")"
            else:
                yield f" = {self.default})"
        if self.comment is None:
            yield "\n"
        else:
            yield f" : {self.comment}\n"

# =============================================================================================================================
# Return

class Return(Section):
    def __init__(self, name, description=None):
        super().__init__(name, comment=description)

    def build(self, indent=0):
        yield f"- {self.title}"
        if self.comment is None:
            yield '\n'
        else:
            yield f" : {self.comment}\n"

# =============================================================================================================================
# Arguments section

class Arguments(Section):
    def __init__(self):
        super().__init__('Arguments', with_sections_only=True)

    def build_header(self, indent=0):
        yield "Arguments:\n"
        yield "----------\n"

# =============================================================================================================================
# Arguments section

class Returns(Section):
    def __init__(self):
        super().__init__('Returns', with_sections_only=True)

    def build_header(self, indent=0):
        yield "Returns:\n"
        yield "--------\n"

# =============================================================================================================================
# Function section

class Function(Section):
    def __init__(self, name, comment=None):
        """ Section dedicated to function documentation.
        """
        super().__init__(name)
        self.append(Arguments())
        self.append(Returns())

        self.is_staticmethod = False
        self.is_classmethod  = False
        self.is_getter       = False
        self.is_setter       = False
        self.args            = None

        # ----------------------------------------------------------------------------------------------------
        # Extract arguments from comment

        context = 'COMMENT'
        new_comment = ""

        add_blank = False
        blank_count = 0
        for raw_line in comment.split("\n"):

            if add_blank:
                if blank_count < 1:
                    new_comment += "\n"
                    blank_count += 1
                add_blank = False

            line = raw_line.strip()
            if line[:8].lower() == 'argument':
                context = 'ARGUMENTS'
                continue
            elif line[:6].lower() == 'return':
                context = 'RETURNS'
                continue

            if context == 'COMMENT':
                if line == "":
                    add_blank = True
                else:
                    new_comment += line + "\n"
                    add_blank = False
                    blank_count = 0

            else:
                if line == "":
                    add_blank = True
                    continue

                if line[0] != '-':
                    context = 'COMMENT'
                    new_comment += '\n' + line + '\n'
                    add_blank = False
                    blank_count = 0
                    continue

                if line[1] == '-':
                    continue

                if context == 'ARGUMENTS':

                    expr = r"-\s*(\w+)\s*(\((\w+)\s*(=\s*(.+))?\))?(\s*:\s*(.+))?"
                    match = re.search(expr, line)

                    if match is None:
                        self.arguments.append(Argument(name = line[2:]))
                    else:
                        self.arguments.append(Argument(
                                name        = match.group(1),
                                type        = match.group(3),
                                default     = match.group(5),
                                description = match.group(7)))

                elif context == 'RETURNS':
                    expr = r"-\s*(\w+)(\s*:\s*(.+))?"
                    match = re.search(expr, line)

                    if match is None:
                        raise Exception(f"Return spec not correctly formatted\n{line}")

                    self.returns.append(Return(match.group(1), match.group(3)))

        self.comment = new_comment

    @property
    def arguments(self):
        return self.get_section('Arguments')

    @property
    def returns(self):
        return self.get_section('Returns')

    # ====================================================================================================
    # Initialize from a Doc class coming from pyparse

    @classmethod
    def FromDoc(cls, doc):
        inst = cls(doc.name, doc.comment)

        for deco in doc.decorators:
            if deco == '@classmethod':
                inst.is_classmethod = True
            elif deco == '@staticmethod':
                inst.is_staticmethod = True
            elif deco == '@property':
                inst.is_getter = True
            elif deco.find('.setter')> 0:
                inst.is_setter = True

        inst.args = doc.args

        return inst

# =============================================================================================================================
# Class documentation

class Class(Section):

    def __init__(self, class_name, comment):
        super().__init__(class_name, comment)

        self.append(Section('Properties', with_sections_only=True))
        self.append(Section('Methods', with_sections_only=True))

        self.bases = []

    @classmethod
    def FromDoc(cls, doc):
        inst = cls(doc.name, doc.comment)

        inst.bases.extend(doc.bases)

        for d in doc.funcs.values():
            inst.methods.append(Function.FromDoc(d))

        return inst

    @property
    def properties(self):
        return self.get_section('Properties')

    @property
    def methods(self):
        return self.get_section('Methods')

    # ====================================================================================================
    # Capture methods and properties from another class

    def capture_class(self, other):
        for section in other.properties:
            if self.properties.get_section(section.title) is None:
                self.properties.append(section)

        for section in other.methods:
            if self.methods.get_section(section.title) is None:
                self.methods.append(section)

        return self

    # ====================================================================================================
    # Build

    def build(self, indent=0):
        for line in super().build(indent=indent):
            yield line

        if len(self.bases):
            yield f"\n**inherits from** "
            for name in self.bases:
                yield name + " "
            yield '\n\n'

# =============================================================================================================================
# Classes documentation

class Classes(Section):

    def __init__(self, class_name, comment):
        super().__init__(class_name, comment, sort_sections=True)

    def build_sections(self, indent=0):
        """ Yield the sections parts
        """
        sections = self.sorted_sections
        for section in sections:
            yield f"- [{section.title}]({section.link_to()})\n"

# =============================================================================================================================
# Module documentation

class Module:

    def __init__(self, name, text):

        self.name = name
        self.docs = Parser(text).documentation()

        self.classes   = {}
        self.functions = {}

        for doc in self.docs:
            if doc.is_class:
                self.classes[doc.name] = Class.FromDoc(doc)
            else:
                self.functions[doc.name] = Function.FromDoc(doc)

# =============================================================================================================================
# Project documentation

class ProjectDocumentation:

    def __init__(self, name, doc_folder):

        self.name       = name
        self.doc_folder = Path(doc_folder)

        # ----- Modules contain the source modules with their classes and functions

        self.modules    = {}

        # ----- Classes and Functions contain the documented items
        # built from the modules or added manually

        self.classes    = {}
        self.functions  = {}

    # ====================================================================================================
    # Modules : source

    # ----------------------------------------------------------------------------------------------------
    # Add a module

    def add_module(self, name, text):

        self.modules[name] = Module(name, text)

    # ----------------------------------------------------------------------------------------------------
    # Read the modules from files

    @classmethod
    def FomFiles(cls, name, folder, sub_folders=[], doc_folder='doc'):

        proj = cls(name, Path(folder) / doc_folder)

        root_folder = Path(folder)
        all_folders = ["."] + sub_folders

        for subf in all_folders:
            if subf == '.':
                path = root_folder
            else:
                path = root_folder / subf
            for fpath in path.iterdir():
                if not fpath.match("*.py"):
                    continue
                print("Parse", fpath)
                proj.add_module(subf, fpath.read_text())

        return proj

    # ----------------------------------------------------------------------------------------------------
    # Get a class from a module

    def get_module_class(self, class_name, module_name=None, halt=True):

        class_ = None
        if module_name is None:
            for m in self.modules:
                fc = m.classes.get(class_name)
                if fc is not None:
                    class_ = fc
                    break
        else:
            class_ = self.modules[module_name].get(class_name)

        if class_ is None and halt:
            raise Exception(f"Class '{class_name}' not found in {list(self.modules.keys())}")

        return class_

    # ====================================================================================================
    # Build the structure

    def add_class(self, class_name, module_name=None, bases=[], capture=[]):

        if self.classes.get(class_name) is not None:
            raise Exception(f"Add class error: {class_name} already exists")

        from_class = self.get_module_class(class_name, module_name=module_name)

        # ----- Create the class from the module

        class_ = Class(class_name, from_class.comment).capture_class(from_class)

        # ----- Set the inheritance

        for cname in bases:
            class_.bases.append(cname)
        class_.bases = list(set(class_.bases))

        # ----- Capture transparent root classes

        for cname in capture:
            class_.capture(self.get_module_class(cname))

        # ----- Register the class to comment

        self.classes[class_name] = class_

        return class_






# =============================================================================================================================
# Tests

class Foo:
    def __init__(self, foo_name, comment="Comment string"):
        """ Foo class

        Foo dummy class

        Arguments
        ---------
        - foo_name (str) : Foo name
        - comment : The comment string
        """
    @property
    def foo_prop1(self):
        """ Foo prop 1
        """
        pass

    @property
    def foo_prop2(self):
        """ Foo prop 2
        """
        pass

    @foo_prop2.setter
    def foo_prop2(self, value):
        """ Foo prop 2
        """
        pass

    @staticmethod
    def foo_static():
        """ Foo static method
        """
        pass

    @classmethod
    def foo_class(cls):
        """ Foo class method
        """
        pass

    @classmethod
    @property
    def foo_class(cls):
        """ Foo class property
        """
        pass

    def foo_method(self, name, name_str, name_str_comm, name_def="Default name", name_def_comm="Default name", **kwargs):
        """ Foo method

        Arguments
        ---------
        - name
        - name_str (str)
        - name_str_comm (str) : The comment on name str
        - name_def (str="Default name")
        - name_def_comm (str="Default name") : The comment on name str default
        - **kwargs : comment on kwargs

        Returns
        -------
        - float : comment on the returned type
        """

    def overriden_method(self):
        """ Foo overriden method
        """

class Bar(Foo):

    def bar_method(self):
        """ Bar method
        """

    def overriden_method(self):
        """ Bar overriden method
        """


def tests():

    root = Path(__file__)

    proj = ProjectDocumentation.FomFiles('Test', folder=root.parents[0], sub_folders=[], doc_folder='doc')

    return


    docs = Parser.FromFile(__file__).documentation()

    foo_class = Class.FromDoc(docs['Foo'])
    foo_class.print()

    bar_class = Class.FromDoc(docs['Bar'])
    bar_class.capture_class(foo_class)
    bar_class.print()