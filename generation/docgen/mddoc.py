#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 08:33:58 2024

@author: alain
"""

from pprint import pprint
from pathlib import Path
import re

from parser import format_list_line, parse_file_source, parse_files
from parser import struct_search, struct_iter, struct_list, capture_inheritance
from parser import extract_source, replace_source

# =============================================================================================================================
# Utilities

def title_to_file_name(title):
    """ Get the file name from the title
    
    Arguments
    ---------
    - title (str) : title
    
    Returns
    -------
    - str : file name (file.md)
    """
    return f"{title.lower().replace(' ', '_')}.md"

def title_to_anchor(title):
    """ Convert the title into markdown anchor
    
    Arguments
    ---------
    - title (str) : title
    
    Returns
    -------
    - str : anchor
    """
    return title.lower().replace(' ', '-')

# =============================================================================================================================
# Base section

class Section:
    
    def __init__(self, title, comment=None, sort_sections=False, in_toc=False, module=None, is_page=False, ignore_if_empty=True, top_bar=None):
        """ Document section
        
        Project documentation is made of **pages** organized in **modules**.
        
        The documentation is based on the versatile class <!Section> which can be:
        - a text section in a page
        - a documentation page
        - a module
        - the whole documentation itself
        
        A <!Section> is basically a list of **sub sections** with a header <!Section#comment>.
        
        Properties
        ----------
        - owner (Section) : owning section
        - children (list of Sections) : child sections
        - title (str) : section title
        - comment (str) : text to display just below the section title
        - sort_sections (bool) : sort sections in alphabetical order when added
        - in_toc (bool) : put this section in the page table of content
        - hidden (bool) : hide this section
        - ignore_if_empty (bool) : don't display the section if it has no content
        - top_bar (str = None or '-') : char to use to display an horizontal bar before the section 
        
        Arguments
        ---------
        - title (str) : section title
        - comment (str) : text to display just below the section title
        - sort_sections (bool) : sort sections in alphabetical order when added
        - in_toc (bool) : put this section in the page table of content
        - module (str) : module path
        - is_page (bool) : this section is a page, child sections will be displayed as sub sections
        - ignore_if_empty (bool) : don't display the section if it has no content
        - top_bar (str = None) : char to use to display an horizontal bar before the section 
        
        """        
        self.owner    = None
        self._module  = module
        self._is_page = is_page or module is not None
        
        self.children = []
        
        # Header content
        self.title   = title
        self.comment = comment
        
        # Options
        self.sort_sections   = sort_sections
        self.in_toc          = in_toc
        self.hidden          = False
        self.ignore_if_empty = ignore_if_empty
        self.top_bar         = top_bar
        
    def __str__(self):
        stype   = "P" if self.is_page else " "
        if self.is_module:
            stype = "M"
        if self.is_top:
            stype = "T"
        shidden = "H" if self.hidden  else "D"
            
        return f"<{self.depth} {stype}{shidden} '{self.module:8s}'{'  '*self.depth_in_page} {self.title}>"
    
    # =============================================================================================================================
    # Hierarchy iteration
    
    def iteration(self, func, *args, include_top=True):
        """ Iterate on the section and child sections
        
        This method calls the function **func** on the section hierarchy.
        
        The **func** template must be:
            
        ```python
        def func(section, *args):
        ````
        
        The following rules apply:
        - The function is not called on `self` if **include_top*$ is False
        - The function is not called on the child sections if it returns 'NO CHILDREN'
          when call on `self` (see <#get_toc>)
        - The iteration stops if the function **func** return True. It returns
          the section for which it is the case (see <#get_section> for instance)
                                                
        Arguments
        ---------
        - func (function) : templace `func(section, *args)`
        - args : args to pass to the function **func** in addition to the section
        - include_top (bool = True) : call the function on self before calling for the child sections
        
        Returns
        -------
        - Section : section for which the function return True, None otherwise
        """
        ok_children = True
        if include_top:
            res = func(self, *args)
                    
            if res == True:
                return self
            
            ok_children = res != 'NO CHILDREN'
            
        if ok_children:
            for section in self.children:
                res = section.iteration(func, *args, include_top=True)
                if res is not None:
                    return res
            
        return None
        
    # =============================================================================================================================
    # Children management
    
    def append(self, section):
        """ Append a new section.
        
        This is were the owner is set in the child section.
        
        > [!NOTE]
        > If the property <#sort_sections> is True, the section is inserted in alphabetical order
        
        Arguments
        ---------
        - section (Section) : the section to append
        
        Returns
        -------
        - section : the added section
        """
        section.owner = self
        self.children.append(section)
        if self.sort_sections:
            self.sort()
        return section
            
    def sort(self):
        """ Sort the child sections
        """
        
        self.children.sort(key=lambda s: s.title)
        
    def get_section(self, title=None, condition=None, **kwargs):
        """ Get a section matching conditons
        
        There are several possible conditions:
        - Section <#title> matches the argument **title**
        - The function **condition** returns True
        - Sections properties match the keyword arguments **kwargs**
        
        This methods call <#iteration> with the following function (simplified version)
        
        ``` python
        def check_section(section):
            
            # In this simplified version, we supposed all the conditions
            # are required
            
            if not section.title == title and condition(section):
                return False
            
            for k, v in kwargs.items():
                if getattr(section, k) != v:
                    return False
                
            # Only matches
            return True
        
        # main
        return self.iteration(check_section)
        ```
        
        > [!NOTE]
        > See <!get_module> or <!get_page> for an example of use
        
        Arguments
        ---------
        - title (str) : section title must be this value if not None
        - condition (function) : function accepting one argument and returning a bool
        - kwargs : pairs of (section attribute, value) 
        
        Returns
        -------
        - Section : the first section matching the conditions, None if not found
        """
        
        # ----------------------------------------------------------------------------------------------------
        # Function : test if title matches and conditions are ok
        
        def ok_section(section, title_):
            if title_ is not None and section.title != title_:
                return False
                
            for k, v in kwargs.items():
                if getattr(section, k) != v:
                    return False
                
            if condition is not None and not condition(section):
                return False
                
            return True

        # ----------------------------------------------------------------------------------------------------
        # No condition on title
        
        if title is None:
            return self.iteration(ok_section, None)
        
        # ----------------------------------------------------------------------------------------------------
        # Title is simple
        
        p = title.find('.')
        if p < 0:
            return self.iteration(ok_section, title)

        # ----------------------------------------------------------------------------------------------------
        # Title is composed
        
        parent = self.get_section(title[:p])
        if parent is None:
            return None
        else:
            return parent.get_section(title[p+1:], **kwargs)

    def get_module(self, title, condition=None, **kwargs):
        """ Get a module Section matching some conditions
        
        Basically call <#get_section> while addinf a supplementary condition
        on the attribute <#is_module>:
            
        ``` python
        return self.get_section(..., is_module=True, ...)
        ``` 
        Arguments
        ---------
        - title (str) : section title must be this value if not None
        - condition (function) : function accepting one argument and returning a bool
        - kwargs : pairs of (section attribute, value) 
        
        Returns
        -------
        - Section : the first module section matching the conditions, None if not found
        """
        return self.get_section(title, condition=condition, is_module=True, **kwargs)

    def get_page(self, title, condition=None, **kwargs):
        """ Get a page Section matching some conditions
        
        Basically call <#get_section> while addinf a supplementary condition
        on the attribute <#is_module>:
            
        ``` python
        return self.get_section(..., is_page=True, ...)
        ``` 
        Arguments
        ---------
        - title (str) : section title must be this value if not None
        - condition (function) : function accepting one argument and returning a bool
        - kwargs : pairs of (section attribute, value) 
        
        Returns
        -------
        - Section : the first page section matching the conditions, None if not found
        """
        return self.get_section(title, condition=condition, is_page=True, **kwargs)
        
        
    # =============================================================================================================================
    # Properties
    
    # -----------------------------------------------------------------------------------------------------------------------------
    # Hierarchy
    
    @property
    def is_top(self):
        """ Is top section
        
        Returns
        -------
        - bool : True if owner is None
        """
        return self.owner is None
    
    @property
    def top(self):
        """ Get the topmost section
        
        Returns
        -------
        - Section : the top section
        """
        if self.owner is None:
            return self
        else:
            return self.owner.top

    @property
    def depth(self):
        """ Distance to the top
        
        Returns
        -------
        - int : Distance to the top (0 for top section)
        """
        if self.owner is None:
            return 0
        else:
            return self.owner.depth + 1
    
    # -----------------------------------------------------------------------------------------------------------------------------
    # Pages
    
    @property
    def is_page(self):
        """ The section is a page
        
        > [!NOTE]
        > Top section is necessarily a page
        
        Returns
        -------
        - bool : True if owner is None
        """
        return self.is_top or self._is_page
    
    @is_page.setter
    def is_page(self, value):
        self._is_page = value
    
    @property
    def page(self):
        """ The page section this section belongs to
        
        > [!CAUTION]
        > Since a page returns self, a misuse could lead to infinite recurrence loop
        
        Returns
        -------
        - Section : page this section belongs to
        """
        return self if self.is_page else self.owner.page
            
    @property
    def depth_in_page(self):
        """ Distance to the page
        
        Returns
        -------
        - int : Distance to the page(0 for page sections)
        """
        if self.is_page:
            return 0
        else:
            return self.owner.depth_in_page + 1
        
    # -----------------------------------------------------------------------------------------------------------------------------
    # Module
    
    @property
    def is_module(self):
        """ The section is a page
        
        A module is a section owning the module name in a private attribute
        
        > [!NOTE]
        > Top section is necessarily a module
        
        Returns
        -------
        - bool : True if owner is None
        """
        return self.is_top or self._module is not None
    
    @property
    def module(self):
        """ The name of the module this section belongs to

        > [!NOTE]
        > Top section return en empty string
        
        Returns
        -------
        - str : name of the module this page belongs to
        """
        if self.is_top:
            return ""
        elif self._module is None:
            return self.owner.module
        else:
            return self._module

    @property
    def module_path(self):
        """ Module path of the section module
        
        A module path is build from the chain of module and submodules
        separated by '-' char.

        > [!NOTE]
        > top module returns ""
        
        > [!NOTE]
        > module paths are used to build full file name without collisions
        
        Returns
        -------
        - str : module path with - char as separator
        """
        if self.is_top:
            return ""

        elif self._module is None:
            return self.owner.module_path

        else:
            owner_path = self.owner.module_path
            if owner_path == "":
                return self._module
            else:
                return owner_path + '-' + self._module
            
    # -----------------------------------------------------------------------------------------------------------------------------
    # Content
    
    @property
    def has_toc(self):
        """ The page has a table of content
        
        A page has a table of content if it contains sections with
        an attribute <#in_toc> = True.
        
        > [!NOTE]
        > Only page sections can have a toc
        
        Returns
        -------
        - bool : True if the page has a toc
        """
        if not self.is_page:
            return False
        
        def check_children(section):
            if section.is_page:
                if section.in_toc and section.has_content:
                    return True
                else:
                    return 'NO CHILDREN'
            else:
                return section.in_toc and section.has_content
            
        return self.iteration(check_children)
        
    @property
    def has_content(self):
        """ The section has a content to display.
        
        The section content is composed of the its <#comment> and its sections in <#children>.
        If comment is empty and no child has a content to display, the section is considered
        as empty.
        
        If the attribute <#ignore_if_empty> is not set, the section is considered as not empty.
        
        > [!NOTE]
        > If a page contains only pages which must appear in a table of content (<#in_toc> is set),
        > the page will have a toc and hence is has a content
        
        Returns
        -------
        - bool : True if the section has content to display
        """
        
        if self.is_top:
            return True
        
        if self.hidden:
            return False
        
        if not self.ignore_if_empty:
            return True
        
        if self.comment is not None:
            return True
        
        def check_children(section):
            if section.is_page:
                if section.hidden or not section.in_toc:
                    return False
                else:
                    return 'NO CHILDREN'
            else:
                return section.in_toc and section.has_content
            
        if self.iteration(check_children) is not None:
            return True
            
        if self.has_toc:
            return True
            
        return False
            
    # -----------------------------------------------------------------------------------------------------------------------------
    # File name / anchor

    @property
    def file_name(self):
        """ File name were to write the page
        
        The file name is built by joining <#module_path> with the name of section.

        > [!NOTE]
        > top module returns "index.md"
        
        Returns
        -------
        - str : file name
        """
        if self.is_top:
            return "index.md"
        
        if self.is_page:
            module_path = self.module_path
            if module_path != '':
                module_path += '-'
            return module_path + title_to_file_name(self.title)
        else:
            return self.page.file_name
        
    @property
    def homonyms_count(self):
        """ Count the number of sections have the same title
        
        This number is used to suffix the title anchor if needed.
        
        > [!NOTE]
        > The number of homonymes is count up the the section itsefl, not after
        
        Returns
        -------
        - int: number of above sections sharing the same title
        """
        anchor = title_to_anchor(self.title)
        
        def func(section, counter):
            if self == section:
                return True
            
            if not section.hidden:
                return False
            
            if title_to_anchor(section.title) == anchor:
                counter[0] += 1
        
        if self.is_page:
            return 0
        
        counter = [0]
        self.page.iteration(func, counter)
        
        return counter[0]
        
        
    @property
    def anchor(self):
        """ The anchor of this section within the page
        
        Returns
        -------
        - str : section anchor
        """
        anchor = title_to_anchor(self.title)
        if self.is_page:
            return anchor
        else:
            count = self.homonyms_count
            if count == 0:
                return anchor
            else:
                return f"{anchor}-{count}"
            
    def link_to(self, absolute=True, title=None):
        """ returns the link to this section
        
        > [!NOTE]
        > The result could be wrong if sections with the same title are later inserted above this section
        
        Arguments
        ---------
        - Absolute (bool = True) : include file name, only the anchor otherwise
        
        Returns
        -------
        - str : link in md format `[title](file.md#anchor)`
        """
        return f"[{self.title if title is None else title}]({self.file_name if absolute else ''}#{self.anchor})"
        
    # =============================================================================================================================
    # Add sections
    
    def add_module(self, module, title, comment=None, **kwargs):
        """ Add a module section
        
        Arguments
        ---------
        - module (str) : name of the module to create
        - title (str) : section title
        - comment (str) : section comment
        - kwargs : valid section attribute settings
        
        Returns
        -------
        - Section : module section
        """
        return self.add_section(title, comment, module=module, **kwargs)
    
    def add_page(self, title, comment=None, **kwargs):
        """ Add a page section
        
        Arguments
        ---------
        - title (str) : section title
        - comment (str) : section comment
        - kwargs : valid section attribute settings
        
        Returns
        -------
        - Section : page section
        """
        return self.add_section(title, comment, is_page=True, **kwargs)

    def add_section(self, title, comment=None, **kwargs):
        """ Add a section
        
        Arguments
        ---------
        - title (str) : section title
        - comment (str) : section comment
        - kwargs : valid section attribute settings
        
        Returns
        -------
        - Section : module section
        """        
        return self.append(Section(title, comment, **kwargs))
    
    def get_create_section(self, title, comment=None,**kwargs):
        """ Get an existing section or create a new one
        
        > [!NOTE]
        > Contrary to <#get_section>, this method searchs the section only
        > in the direct children, not in all the hierarchy.
        
        Arguments
        ---------
        - title (str) : section title
        - comment (str) : section comment
        - kwargs : valid section attribute settings
        
        Returns
        -------
        - Section : module section
        """        
        for section in self.children:
            if section.title == title:
                return section
        return self.add_section(title, comment=comment, **kwargs)
    
    # =============================================================================================================================
    # Table of content
    
    def get_toc(self, title='Content', level=2):
        """ Build the text for table of content
        
        > [!NOTE]
        > The toc is inserted directly after the <#comment> and not as a
        > specific section
        
        Arguments
        ---------
        - title (str = 'Content') : content section title
        - level (int = 2) : markdown level
        
        Returns
        -------
        - str : markdown text for the table of content
        """
        if not self.is_page:
            return None
        
        items = {}
        
        def get_items(section):
            if section.in_toc:
                items[section.title] = section.link_to(absolute=section.is_page)
                return 'NO CHILDREN'
                
        self.iteration(get_items, include_top = False)
        if items is None:
            return None
        
        sorted_keys = sorted(items.keys())
        
        # ----------------------------------------------------------------------------------------------------
        # A simple ordered list
        
        if len(items) < 10:
            text = "\n- ".join([items[key] for key in sorted_keys])
            
        # ----------------------------------------------------------------------------------------------------
        # One line per initial
        
        else:
            alpha = {}
            for key in sorted_keys:
                first = key[0].upper()
                first_list = alpha.get(first)
                if first_list is None:
                    first_list = [items[key]]
                    alpha[first] = first_list
                else:
                    first_list.append(items[key])
            
            text = ""
            for first in sorted(list(alpha.keys())):
                text += f"\n- {first} : " + " :black_small_square: ".join(alpha[first])
                
        # Done
                
        return f"\n\n{'#'*level} {title}\n\n" + text + "\n\n"        
    
    
    # =============================================================================================================================
    # Dynamic write
    
    def write(self, text):
        """ Append text to the header comment

        Arguments
        ---------
        - text (str) : the text to write
        """        
        if text is None:
            return

        if self.comment is None:
            self.comment = text
        else:
            self.comment += text

    def write_source(self, source):
        """ Append source code to the header comment

        Arguments
        ---------
        - source (str) : source code to append
        """
        self.write("\n\n``` python\n")
        self.write(source.replace("`", "'"))
        self.write("\n```\n\n")
        
    def write_header(self, level, title, text):
        """ Write a section in the text stream
        
        This method write markdonw text corresponding to a header followed by text.
        
        > [!NOTE]
        > This method doesn't create a section in the hierarchy, contrary to <#add_section>
        
        Arguments
        ---------
        - level (int) : header level
        - title (str) : header title
        - text (str) : text
        """
        self.write(f"\n\n{'#'*level} {title}\n\n{text}\n\n")
        
        
    def write_navigation(self):
        """ Write navigation bar
        """
        self.write(f"\n\n<sub>[top](#{self.page.anchor}) [index](index.md)</sub>\n\n")
        
    # =============================================================================================================================
    # Build the whole documentation
    
    def get_content(self):
        """ Returns the text to write in the page
        
        A page is built by:
        - joining section and comment
        - optionnally joining a table of content
        - recursively joining the content of the children
        
        Returns
        -------
        - str : section and sub section content
        """
        
        if self.top_bar is None:
            header = ""
        else:
            header = self.top_bar * 10 + "\n"
        header += f"#{'#'*self.depth_in_page} {self.title}\n\n"
        
        text = None
        content = self.get_toc()
        
        # ----- Header and comment
        
        if content is not None or not self.ignore_if_empty:
            text = header
            
        if self.comment is not None:
            if text is None:
                text = header + self.comment
            else:
                text += self.comment
                
        # ----- Content
        
        if content is not None:
            text += content
                
        # ----- Children sections
                
        for section in self.children:
            if section.hidden:
                continue
            
            sub_text = section.get_content()
            if sub_text is not None:
                if text is None:
                    text = header + sub_text
                else:
                    text += '\n\n' + sub_text

        return text
    
    def get_documentation(self, create_files=True):
        """ Build and write the whole documentation
        
        The documentation is returned as a dictionary of pages keyed
        by their file name.
        
        Files are actually written if:
        - create_files is True
        - top section as not None <!Doc#doc_folder> attribute
        
        Returns
        -------
        - dict : documentation files content
        """
        doc = {}
        if create_files:
            create_files = self.top.doc_folder is not None
        
        def create_file(section):
            if not section.is_page:
                return
            
            text = section.get_content()
            if text is not None:
                file_name = section.file_name
                assert(file_name not in doc)
                doc[file_name] = text
                
                if create_files:
                    with (self.top.doc_folder / str(file_name)).open(mode='w') as f:
                        f.write(text)
                
        self.iteration(create_file)
        
        return doc
    

    # =============================================================================================================================
    # dev and test

    @classmethod
    def TestStructure(cls):
        
        top = cls("Top", "Top text")
        top.add_section("Top section", "Top section text")
        top.add_section("Top section", "Top section text")
        top.add_section("Hidden section")
        top.add_page("First page", "First page text")
        top.add_page("Second page", "Second page text")
        
        module = top.add_module("M1", "Module 1", "Module 1 text")
        module.add_section("M1 Section")
        module.add_section("M1 Section")
        module.add_section("Homonym")
        module.add_page("First page", "First page text")
        module.add_page("Second page", "Second page text")
        
        module = top.add_module("M2", "Module 2")
        module.add_section("M2 Section A", "Section text")
        module.add_section("M2 Section B", "Section text")
        module.add_section("Homonym")
        
        submodule = module.add_module("M21", "Hidden Module")
        submodule.add_page("Far page").add_section("Far section", "text")
        
        page = module.add_page("Page 1", "Page text")
        page = module.add_page("Page 2", "Page text")
        page = module.add_page("Target section")
        page = module.add_page("Hidden page")
        
        top.add_module("M3", "Hidden Module")
        
        return top
    
    def dump(self):
        print()
        print("Dump of", self.title)
        print('-'*50)
        print()
        def func(section):
            print(str(section), section.anchor)
            
        self.iteration(func)
        print()
        
    def print(self, text_max=100):
        print()
        print("Print documentation of", self.title)
        print('-'*50)
        print()
        
        doc = self.get_documentation()
        for file_name, text in doc.items():
            print('.'*50)
            print('::::',file_name)
            print('')
            if len(text) > text_max:
                print(text[:text_max], '...')
            else:
                print(text)
        
    @staticmethod
    def test_dump():
        
        top = Section.TestStructure()

        top.dump()
        
    @staticmethod
    def test_get():

        top = Section.TestStructure()

        top.dump()
        
        
        print()
        print("Get section / page / module")
        print('-'*50)        
        
        for target in ["Target section", "M2 Section A", "Hidden Module"]:
            print(f"Get Section '{target}' : {top.get_section(target)}")
                    
        for target in ["Target section", "M2 Section A", "Hidden Module"]:
            print(f"Get Page '{target}' : {top.get_page(target)}")
                    
        for target in ["Target section", "M2 Section A", "Hidden Module"]:
            print(f"Get Module '{target}' : {top.get_module(target)}")

        print()
        print("Section path")
        print('-'*50)        
        target = "Module 1.Homonym"
        print(target, ':', top.get_section(target))
        target = "Module 2.Homonym"
        print(target, ':', top.get_section(target))

    @staticmethod
    def test_doc():

        top = Section.TestStructure()

        top.dump()
        
        top.print()
        
# =============================================================================================================================
# Documentation class

class Doc(Section):
    def __init__(self, title, doc_folder, source_folder=None):
        """ Markdown documentation package
        
        This class is a subclass of <!Section> and is to top section of the
        hierarchy of sections
        
        Properties
        ----------
        - doc_folder (str) : target folder for documentation files
        - source_folder (str) : root folder for files
        - parsed (dict) : dictionary of loaded and parsed filed
        - hooks (list) : list of regular expressions and hook function to apply on the documentation
        
        Arguments
        ---------
        - title (str) : documentation title, displayed as title of index.md file
        - doc_folder (str) : target folder for documentation
        - source_folder (str) : root folder where to load files from
        """
        
        super().__init__(title)
        
        # Source and target folders
        
        self.doc_folder = Path(doc_folder)
        self.source_folder = source_folder
        
        # ----------------------------------------------------------------------------------------------------
        # Source filers
        
        self.parsed = {'obj': 'file', 'name': 'title', 'comment': None, 'subs': {}}
        
        # ----- Compile regex expression to solve links
        
        self.solve_links_expr = r'<(!(?P<page>[^#">]*))?(#(?P<section>[^">]*))?("(?P<display>[^>]*))?>'
        self.solve_links_re   = re.compile(self.solve_links_expr, flags=re.MULTILINE)
        
        # ----- Custom hooks
        
        self.hooks = []
        
    # =============================================================================================================================
    # Documentation from file management
    
    @property
    def files(self):
        """ Dictionary of parsed files.
        
        Returns
        -------
        - dict
        """
        return self.parsed['subs']
    
    def files_search(self, **kwargs):
        return struct_search(self.parsed, **kwargs)
    
    def files_iter(self, f, *args, **kwargs):
        return struct_iter(self.parsed, f, *args, **kwargs)
    
    def files_list(self, name_only=True, **kwargs):
        return struct_list(self.parsed, name_only=name_only, **kwargs)
    
    def get_class(self, class_name):
        return self.files_search(obj='class', name=class_name)
    
    @property
    def classes_list(self):
        """ List of classes
        
        Returns
        -------
        - list : list of class dictionaries
        """
        return self.files_list(obj='class')
        
    # ----------------------------------------------------------------------------------------------------
    # Add a source file

    def load_source(self, key, text):
        """ Add a source code.

        The source code is parsed and the resulting dict is stored in the <!#parsed> dict.

        Arguments
        ---------
        - key (str) : source file key
        - text (str) : the source code

        Returns
        -------
        - Section
        """
        
        if key in self.files:
            raise Exception(f"Impossible to add the source keyed by '{key}': key already exists in {list(self.files.keys())}")

        self.files[key] = parse_file_source(text)
        
    
    # ----------------------------------------------------------------------------------------------------
    # Load source files from a folder

    def load_file(self, file_key, file_name, verbose=False):
        """ Enrich the reference doc by parsing source files.

        All the files with `.py` extension are parsed.

        Arguments
        ---------
        - file_key (str) : file key in <#files>
        - file_name (str) : file path
        """
        
        file_key = str(file_key)

        self.load_source(file_key, Path(file_name).read_text())
        if verbose:
            print(f"load {Path(file_name).name} : ", self.file_info(file_key))
        

    # ----------------------------------------------------------------------------------------------------
    # Load source files from a folder

    def load_folder(self, folder, verbose=True):
        """ Enrich the reference doc by parsing source files.
        
        > [!CAUTION]
        > if <#source_folder> is not None, folder is relative to it

        All the files with `.py` extension are parsed.

        Arguments
        ---------
        - folder (str) : absolute folder or folder relative to <#source_folder> if not None

        Returns
        -------
        - self
        """
        
        if self.source_folder is None:
            abs_folder = Path(folder)
        else:
            abs_folder = self.source_folder / folder

        if not abs_folder.exists():
            raise Exception(f"Folder {folder} doesn't exist")
        if not abs_folder.is_dir():
            raise Exception(f"Path {folder} is not a folder")

        folder_key = Path(folder)
        for fpath in abs_folder.iterdir():
            if not fpath.match("*.py"):
                continue
            
            self.load_file(folder_key / fpath.stem, fpath, verbose=verbose)

        return self
    
    def file_info(self, key):
        
        file = self.files.get(key)
        
        if file is None:
            return f"File '{key}' not found in {list(self.files.keys())}"
        
        else:
            nclasses = len([s for s in file['subs'].values() if s['obj'] == 'class'])
            nfuncs   = len([s for s in file['subs'].values() if s['obj'] == 'function'])
            return f"File '{key}' : {nclasses} classes, {nfuncs} functions"
    
    def files_content(self):
        return f"{len(self.files)} files:\n" + "\n".join([self.file_info(key) for key in self.files])
    
    # ----------------------------------------------------------------------------------------------------
    # Hidden inheritance
    
    def hide_classes(self, classes, verbose=True):
        """ Undocument classes
        
        Properties and methods of undocumented classes are capture by inherited classes
        """
        
        if isinstance(classes, str):
            classes = [classes]
        
        for base_name in classes:
            base_ = self.files_search(obj='class', name=base_name)
            if base_ is None:
                raise Exception(f"Hide classes: class '{base_name}' not found")
                
            base_['hidden'] = True
                
            def hide(class_):
                if base_name in class_['inherits']:
                    if verbose:
                        print(f"Hide '{base_name}' inheritance in '{class_['name']}'")
                    capture_inheritance(class_, base_, remove=True)
                
            self.files_iter(hide, obj='class')
    

    # =============================================================================================================================
    # Hook function
    
    # ----------------------------------------------------------------------------------------------------
    # Set a hook

    def set_hook(self, expr, repl):
        """ Replace a regular expression by as substitution string

        Hooks are applied to the documentation at compilation time.

        ``` python
        # Instance of [!TOKEN] will be replaced by the substitution text.

        proj.set_hook(r"\[!TOKEN\]", "substitution text")
        ```

        Due to the piece of code above, the anchor `[!TOKEN]` is replaced here: **[!TOKEN]**

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
        self.hooks.append({'expr': expr, 'repl': repl, 'cexpr': re.compile(expr, flags=re.MULTILINE)})

    # -----------------------------------------------------------------------------------------------------------------------------
    # Custom links
    
    def solve_section_links(self, section, ignore_source=False):
        
        # ----- Regex substitution function
        
        def repl(m):
            page_title    = m.group('page')
            section_title = m.group('section')
            display       = m.group('display')
            
            # ----------------------------------------------------------------------------------------------------
            # Display
            
            if display is None:
                if section_title is None:
                    if page_title is None:
                        return m.group(0)
                    else:
                        display = page_title.strip()
                else:
                    display = section_title.strip()
            else:
                display = display.strip()
        
            # ----------------------------------------------------------------------------------------------------
            # File
                
            path = ""
            target_page = section.page
                
            if page_title is not None:
                target_page = self.get_page(page_title.strip())
                if target_page is None:
                    display = f"LINK ERROR: page '{page_title}' not found"
                else:
                    path = target_page.file_name
        
            # ----------------------------------------------------------------------------------------------------
            # Token
                
            if target_page is not None and section_title is not None:
                target_section = target_page.get_section(section_title.strip())
                if target_section is None:
                    display = f"LINK ERROR: section '{section_title}' not found"
                else:
                    path += f"#{target_section.anchor}"
                
            return f"[{display}]({path})"
        
        # ----- Main
        
        if section.comment is None:
            return

        # Extract source code
        
        codes = None
        if not ignore_source:
            section.comment, codes = extract_source(section.comment)
            
        # Solve the links
        
        if section.comment is not None:
            section.comment = self.solve_links_re.sub(repl, section.comment)

        # Replace source code

        if not ignore_source:
            section.comment = replace_source(section.comment, codes)
            
    # -----------------------------------------------------------------------------------------------------------------------------
    # Solve the hooks
    
    def solve_links(self, ignore_source=False):
        """ Solve user links into MD links.
        
        Syntax of user link is made of three parts is
        `<!Page title#Section title"Display string>`:
        - _Page title_ : title of the page to link to. If no given,
          an intra page link is returned
        - _Section title_ : title of the section within the page, or
          within the current page if first parameter is not given
        - _Display string_ : display string of the link, _Section title_ or
          _Page title_ is taken in this order
         
        > [!NOTE]
        > If a link can't be solved, the links contains an error message.
        
        > [!IMPORTANT]
        > <#_anchor> and <#is_page> must have been set correctly before solving the links.
         
        Arguments
        ---------
        - ignore_source (bool = False)) : Do not extract source before solving (already done)  
        """
        
        self.iteration(lambda section: self.solve_section_links(section, ignore_source=ignore_source))
            
    # -----------------------------------------------------------------------------------------------------------------------------
    # Solve the hooks
    
    def solve_hooks(self, include_links=True):
        """ Solve all the hooks for a section.
        
        Arguments
        ---------
        - include_links (bool = True) : solve also the links
        """
        
        # ----------------------------------------------------------------------------------------------------
        # Solve the hooks for a section
    
        def solve_section(section):
            
            if section.comment is None:
                return
        
            # ---- Extract source code
            
            section.comment, d = extract_source(section.comment)
            
            # ----- Loop on the hooks
        
            for hook in self.hooks:
    
                func = hook['repl']
                if isinstance(func, str):
                    repl = func
                else:
                    if len(inspect.getfullargspec(func).args) == 1:
                        repl = func
                    else:
                        repl = lambda m: func(m, section)
    
                txt = hook['cexpr'].sub(repl, section.comment)
                
            # ----- Finalize with the links
            
            if include_links:
                self.solve_section_links(section, ignore_source = True)
        
            # ----- Replace source code
    
            section.comment = replace_source(section.comment, d)
            
        # ----------------------------------------------------------------------------------------------------
        # Main : iteration on all sections
        
        self.iteration(solve_section)
        
    # =============================================================================================================================
    # Put items in the documentation to build
    
    def document_folder(self, folder_key):
        
        title = Path(folder_key).stem
        
        init_dict = self.files.get(str(Path(folder_key) / '__init__'))
        
        if init_dict is None:
            comment = None
        else:
            comment = init_dict['comment']
            
        if title == "":
            # Root folder
            module = self
            if module.comment is None:
                module.comment = comment
            else:
                module.comment += '\n\n' + comment
                
                
        else:
            module = self.add_module(title, comment, in_toc=True)
        
        for key, file_dict in self.files.items():
            if str(Path(key).parents[0]) == folder_key:
                module.add_file_dict(file_dict)
        
        
    # =============================================================================================================================
    # Create self documentation
    
    @staticmethod
    def docgen_documentation():
        
        # -----------------------------------------------------------------------------------------------------------------------------
        # Target folder as sub folder 'doc' in the current folder
        
        folder = Path(__file__).parents[0]
        doc_folder = folder / 'doc'
        
        # -----------------------------------------------------------------------------------------------------------------------------
        # Initialize the documentation
            
        doc = Documentation("Documentation Generator", doc_folder)
        
        # -----------------------------------------------------------------------------------------------------------------------------
        # Load the source files
        
        doc.load_folder('', verbose=True)
        file = doc.files_search(name='Documentation')
        pprint(file.get('comment'))
        
        # -----------------------------------------------------------------------------------------------------------------------------
        # Adding and twisting
        
        
        # -----------------------------------------------------------------------------------------------------------------------------
        # Structure
        
        doc.document_folder('.')
        
        doc.solve_hooks()
        
        # -----------------------------------------------------------------------------------------------------------------------------
        # Write
        
        #doc.dump()
        
        #doc.print()
        
        doc.get_documentation()
        
        
        
        
        
    # =============================================================================================================================
    # Dev and tests

    @classmethod
    def test_file(cls, file_name=None, doc_folder=None):

        
        if file_name is None:
            file_name = __file__
            
        folder = Path(file_name).parents[0]
        
        if doc_folder is None:
            doc_folder = folder / 'testdoc'
        
        print("doc_folder", str(doc_folder))
            
            
        proj = cls("Documentation", doc_folder)
        
        text = parse_file_source(Path(__file__).read_text())
        
        proj.add_file_dict(text)
        
        #proj.dump()
        
        #proj.print()
        
        sect = proj.get_section('Section')
        print(sect)
        print(sect.is_page, sect.file_name, sect.link_to(False), sect.link_to(True))
        
        proj.get_documentation(True)
        
    
    
        
        
        
                    
Documentation.docgen_documentation()
                
