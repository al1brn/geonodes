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
    def __init__(self, title, comment=None, level=0, with_sections_only=False, sort_sections=False):
        """ Elementary base of a documentation

        A **Section** is basically a title and a comment.

        It inherits from a list into which sub sections can be stored.
        A Section produces documentation:
        - Header
        - Comment
        - Loop on sub sections

        Arguments
        ---------
        - title (str) : section title
        - comment (str = None) : header comment
        - level (int = 0) : indentation level
        - with_sections_only (bool=False) : ignore if there is no sub sections
        - sort_sections (bool = False) : sort the sub sections before writting them
        """

        super().__init__()

        # ----- Initialize the section

        self.title              = title
        self._comment           = None
        self.level              = level
        self.with_sections_only = with_sections_only
        self.sort_sections      = sort_sections

        # ----- Overridable init

        self.init()

        # ----- Comment after init is done

        self.comment = comment

    # ====================================================================================================
    # Specific init

    def init(self):
        pass

    # ====================================================================================================
    # Comment property

    @property
    def comment(self):
        """ Comment property

        Returns
        -------
        - str : Section header comment
        """
        return self._comment

    @comment.setter
    def comment(self, value):
        self._comment = self.parse_comment(value)

    # ====================================================================================================
    # Target file name

    def parse_comment(self, comment):
        """ Parse comment to extract information

        This method extract information embbeded in the comment and returns the cleaned text.
        The default implementation returns the argument without change.

        Arguments
        ---------
        - comment (str) : the raw comment

        Returns
        -------
        - str : the cleaned comment
        """
        return comment

    # ====================================================================================================
    # Target file name

    @property
    def md_file_name(self):
        """ MD Document file name

        Returns
        -------
        - str : markdown file name
        """
        return f"{self.title.lower().replace(' ', '_')}.md"

    # ====================================================================================================
    # Link to

    @property
    def link_token(self):
        """ MD link token

        The markdown token is the lower case title where spaces are replaces by '-' char

        Returns
        -------
        - str : markdown token
        """
        return self.title.lower().replace(' ', '-')

    def link_to(self, url=""):
        """ MD link

        Returns
        -------
        - str : [title](url + link_token)
        """
        if url != "":
            url += '#'
        return f"[{self.title}]({url}{self.link_token})"

    # ====================================================================================================
    # Get a section

    def get_section(self, title):
        """ Look for a sub section by its title

        Arguments
        ---------
        - title (str) : the section to look for

        Returns
        -------
        - Section if found, None otherwise
        """
        for section in self:
            if section.title == title:
                return section
        return None

    @property
    def sorted_sections(self):
        """ Sort the sub sections in alphabetical order

        Returns
        -------
        - List : list of the sub sections sorted in alphabetical order
        """
        return sorted(self, key=lambda s: s.title)

    def alphabetical_sections(self, alpha=None):
        """ Build a dictionary keyed by the section title initials

        Used to diplay a table of content when there is a great number of sections.

        ```
        {'A': ['a section', 'another section',
         'O': ['other section']
         }
        ```

        Arguments
        ---------
        - alpha (dict = None) : dictionary to feed

        Returns
        -------
        - dict of list of Sections
        """
        if alpha is None:
            alpha = {}

        for section in self:
            first = section.title[0].upper()
            sections = alpha.get(first)
            if sections is None:
                sections = Section(first)
                sections.sort_sections = True
                alpha[first] = sections
            sections.append(section)
        return alpha

    # ====================================================================================================
    # Yield the documentation

    def build_header(self):
        """ Yield the lines of the header part
        """
        yield '#'*(self.level + 1) + ' ' + self.title + '\n\n'
        if self.comment is not None:
            yield self.comment + '\n\n'

    def build_sections(self):
        """ Yield the lines of the sections parts
        """
        sections = self.sorted_sections if self.sort_sections else self
        for section in sections:
            for line in section.build():
                yield line

    def build(self):
        """ Yield the lines of the section

        The method yields the lines from method **build_header** and the from
        **build_sections**.

        If the flag **with_sections_only** is set, nothing is yield if there is no
        sub sections.

        Returns
        -------
        - str : documentation lines for the sections
        """
        if self.with_sections_only and len(self) == 0:
            return

        for line in self.build_header():
            yield line

        for line in self.build_sections():
            yield line

        yield "\n"

    # ====================================================================================================
    # Debug

    def print(self):
        """ Print the documentation in the console

        For debug purpose.
        """
        print("-"*100)
        for line in self.build():
            print(line, end='')
        print()

# =============================================================================================================================
# Argument

