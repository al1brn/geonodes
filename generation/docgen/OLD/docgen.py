""" Markdown python documentation generator

Generate documentation for python project based on the source file.
"""

import re
from pprint import pprint
from pathlib import Path
import inspect

from parser import del_margin, parse_module, parse_files














# =============================================================================================================================
# Manages the documentation of a project
#
# Documentation is organized as a hierarchy of files
#
# Documentation comes from:
# - automatic building from files
# - manual adds

def title_to_file_name(title):
    return f"{title.lower().replace(' ', '_')}.md"

def title_to_token(title):
    return title.lower().replace(' ', '-')

# =============================================================================================================================
# Parse comment to extract information

def parse_comment(comment):
    """ Function comment parser

    The Function parser extracts Properties, Arguments and Returns sections.
    The corresponding lines are removed to build the 'new_comment' text.

    The lists are generated from the structure

    Arguments
    ---------
    - comment (str) : the raw comment

    Returns
    -------
    - dict : {'new_comment', 'properties', 'arguments', 'returns', 'raises'}
    """

    if comment is None:
        return {'new_comment': None}

    list_expr = r"^(\w*) ?\n-+ ?\n(([^\w\n]+.*\n)*)"

    for m in re.finditer(list_expr, comment + '\n\n', flags=re.MULTILINE):

        title = m.group(1).strip().lower()

        lines = []
        for line in m.group(2).split('\n'):
            if line.strip() == '':
                continue
            if line[0] == ' ':
                lines[-1] += ' ' + line.strip()
            else:
                lines.append(line.strip())


        if title in ['property', 'properties']:
            pass

        elif title in ['argument', 'arguments']:
            pass

        elif title in ['return', 'returns']:
            pass

        elif title in ['raise', 'raises']:
            pass

        print(title)
        print('-'*20)
        print("\n".join(lines))
        print('-'*20)

    return







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
        elif line[:10].lower() == 'properties':
            context = 'PROPERTIES'
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

            if context in ['ARGUMENTS', 'PROPERTIES']:
                target_section = self.arguments if context == 'ARGUMENTS' else self.props

                expr = r"-\s*(\w+)\s*(\((\w+)\s*(=\s*(.+))?\))?(\s*:\s*(.+))?"
                match = re.search(expr, line)

                if match is None:
                    target_section.append(Argument(name = line[2:]))
                else:
                    target_section.append(Argument(
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

comment = """ Test
some comment

Properties
----------
- Test
  continued
- Test2
mlqkjfqlm

Raises
------
- ljslfdkj
  skhfkjs


ttot
"""



parse_comment(comment)



# =============================================================================================================================
# Section

class Section(list):

    def __init__(self, title, comment=None, level=0, **kwargs):
        """ Elementary base of a documentation

        A **Section** is basically a title, a header section and sub sections

        It inherits from a list into which sub sections are stored.
        A Section produces documentation:
        - Header (level 0)
        - Header
        - Table of content section (level 1)
        - Loop on sub sections (level 1)
        - Extra (for intrapage links)

        Properties
        ----------
        - title (str) : Section title
        - with_sections_only (bool) : The section is printed only if
          the list of sub sections is not empty
        - sort_sections (bool) : The sections are placed in alphabetical order
        - extra (str) : Extra text at the end of the documentation
        - in_toc(bool) : section is included in the owner section table of content
        - toc (str) : name of the toc section, None if no toc is generated
        - fixed_level (bool) : level is fixed and can't be changed
        - page (<!Section>) : the page where this section will appear

        Arguments
        ---------
        - title (str) : section title
        - comment (str = None) : header comment
        - level (int = 0) : indentation level. If the value is negative, the absolute value
          is taken and the level is considered as fixed (see <!#fixed_level>)
        - with_sections_only (bool=False) : ignore if there is no sub sections
        - sort_sections (bool) : sort the sub sections before writting them
        """

        super().__init__()

        # ----- Initialize the section

        self.title              = title
        self._comment           = None
        self._level             = abs(level)
        self.fixed_level        = level < 0
        self.with_sections_only = False
        self.sort_sections      = False

        self.toc                = None
        self.in_toc             = True

        self.extra              = None
        self.docs               = None
        self.page               = None

        # ----- Overridable init
        # To create other attributes

        self.init()

        # ----- Set the keyword arguments

        for param, value in kwargs.items():
            if param not in self.__dict__:
                raise AttributeError(f"{type(self).__name__} init error: '{param}' attribute doesn't exist!")
            setattr(self, param, value)

        # ----- Comment after init is done

        self.comment = comment

    def __str__(self):
        scomm = 'None' if self.comment is None else self.comment[:10] + '...'
        return f"<Section {type(self).__name__} '{self.title}' {len(self)}: {scomm}>"

    # ====================================================================================================
    # Get the content from a source file

    @classmethod
    def FromSource(cls, name, text):
        """ Get the content from a source file.

        The source is parsed and a <!Section> is added for each class and global function.
        Arguments
        ---------
        - text (str) : source code to parse

        Returns
        -------
        - Section
        """

        section = Section(name)

        # ----- Parse the source code and keep a reference to it

        section.docs = Parser(text).documentation()

        # ----- Add a section per class / function

        for doc in section.docs.values():
            if doc.name == 'import':
                continue

            if doc.is_class:
                section.append(Class.FromDoc(doc))
            else:
                section.append(Function.FromDoc(doc))

        return section

    # ====================================================================================================
    # As a dict

    @property
    def as_dict(self):
        """ Return as a dictionary

        Returns
        -------
        - dict : section title: section
        """
        return {section.title: section for section in self}

    # ====================================================================================================
    # Specific init

    def init(self):
        """ Class initialisation

        This complementary initialisation takes place at the end of **__init__**, before
        [parse_comment](#parse_comment) is called.

        Allows to initialize attributes which are used in [parse_comment](#parse_comment) method.

        Default method is empty.
        """
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
    # Level property

    @property
    def level(self):
        """ Indentation level

        When set, the sub sections levels are set with the passed value plus 1.

        Returns
        -------
        - int
        """
        return self._level

    @level.setter
    def level(self, value):
        if self.fixed_level:
            return
        self._level = value
        for section in self:
            section.level = value + 1

    # ====================================================================================================
    # Iteration

    def iteration(self, f):
        """ Run the function on the section and sub sections

        The method halts on the first section for which the function
        return `True` and returns this section.
        If the function doesn't return `True`, the methods is run on all sections
        and return `None`.

        Arguments
        ---------
        - f (function of template f(section)) : the function to run

        Returns
        -------
        - Section or None
        """
        try:
            ok = f(self)
        except:
            return self

        if ok == True:
            return self

        for section in self:
            s = section.iteration(f)
            if s is not None:
                return s

        return None

    # ====================================================================================================
    # Compile

    def compile(self, project):
        pass

    # ====================================================================================================
    # Parse the comment

    def parse_comment(self, comment):
        """ Parse comment to extract information

        This method extract information embbeded in the comment and returns the cleaned text.
        The default implementation normalizes the markdwon comment.

        Arguments
        ---------
        - comment (str) : the raw comment

        Returns
        -------
        - str : the cleaned comment
        """
        return md_normalize(comment)

    # ====================================================================================================
    # Dynamic documentation

    def new_section(self, title, comment=None, sub_level=1):
        """ Add a sub section

        Arguments
        ---------
        - title (str) : section title
        - comment (str) : header comment
        - sub_level (int = 1) : level increment

        Returns
        -------
        - Section
        """

        section = Section(title, comment=comment, level=self.level + sub_level)
        self.append(section)

        # Reference to the top page
        section.page = self.page

        return section

    def write_header(self, comment='\n', parse=True):
        """ Append text to the header comment

        Arguments
        ---------
        - comment (str) : the text to write
        - parse (bool = True) : parse the comment
        """

        if parse:
            comment = self.parse_comment(comment)

        if self._comment is None:
            self._comment = comment
        else:
            self._comment += comment

    def write(self, comment='\n', parse=True):
        """ Append text to the current text

        The current text is either the comment if this section if there is not sub sections,
        or the comment of the last sub sections.

        Arguments
        ---------
        - comment (str) : the text to write
        - parse (bool = True) : parse the comment
        """

        if len(self):
            self[-1].write(comment, parse=parse)

        else:
            if parse:
                comment = self.parse_comment(comment)

            if self._comment is None:
                self._comment = comment
            else:
                self._comment += comment

    def write_source(self, source):
        self.write("``` python\n", parse=False)
        self.write(source.replace("`", "'"), parse=False)
        self.write("```\n\n", parse=False)

    # ====================================================================================================
    # Properties

    @property
    def md_file_name(self):
        """ MD Document file name

        Returns
        -------
        - str : markdown file name
        """
        return title_to_file_name(self.title)
        #return f"{self.title.lower().replace(' ', '_')}.md"

    @property
    def link_token(self):
        """ MD link token

        The markdown token is the lower case title where spaces are replaces by '-' char

        Returns
        -------
        - str : markdown token
        """
        return title_to_token(self.title)
        #return self.title.lower().replace(' ', '-')

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

        > [!NOTE]
        > This function searches only in the direct children, not in the whole tree.

        To search a section in the whole tree, use <!#iteration> method:

        ``` python
        sub_section = parent_section.iteration(lambda s: s.title == 'The title')
        ```

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

    def build_toc(self):
        if self.toc is None:
            return

        yield f"{'#'*(self.level + 1)} {self.toc}\n\n"
        for section in self.sorted_sections:
            if section.in_toc:
                yield f"- [{section.title}](#{section.link_token})\n"
        yield '\n'

    def build_sections(self):
        """ Yield the lines of the sections parts
        """
        sections = self.sorted_sections if self.sort_sections else self
        for section in sections:
            for line in section.build():
                yield line

    def build_extra(self):
        """ Yield extra lines at the end of the section documentation
        """
        if self.extra is None:
            return
        else:
            yield '\n' + self.extra

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

        for line in self.build_toc():
            yield line

        for line in self.build_sections():
            yield line

        for line in self.build_extra():
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
        """ Yield line argument

        Returns
        -------
        - str : formatted argument line
        """
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
        """ Yield line return

        Returns
        -------
        - str : formatted return line
        """
        yield f"- _{self.title}_"
        if self.comment is None:
            yield '\n'
        else:
            yield f" : {self.comment}\n"

# =============================================================================================================================
# Function section

class Function(Section):
    """ Section dedicated to function documentation.

    The comment can contain description of Arguments and Returns.
    The comment is parsed in order to extract this information and to
    write the document is a homogeneous way.

    Arguments
    ---------
    - name (str) : function or method name
    - comment (str = None) : header comment
    - level (int = 1) : indentation level
    """

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

        self.append(Section("Arguments",  level=4, with_sections_only=True))
        self.append(Section("Returns",    level=4, with_sections_only=True))

        # Properties can be documented in the __init__comment
        self.props = Section("Properties")

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

        The Function parser extracts Properties, Arguments and Returns sections.
        The corresponding lines are remove from the comment to feed the two sections.

        The lists are generated from the structure

        Arguments
        ---------
        """
        if comment is None:
            return None

        comment = super().parse_comment(comment)

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
            elif line[:10].lower() == 'properties':
                context = 'PROPERTIES'
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

                if context in ['ARGUMENTS', 'PROPERTIES']:
                    target_section = self.arguments if context == 'ARGUMENTS' else self.props

                    expr = r"-\s*(\w+)\s*(\((\w+)\s*(=\s*(.+))?\))?(\s*:\s*(.+))?"
                    match = re.search(expr, line)

                    if match is None:
                        target_section.append(Argument(name = line[2:]))
                    else:
                        target_section.append(Argument(
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
        """ Arguments Section

        Returns
        -------
        - Section : title is 'Arguments', sub sections are [Argument](#argument)
        """
        return self.get_section('Arguments')

    @property
    def returns(self):
        """ Arguments Section

        Returns
        -------
        - Section : title is 'Arguments', sub sections are [Return](#return)
        """
        return self.get_section('Returns')

    # ====================================================================================================
    # Initialize from a Doc class coming from pyparse

    @classmethod
    def FromDoc(cls, doc, class_name=None, **kwargs):
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

        inst = cls(doc.name, comment, **kwargs)

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
    """ Section documenting a class

    The structure of the document is:
    - title (class name)
    - header comment
    - properties & methods table of contents
    - Properties section with the documented properties as sub sections
    - Methods section withe the documented methods as sub sections

    The class documentation is completed afterward by the [compile](#compile) method
    which get the links coming from inheritance between classes.

    Properties
    ----------
    - bases (list of str) : name of the base classes
    - subclasses (list of str) : name of the sub classes
    - inherited (list of str) : properties and methods inherited from base classes

    Arguments
    ---------
    - class_name (str) : class name
    - comment (str) : header comment
    """

    def init(self):

        self.append(Section('Properties', with_sections_only=True, sort_sections=True))
        self.append(Section('Methods',    with_sections_only=True, sort_sections=True))

        self.bases      = []
        self.subclasses = []
        self.inherited  = []

    @classmethod
    def FromDoc(cls, doc, ignore_uncommented=True, **kwargs):
        """ Creates a Class document from a Doc parsed from source file

        The **doc** argument contains the list of documents methods and properties.

        Arguments
        ---------
        - doc (Doc) : Doc parsed from a sourc file
        - exclude_uncommented (bool = True) : exclude the methods which are not commented
          in the source file

        Returns
        -------
        - Class : document on the class
        """
        inst = cls(doc.name, doc.comment, **kwargs)

        inst.bases.extend(doc.bases)

        for d in doc.funcs.values():
            if not(d.comment is None and ignore_uncommented):
                inst.methods.append(Function.FromDoc(d, class_name=doc.name, level=1))

        return inst

    @property
    def properties(self):
        """ Properties Section

        Returns
        -------
        - Section : title is 'Properties', sub sections are documented properties
        """
        return self.get_section('Properties')

    @property
    def methods(self):
        """ Methods Section

        Returns
        -------
        - Section : title is 'Methods', sub sections are documented methods
        """
        return self.get_section('Methods')

    # ====================================================================================================
    # Compile

    def compile(self, project):
        """ Compile the class

        **project** refers to the global <!Project> documentation.

        Class compilation is:
        - Load each class based on this one into to the **subclasses** attribute.
        - Load the methods and properties inherited from parent classes

        Arguments
        ---------
        - project (<!Project>) : main project

        Returns
        -------
        - self
        """

        # ----------------------------------------------------------------------------------------------------
        # Inheritance

        inherited = {}

        #classes = project.objects

        for class_ in project.objects.values():

            if not isinstance(class_, Class):
                continue

            # ----- Sub classes

            if self.title in class_.bases:
                self.subclasses.append(class_.title)

            # ----- Inherited properties and methods

            if class_.title in self.bases:
                for prop in class_.properties:
                    if self.properties.get_section(prop.title) is None:
                        inherited[prop.title] = f"<!{class_.title}#{prop.title}>"

                for meth in class_.methods:
                    if self.methods.get_section(meth.title) is None:
                        inherited[meth.title] = f"<!{class_.title}#{meth.title}>"

        if len(inherited):
            self.inherited = [inherited[key] for key in sorted(inherited.keys())]

        # ----------------------------------------------------------------------------------------------------
        # Properties documented in the comment section
        #
        # Comment parsing may have created properties doc in 'props' section of some functions
        # (normally in __init__.comment)

        for meth in self.methods:
            for prop in meth.props:
                if self.properties.get_section(prop.title) is None:
                    if prop.comment is None:
                        comment = "Property\n\n"
                    else:
                        comment = prop.comment + '\n\n'
                    comment += f"Returns\n- {prop.type}\n"
                    self.properties.append(Function(prop.title, comment))

        # ====================================================================================================
        # Add to the header comment

        sepa = None
        if len(self.bases):
            self.write_header(f"\n> inherits from: ", parse=False)
            for name in self.bases:
                self.write_header(f"[{name}]({name.lower()}.md) ", parse=False)
            self.write_header('\n', parse=False)
            sepa = '\n'

        if len(self.inherited):
            self.write_header("\n> inherited: " + ", ".join(self.inherited), parse=False)
            sepa = '\n'

        if len(self.subclasses):
            self.write_header(f"\n> subclasses: ", parse=False)
            for name in self.subclasses:
                self.write_header(f"[{name}]({name.lower()}.md) ", parse=False)
            self.write_header('\n', parse=False)
            sepa = '\n'

        if sepa is not None:
            self.write_header(sepa, parse=False)

        # ----------------------------------------------------------------------------------------------------
        # Methods table of content

        if len(self.methods) or len(self.properties):
            section = self.new_section("Methods and Properties")

            alpha = self.methods.alphabetical_sections(self.properties.alphabetical_sections())

            for letter in sorted(alpha.keys()):
                methods = sorted(alpha[letter], key=lambda s: s.title)
                section.write(f"- {letter} : ", parse=False)
                for s in methods:
                    section.write(f"[{s.title}](#{s.link_token}) ", parse=False)
                section.write('\n', parse=False)
            section.write('\n', parse=False)

        # ----------------------------------------------------------------------------------------------------
        # Extra

        for section in self.properties:
            section.extra = f"\n<sub>[top](#{self.link_token}) [index](index.md)</sub>"

        for section in self.methods:
            section.extra = f"\n<sub>[top](#{self.link_token}) [index](index.md)</sub>"

    # ====================================================================================================
    # Capture methods and properties from another class

    def capture_class(self, other, with_comment=False):
        """ Capture methods and properties from another Class

        This method allows to get the documentation of inherited items of a class
        which is not documentated.

        Arguments
        ---------
        - other (Class) : class to copy methods and properties from

        Returns
        -------
        - self
        """

        if self._comment is None and with_comment:
            self._comment = other._comment

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
        """ Yield the Class documentation lines
        """

        # ----------------------------------------------------------------------------------------------------
        # __init__ comment as class comment

        init = self.methods.get_section('__init__')
        if init is not None:
            if self.comment is None:
                self._comment = init.comment
            else:
                self._comment += '\n\n' + init.comment
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
        # Inheritance / sub classes

        if False:
            sepa = None
            if len(self.bases):
                yield f"\n> inherits from: "
                for name in self.bases:
                    yield f"[{name}]({name.lower()}.md) "
                yield '\n'
                sepa = '\n'

            if len(self.inherited):
                yield "\n> inherited: " + ", ".join(self.inherited)
                sepa = '\n'

            if len(self.subclasses):
                yield f"\n> subclasses: "
                for name in self.subclasses:
                    yield f"[{name}]({name.lower()}.md) "
                yield '\n'
                sepa = '\n'

            if sepa is not None:
                yield sepa

        # ----------------------------------------------------------------------------------------------------
        # Methods table of content

        if False:
            if len(self.methods) or len(self.properties):
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
# Project documentation

class Project(Section):

    def __init__(self, title, comment=None, toc='Content'):
        """ Project documentation

        Project documentation allows to build a full project documentation
        from parsing source code, loading complementary documentation file and also
        by dynamically adding documentation.

        The final documentation is written ad **MarkDown** files with **index.md** as main
        entrance for the documentation.

        > [!IMPORTANT]
        > All files are written in the same folder. The page titles must be unique in order
        > to avoid overwritting content.

        The document is built by:
        - creating pages and writing content into it
        - creating pages from parsed source code

        The parsed source code is stored in <!#refdoc> dictionary with one entry per parsed file.
        The parsed source contain classes and function documentation which can be transfered
        into pages.

        When transferring, a class can be enriched with other classed, either to specify
        inherited methods and properties or to complement the documentation with inheritance.
        See <!#add_class>.

        The following example is pseudo code for documentation building.

        ``` python
        # Create the project
        proj = Project(...)

        # Parse source files to feed proj.refdoc dict
        proj.load_files(...)

        # Create pages from reference documentation
        proj.add_class(...)

        # Add 'manual' pages
        page proj.new_page("Tutorial")
        page.write(...)

        # Create the documentation
        proj.create_documentation(...)
        ```

        Properties
        ----------
        - refdocs (dict of <!Section>) : reference documentation loaded from source file
        - pages (dict of <!Section>) : the pages to create in the final documentation
        - sections (list of <!Section>) : dictionary of documented items

        Arguments
        ---------
        - title (str) : project name
        - comment (str) : header comment
        - toc (str = 'Content') : name of the table of content section, None if
          this section is not required
        """

        super().__init__(title, comment, toc=toc)
        self.hooks = []

        # LAYER 1
        # Reference documentation: typically the result of parsing source files

        self.refdoc = {}

        # LAYER 2
        # Final pages: one file is written per page

        self.pages    = {}

        # Documented Objects

        self.objects = {}

    def object_link(self, name, token=None):

        # Token only

        if name is None or name == "":
            if token is None or token == "":
                return ""
            else:
                return f"[{token}](#{title_to_token(name)})"

        # The page where the object will appear

        obj = self.objects.get(name)
        if obj is None:
            # Let's try a page
            obj = self.pages.get(name)
            if obj is None:
                print(f"CAUTION: impossible to link toward '{name}'. This object is not referenced.")
                return f"[LINK ERROR to '{name}'](index.md)"

        # Link with token or not

        if obj.page is None or obj.page.title == name:
            if token is None or token == "":
                return f"[{name}]({title_to_file_name(name)})"
            else:
                return f"[{token}]({title_to_file_name(name)}#{title_to_token(token)})"

        else:
            return f"[{name}]({title_to_file_name(obj.page.title)}#{title_to_token(name)})"


    # ====================================================================================================
    # ====================================================================================================
    # LAYER 1: Reference documentation management
    # ====================================================================================================
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Add a source file

    def add_source(self, key, text):
        """ Add a source code.

        The source code is parsed and the resulting <!Section> is stored in the <!#refdoc> dict.

        Arguments
        ---------
        - key (str) : source file key
        - text (str) : the source code

        Returns
        -------
        - Section
        """

        if key in self.refdoc:
            raise Exception(f"Impossible to add the source keyed by '{key}': key already exists in {list(self.refdoc.keys())}")

        self.refdoc[key] = Section.FromSource(key, text)

        return self.refdoc[key]

    # ----------------------------------------------------------------------------------------------------
    # Load source files from a folder

    def load_files(self, folder=None, sub_folders=[], key=None):
        """ Enrich the reference doc by parsing source files.

        All the files with `.py` extension are parsed.

        Arguments
        ---------
        - folder (str) : main folder
        - sub_folders (str) : sub folders to explore
        - key (str=None) :

        Returns
        -------
        - self
        """

        if key is None:
            key = Path(folder).stem

        root_folder = Path(folder)
        all_folders = ["."] + sub_folders

        for subf in all_folders:
            if subf == '.':
                path = root_folder
                file_key = key
            else:
                path = root_folder / subf
                file_key = str(Path(key) / subf)

            for fpath in path.iterdir():
                if not fpath.match("*.py"):
                    continue
                print("Parse", fpath)
                self.add_source(str(Path(file_key) / fpath.stem), fpath.read_text())

        return self

    # ----------------------------------------------------------------------------------------------------
    # Get a reference doc

    def get_refdoc(self, name, key=None, exact=True, halt=True):
        """ Get a reference documentation from the base

        If **key** argument is None, the **name** is searched in the whole dictionary,
        otherwise the search is performed only in the specified key.

        If **exact** is False, name is considered as a regular expression.
        All the title matching this expression is returned in a list.

        Arguments
        ---------
        - name (str) : title of the reference documentation
        - key (str = None) : source file key
        - exact (bool = True) : use exact name if True, regular expression otherwise
        - halt (bool = True) : raise an exception if not found

        Returns
        -------
        - <!Section> or list : found section if exact is True, list of sections otherwise
        """

        # ----------------------------------------------------------------------------------------------------
        # Get the resources to explore

        if key is None:
            refs = list(self.refdoc.values())
        else:
            refs = [self.refdoc[key]]

        # ----------------------------------------------------------------------------------------------------
        # Exact search

        class_ = None
        if exact:
            for ref in refs:
                section = ref.get_section(name)
                if section is not None:
                    class_ = section
                    break

        # ----------------------------------------------------------------------------------------------------
        # Regular expression

        else:
            class_ = []
            for ref in refs:
                for section in ref:
                    try:
                        if re.search(name, section.title) is not None:
                            class_.append(section)
                    except Exception as e:
                        print(f"Wrong regular expression '{name}'")
                        raise e


        if False: # OLD
            class_ = None
            if key is None:
                for source_section in self.refdoc.values():
                    section = source_section.get_section(name)
                    if section is not None:
                        class_ = section
                        break
            else:
                source = self.refdoc.get(key)
                if source is None:
                    raise Exception(f"RefDoc file key '{key}' doesn't exists in files {list(self.refdoc.keys())}")
                class_ = source.get(name)

        if class_ is None and halt:
            raise Exception(f"Reference doc named '{name}' not found in files {list(self.refdoc.keys())}")

        return class_

    # ----------------------------------------------------------------------------------------------------
    # Ref doc content

    @property
    def refdoc_content(self):
        return {key: [s.title for s in section] for key, section in self.refdoc.items()}

    # ====================================================================================================
    # ====================================================================================================
    # LAYER 2: Pages management
    # ====================================================================================================
    # ====================================================================================================    #

    # ----------------------------------------------------------------------------------------------------
    # Add a page

    def add_page(self, page):
        """ Add a page in the documentation

        Arguments
        ---------
        - page (<!Section>) : the page to add

        Returns
        -------
        - <!Section> : the argument **page**
        """
        if page.title in self.pages.keys():
            print("Existing pages:", list(self.pages.keys()))
            raise Exception(f"Project error when adding section '{page.title}' : the page key '{page.title}' already exists!")

        self.pages[page.title] = page

        # Auto reference, no fear !
        page.page = page

        return page

    # ----------------------------------------------------------------------------------------------------
    # Create a new page

    def new_page(self, title, comment=None, toc=None, in_toc=True):
        """ Add a page in the documentation

        > [!CAUTION]
        > **title** argument is used a as key in <!#pages> dictionary. It must be unique
        > in the scope of the project

        Arguments
        ---------
        - title (str) : page title
        - comment (str) : comment
        - toc (str = None) : title of the content section, None if no content section is required
        - in_toc (bool = True) : include the the documentation table of content

        Returns
        -------
        - <!Page>
        """
        page = Section(title, comment)

        page.toc = toc
        page.in_toc = in_toc

        return self.add_page(page)

    # ----------------------------------------------------------------------------------------------------
    # Section in pages

    def add_section_to_page(self, section, page, sub_level=0):

        if page is None:
            return self.add_page(section)

        else:
            if isinstance(page, str):
                target = self.pages[target_page]
            else:
                target = page

            target.append(section)
            section.page = page.page
            section.level = page.level + sub_level

            return section

    # ----------------------------------------------------------------------------------------------------
    # Add documentation for a class

    def add_class(self, class_name, page=None, bases=[], capture=[], file_key=None):
        """ Copy class documentation from reference documentation to pages

        The class must exist in one of the reference documentation <!#refdoc>.

        The class documentation is completed with **bases** and **capture** arguments.

        > Explicit inheritance with **bases**
        > _class_name_ : inherits from base_class
        > inherited methods : **method1**, **method2**

        > Hidden inheritance with **capture**
        > _class_name_
        > methods : **method1**, **method2**

        Once completed, the class is registered in <!#objects> and placed in the page.

        if **page** is None, the resulting <!Class> is considered as a page and
        added to <!#pages>. If **page** is not None, the class documentation
        is appended to it.

        > [!NOTE]
        > The page where the class is documented can be retreived with attribute <!Section#page>.

        Arguments
        ---------
        - class_name (str) : class name
        - page (<!Section> or str = None) : name of the page where to include the class documentation
        - bases (list of strs = []) : list of base classes
        - capture (list of strs or <!Class> = []) : list of classes to copy methods and properties from
        - file_key (str = None) : file key in <!#files>

        Returns
        -------
        - <!Class> : created class
        """

        # ---------------------------------------------------------------------------
        # A list of names

        if isinstance(class_name, (tuple, list)):
            for cname in class_name:
                self.add_class(cname, page=page, bases=bases, capture=capture, file_key=file_key)
            return None

        # ---------------------------------------------------------------------------
        # Let's create a properly documented class

        from_class = self.get_refdoc(class_name, key=file_key, halt=True)
        assert(isinstance(from_class, Class))

        # ----- Create the class from the module

        class_ = Class(class_name).capture_class(from_class, with_comment=True)

        # ----- Set the inheritance

        for cname in bases:
            class_.bases.append(cname)
        class_.bases = list(set(class_.bases))

        # ----- Capture transparent root classes

        for cname in capture:
            if isinstance(cname, str):
                from_class = self.get_refdoc(cname)
            else:
                from_class = cname
            class_.capture_class(from_class)

        # ---------------------------------------------------------------------------
        # We register and place it in a page

        self.objects[class_.title] = class_

        return self.add_section_to_page(class_, page)

    # ----------------------------------------------------------------------------------------------------
    # Add documentation for a function

    def add_function(self, function_name, page=None, file_key=None, function_key=None,
        exact=True, only_commented=True, sub_level=1):
        """ Copy function documentation reference documentation to pages.

        The function must exist in one of the reference documentation <!#refdoc>.

        Once completed, the function is registered in <!#objects> and placed in the page.

        if **page** is None, the resulting <!Function> is considered as a page and
        added to <!#pages>. If **page** is not None, the class documentation
        is appended to it.

        > [!NOTE]
        > The page where the class is documented can be retrieved with attribute <!Section#page>.

        Arguments
        ---------
        - function_name (str) : class name
        - page (<!Section> or str = None) : name of the page where to include the class documentation
        - file_key (str = None) : file key in <!#files>
        - function_key (str=None) : key of the function in <!#pages>
        - exact (bool = True) : use exact name if True, regular expression otherwise
        - only_commented (bool = True) : don't include uncommented functions
        - sub_level (int=1) : incrementation level to page.level

        Returns
        -------
        - <!Function> : created class
        """

        # ---------------------------------------------------------------------------
        # A list of names

        if isinstance(function_name, (tuple, list)):
            for fname in function_name:
                self.add_function(fname, page=page, file_key=file_key)
            return None

        # ---------------------------------------------------------------------------
        # Let's create a properly documented class

        function_ = self.get_refdoc(function_name, key=file_key, halt=True, exact=exact)
        if exact:
            assert(isinstance(function_, Function))

        # ---------------------------------------------------------------------------
        # We register and place it in a page

        if exact:
            fkey = function_.title if function_key is None else function_key
            self.objects[fkey] = function_

            return self.add_section_to_page(function_, page, sub_level=sub_level)

        objs = []
        for f_ in function_:
            if not isinstance(f_, Function):
                continue
            if f_.comment is None or f_.comment == "" and only_commented:
                continue

            fkey = ("" if function_key is None else function_key) + f_.title
            self.objects[fkey] = f_
            objs.append(self.add_section_to_page(f_, page, sub_level=sub_level))

        return objs

    # ----------------------------------------------------------------------------------------------------
    # Sections content

    @property
    def pages_content(self):
        return [s.title for s in self.pages.values()]

    @property
    def objects_content(self):
        a = []
        for o in self.objects.values():
            a.append(f"'{o.title}' in '{o.page.title}'")
        return a

    # ====================================================================================================
    # Hooks

    # ----------------------------------------------------------------------------------------------------
    # Set a hook

    def set_hook(self, expr, repl):
        """ Replace a regular expression by as substitution string

        Hooks are applied to the documentation at compilation time.

        ``` python
        # Instance of [!TOKEN] will be replaced by the substitution text.

        proj.set_hook(r"\[!TOKEN\]", "substitution text")
        ```

        Due to the piece of code above, the token `[!TOKEN]` is replaced here: **[!TOKEN]**

        > [!NOTE]
        > Text embedded in a _source code_ zone is not replaced

        A function can be passed rather than a string as for `re.sub(expr, repl, text)`.

        Here, the passed function can accept a second positional argument if a reference
        to the current section is required:

        ``` python
        def replace(match_obj, section):
            # section is the Section instance where the replacement occurs
            pass
        ```

        > [!NOTE]
        > By default, a hook is used to define links between pages based on the
        > syntax : `<!Section title#Sub section title>` which is converted in <!Project#set_hook>.

        Arguments
        ---------
            - expr (str) : RegEx expression
            - repl (str or function) : replacement string or function
        """
        self.hooks.append({'expr': expr, 'repl': repl})

    # ----------------------------------------------------------------------------------------------------
    # Apply the hooks

    def apply_hooks(self, comment):

        # ----------------------------------------------------------------------------------------------------
        # <!Section title#Sub section in the page> substitution

        def repl_link(m):
            names = m.group(1).split('#')
            if len(names) == 1:
                return self.object_link(names[0].strip())
            else:
                return self.object_link(names[0].strip(), names[1].strip())

        # ----------------------------------------------------------------------------------------------------
        # The default hooks to combine with the custom hooks

        def_hooks = [{'expr': r"<!([\w# ]*)>", 'repl': repl_link}]

        # ----------------------------------------------------------------------------------------------------
        # Main

        if comment is None:
            return None

        # ---- Extract source code
        txt, d = extract_source(comment)

        for hook in def_hooks + self.hooks:

            func = hook['repl']
            if isinstance(func, str):
                repl = func
            else:
                if len(inspect.getfullargspec(func).args) == 1:
                    repl = func
                else:
                    repl = lambda m: func(m, self)

            txt = re.sub(hook['expr'], repl, txt)

        # ----- Replace source code
        comment = replace_source(txt, d)

        return comment

    # ====================================================================================================
    # Compile the documentation

    def compile_project(self):

        # ----------------------------------------------------------------------------------------------------
        # Compile the classes

        def compile_section(section):
            section.compile(self)

        self.iteration(compile_section)
        for object in self.objects.values():
            object.compile(self)

        # ----------------------------------------------------------------------------------------------------
        # Apply the hooks

        def apply_hooks(section):
            section._comment = self.apply_hooks(section._comment)

        self.iteration(apply_hooks)
        for page in self.pages.values():
            a = page.iteration(apply_hooks)
            if a is not None:
                print(f"CAUTION: hook error on object '{a.title}'")

        # ----------------------------------------------------------------------------------------------------
        # Classes section

        #if self.classes_section:
        #    links = ""
        #    for class_name in sorted(self.classes.keys()):
        #        links += f"- [{class_name}]({class_name.lower()}.md)\n"
        #    self.append(Section("Classes", comment=links, level=1))


    # ====================================================================================================
    # Write the index

    def create_index_file(self, file_name):
        """ Create the index file

        Arguments
        ---------
        - file_name (str) : file name to write
        """

        print(f"Create index: {file_name}")

        with Path(file_name).open(mode='w') as f:
            for line in self.build():
                f.write(line)

            if False:

                # ----- Project name

                f.write(f"# {self.name}\n\n")

                # ----- Modules

                # Later

                # ----- Classes

                f.write(f"## Classes\n\n")

                for key in sorted(self.classes):
                    f.write(f"- [{key}]({key.lower()}.md)\n")


    # ====================================================================================================
    # Create the documentation files

    def create_documentation(self, doc_folder):

        self.compile_project()

        doc_folder = Path(doc_folder)

        for page_name, page in self.pages.items():
            file_path = doc_folder / page.md_file_name
            print(f"Create ‘{page_name}' : {file_path}")
            with file_path.open(mode='w') as f:
                for line in page.build():
                    f.write(line)

        self.create_index_file(doc_folder / 'index.md')


# =============================================================================================================================
# Test on the current folder

def gen_docgen():

    # ====================================================================================================
    # Step 1 : Read project files from root folder

    comment = "This is the **DocGen** documentation generated with the projet itself."

    root = Path(__file__).parents[0]
    proj = Project('Simple Python Documentation Generator', comment=comment)
    proj.load_files(root, sub_folders=[])

    # ====================================================================================================
    # Step 2 : Build the pages

    page = proj.new_page("Parser module", "Simple python source parser\n\n", toc='Content')
    page.write("The module <!Parser> parse source file and returns the documentation as a liste of <!Doc> instances.")

    proj.add_class('Parser', page,  capture = ['Reader'])
    proj.add_class('Doc', page)
    functions = page.new_section("Functions")
    proj.add_function('.', page=functions, file_key='docgen/pyparser', exact=False, only_commented=True)

    proj.add_class('Section')
    proj.add_class('Argument', bases=['Section'])
    proj.add_class('Return',   bases=['Section'])
    proj.add_class('Function', bases=['Section'])
    proj.add_class('Class',    bases=['Section'])
    proj.add_class('Project')

    # ====================================================================================================
    # Step 3 : Add complementary pages

    page = proj.new_page("Demo", "This demo file is the source code used to generate this documentation\n\n")

    page.write_source(inspect.getsource(gen_docgen))

    # ====================================================================================================
    # Finalize the index file (the project Section)

    struct = proj.new_section("Project classes", comment="""
        The project is made of two layers.
        1. The first layer is the reference document read from source files
        2. The second layer is a the set of pages of the documentation

        Pages are created and manually fed by reference documentation
        or by manuel additions.
        """)

    struct.new_section("Parser classes")
    struct.write("- <!Parser> : simple python source code parser\n")
    struct.write("- <!Doc> : list of items documentation returned by the [Parser](parser.md)\n")
    struct.write()

    struct.new_section("DocGen classes")
    struct.write("- <!Project> : Project documentation\n")
    struct.write("- <!Class> : Class documentation\n")
    struct.write("- <!Function> : Function documentation\n")
    struct.write("- <!Section> : Base documentation section\n")

    proj.new_section("Demo", "You can see in <!Demo> the source code used to generate this documentation.")

    # ====================================================================================================
    # Step 5 : Create the documentation

    # Demo custom hook
    proj.set_hook(r"\[!TOKEN\]", "substitution text")

    proj.create_documentation(doc_folder=root / 'doc')