class Argument(Section):
    def __init__(self, name, type=None, default=None, description=None):
        """ Function argument

        Yield a line for argument documentation:
        ```
        - name (type = default) : description
        ```

        Arguments
        ---------
        - name (str) : argument name
        - type (str = None) : type name
        - default (str = None) : default value
        - description (str = None) : description
        """
        super().__init__(name, comment=description)
        self.type = type
        self.default = default

    def build(self):
        yield f"- **{self.title}**"
        if self.type is None:
            if self.default is not None:
                yield f" (= {self.default})"
        else:
            yield f" (_{self.type}_"
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
        """ Function returns

        Yield a line for return documentation:
        ```
        - name  : description
        ```

        Arguments
        ---------
        - name (str) : return type
        - description (str = None) : description
        """
        super().__init__(name, comment=description)

    def build(self):
        yield f"- _{self.title}_"
        if self.comment is None:
            yield '\n'
        else:
            yield f" : {self.comment}\n"

# =============================================================================================================================
# Function section

class Function(Section):
    def __init__(self, name, comment=None, level=1):
        """ Section dedicated to function documentation.

        A **Function** is made of two sections:
        - Properties
        - Methods

        The comment can contain description of Arguments and Returns.
        The comment is parsed in order to extract this information and to
        write the document is a homogeneous way.

        Arguments
        ---------
        - name (str) : function or method name
        - comment (str = None) : header comment
        - level (int = 1) : indentation level
        """
        super().__init__(name, level=level)

        self.comment = comment

    # ====================================================================================================
    # Specific init

    def init(self):
        """ Function section specific init

        A Function section is made of two sections:
        - Arguments
        - Returns

        It also create stores other information:
        - decorators
        - arguments
        """

        # Arguments and Returns sections

        self.append(Section("Arguments", level=4, with_sections_only=True))
        self.append(Section("Returns",   level=4, with_sections_only=True))

        # Function information

        self.is_static = False
        self.is_class  = False
        self.is_getter = False
        self.is_setter = False
        self.args      = None

    # ====================================================================================================
    # Parse the comment

    def parse_comment(self, comment):
        """ Function comment parser

        The Function parser extracts Arguments and Returns sections.
        The corresponding lines are remove from the comment to feed the two sections.

        The lists are generated from the structure

        Arguments
        ---------
        """
        if comment is None:
            return None

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
                        self.returns.append(Return(name = line[2:]))
                    else:
                        self.returns.append(Return(match.group(1), match.group(3)))

        return new_comment

    # ====================================================================================================
    # Arguments and Returns sections

    @property
    def arguments(self):
        return self.get_section('Arguments')

    @property
    def returns(self):
        return self.get_section('Returns')

    # ====================================================================================================
    # Initialize from a Doc class coming from pyparse

    @classmethod
    def FromDoc(cls, doc, class_name=None):
        """ Create a class from an instance of Doc

        Doc is a class read by the **Parser**.

        Arguments
        ---------
        - doc (Doc) : Doc parsed by **Parser**
        """

        # ----------------------------------------------------------------------------------------------------
        # Create additional comment

        decos = []
        is_static = False
        is_class  = False
        is_setter = False
        is_getter = False
        for deco in doc.decorators:
            if deco == '@classmethod':
                decos.append('Class method')
                is_class = True
            elif deco == '@staticmethod':
                decos.append('Static method')
                is_static = True
            elif deco == '@property':
                is_getter = True
            elif deco.find('.setter')> 0:
                is_setter = True

        before = ""
        if len(decos):
            before = "> **Decorators**: " + ", ".join(decos) + '\n\n'

        if len(doc.args):
            if class_name is None:
                fname = doc.name
            elif doc.name == '__init__':
                fname = class_name
            else:
                fname = f"{class_name}.{doc.name}"

            if is_setter or is_getter:
                before += f"``` python\n{fname}\n```\n\n"""
            else:
                before += f"``` python\n{fname}{doc.args}\n```\n\n"

        # ----------------------------------------------------------------------------------------------------
        # Add before the comment argument

        if before == "":
            before = None

        if doc.comment is None:
            comment = before
        elif before is None:
            comment = doc.comment
        else:
            comment = before + '\n\n' + doc.comment

        # ----------------------------------------------------------------------------------------------------
        # Create the Function instance

        inst = cls(doc.name, comment)

        # Complementary information

        inst.args = doc.args

        inst.is_class  = is_class
        inst.is_static = is_static
        inst.is_setter = is_setter
        inst.is_getter = is_getter

        return inst

# =============================================================================================================================
# Class documentation

class Class(Section):

    def __init__(self, class_name, comment):
        super().__init__(class_name, comment)

        self.append(Section('Properties', with_sections_only=True, sort_sections=True))
        self.append(Section('Methods',    with_sections_only=True, sort_sections=True))

        self.bases = []

    @classmethod
    def FromDoc(cls, doc):
        inst = cls(doc.name, doc.comment)

        inst.bases.extend(doc.bases)

        for d in doc.funcs.values():
            inst.methods.append(Function.FromDoc(d, class_name=doc.name))

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

    def build(self):

        # ----------------------------------------------------------------------------------------------------
        # __init__ comment as class comment

        init = self.methods.get_section('__init__')
        if init is not None:
            if self.comment is None:
                self.comment = init.comment
            else:
                self.comment += '\n\n' + init.comment
            self.methods.remove(init)

        # ----------------------------------------------------------------------------------------------------
        # Property methods as properties

        for func in self.methods:
            if func.is_setter or func.is_getter:
                prop = self.properties.get_section(func.title)
                if prop is None:
                    self.properties.append(func)
                else:
                    if prop.comment is None:
                        prop.comment = func.comment
                    elif func.comment is not None:
                        prop.comment += func.comment
                self.methods.remove(func)

        # ----------------------------------------------------------------------------------------------------
        # Header lines

        for line in self.build_header():
            yield line

        # ----------------------------------------------------------------------------------------------------
        # Inheritance

        if len(self.bases):
            yield f"\n> inherits from: "
            for name in self.bases:
                yield f"[{name}](.{name.lower()}.md) "
            yield '\n\n'

        # ----------------------------------------------------------------------------------------------------
        # Methods table of content

        if len(self.methods) or len(self.properies):
            yield "## Methods and Properties\n"

            alpha = self.methods.alphabetical_sections(self.properties.alphabetical_sections())

            for letter in sorted(alpha.keys()):
                methods = sorted(alpha[letter], key=lambda s: s.title)
                yield f"- {letter} : "
                for s in methods:
                    yield f"[{s.title}](#{s.link_token}) "
                yield '\n'
            yield '\n'

        # ----------------------------------------------------------------------------------------------------
        # Properties and methods

        for line in self.properties.build():
            yield line

        for line in self.methods.build():
            yield line


# =============================================================================================================================
# Classes documentation

class Classes(Section):

    def __init__(self, class_name, comment):
        super().__init__(class_name, comment, sort_sections=True)

    def build_sections(self):
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

        for doc in self.docs.values():
            if doc.is_class:
                self.classes[doc.name] = Class.FromDoc(doc)
            else:
                self.functions[doc.name] = Function.FromDoc(doc)

# =============================================================================================================================
# Project documentation

class ProjectDocumentation:

    def __init__(self, name):

        self.name       = name

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
    def FromFiles(cls, name, folder, sub_folders=[]):

        proj = cls(name)

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
                proj.add_module(subf + '_' + fpath.name, fpath.read_text())

        return proj

    # ----------------------------------------------------------------------------------------------------
    # Get a class from a module

    def get_module_class(self, class_name, module_name=None, halt=True):

        class_ = None
        if module_name is None:
            for m in self.modules.values():
                fc = m.classes.get(class_name)
                if fc is not None:
                    class_ = fc
                    break
        else:
            class_ = self.modules[module_name].get(class_name)

        if class_ is None and halt:
            raise Exception(f"Class '{class_name}' not found in modules {list(self.modules.keys())}")

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
            class_.capture_class(self.get_module_class(cname))

        # ----- Register the class to comment

        self.classes[class_name] = class_

        return class_

    # ====================================================================================================
    # Write the documentation

    def write_documentation(self, doc_folder):

        doc_folder = Path(doc_folder)

        for class_name, class_ in self.classes.items():
            file_path = doc_folder / class_.md_file_name
            print(f"Write ‘{class_name}' : {file_path}")
            with file_path.open(mode='w') as f:
                for line in class_.build():
                    f.write(line)



# =============================================================================================================================
# Test on the current folder

def tests():

    # ====================================================================================================
    # Step 1 : read project files from root folder

    root = Path(__file__).parents[0]
    proj = ProjectDocumentation.FromFiles('Test', folder=root, sub_folders=[])

    # ====================================================================================================
    # Step 2 : build document hierarchy

    proj.add_class('Section')
    proj.add_class('Argument', bases=['Section'])
    proj.add_class('Return',   bases=['Section'])
    proj.add_class('Function', bases=['Section'])
    proj.add_class('Class',    bases=['Section'])
    proj.add_class('Classes',  bases=['Section'])
    proj.add_class('Module')
    proj.add_class('ProjectDocumentation')


    # ====================================================================================================
    # Step 3 : write the documentation

    proj.write_documentation(doc_folder=root / 'doc')






    return


    docs = Parser.FromFile(__file__).documentation()

    foo_class = Class.FromDoc(docs['Foo'])
    foo_class.print()

    bar_class = Class.FromDoc(docs['Bar'])
    bar_class.capture_class(foo_class)
    bar_class.print()
