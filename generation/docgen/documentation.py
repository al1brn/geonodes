#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 17:42:12 2024

@author: alain
"""

import re
from pathlib import Path
from pprint import pprint


from parser import format_list_line, parse_module, parse_files
from parser import struct_search, struct_iter, struct_list, capture_inheritance
from parser import extract_source, replace_source


def title_to_file_name(title):
    return f"{title.lower().replace(' ', '_')}.md"

def title_to_anchor(title):
    return title.lower().replace(' ', '-')

# =============================================================================================================================
# Section

class Section(list):
    def __init__(self, title, comment=None):
        """ Document section
        
        Project documentation is made of **pages** organized in **modules**.
        Modules and pages are articulated as folders and files but the document
        hierarchy doesn't have to stick to the structure of the source folders.
        
        Loading a source file will return **classes** and global **functions**:
        - each class is documented in a dedicated page
        - functions are documented in a module page
        - TBD : global objects (vars for instance) will be treated as functions
        
        Hence, loading a source file, or  files from a folder, is done with a target module:
        - functions will be added to the module page
        - classes will be added as pages of the modules and refered in the module page
        
        Here after is the template for a module page:
            
        ```
        # Module name
        ...
        
        ## Content
        - classes (links to dedicated pages)
          - MyClass1
          - MyClass2
          
        - functions (page anchors)
          - my_function1
          - my_function2
          
        ## my_function1
        ...
        
        ## my_function2
        ...
        ```
        
        The documentation is based on the versatile class <!Section> which can be:
        - a text section in a page
        - a documentation page
        - a module
        - the whole documentation itself
        
        A <!Section> is basically a list of **sub sections** with a header <!Section#comment>.
        Its attributes drive its behavior:
            
        - <!Section#is_page> : the section is written in a dedicated page, otherwise
          it is written if the flow of the <!Section#page> it belongs to.
          Wheter a section is a page or not is taken into account to build links toward this section.
        
        
        A <!Section> is intended to be written in
          the documentation file as comment followed by its sub sections.
          
          
        ``` python
        doc = Documentation("Project documentation")
        
        # ----- Load source files in the documentation main modules
        
        doc.load_folder(folder_path1)
        doc.load_folder(folder_path2)
        
        # ----- Create another module from other folder
        
        module = doc.new_module("Some module", folder_path3)
        module.load_folder(folder_path3)
        ```
        """
        
        super().__init__()
        
        self.title   = title
        self.comment = comment
        
        self.key     = None
        
        self._page   = None
        self._depth  = 0
        self._anchor  = None
        
        self.navigation = f"\n\n<sub>[top](#{self.anchor}) [index](index.md)</sub>\n\n"
        
        
    def __str__(self):
        return f"<Section({len(self)}) {self.depth}. {self.title}>"
        
    def __repr__(self):
        return str(self)
        
    # ====================================================================================================
    # Sections management
    
    # ----------------------------------------------------------------------------------------------------
    # Iteration on sections and subsections

    def iteration(self, f, *args):
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
        ok = f(self, *args)

        if ok == True:
            return self

        for section in self:
            s = section.iteration(f, *args)
            if s is not None:
                return s

        return None        

    # ----------------------------------------------------------------------------------------------------
    # Flat list of sections and sub sections
        
    def sections(self, with_owner=False):
        """ Flat list of sections and sub sections
        """
        res = []
        for section in self:
            if with_owner:
                res.append((self, section))
            else:
                res.append(section)
            res.extend(section.sections(with_owner=with_owner))
        return res

    # ----------------------------------------------------------------------------------------------------
    # Get a section by its title or path
    
    def get_section(self, title):
        """ Get a section by its title or path
        """
        section = self
        for sub_title in title.split('.'):
            found = None
            for s in section:
                if s.title == sub_title:
                    found = s
                    break
            if found is None:
                return None
            
            section = found
            
        return section

    # ====================================================================================================
    # Depth
    
    @property
    def depth(self):
        return self._depth
    
    @depth.setter
    def depth(self, value):
        self._depth = value
        for section in self:
            section.depth = value + 1

    # ====================================================================================================
    # Tokens
    
    def set_anchors(self):
        self._anchor = title_to_anchor(self.title)
        anchors = {self._anchor: 1}
        
        for section in self.sections():
            anchor = title_to_anchor(section.title)
            if anchor in anchors:
                count = anchors[anchor]
                section._anchor = f"{anchor}-{count}"
                anchors[anchor] = count + 1
            else:
                section._anchor = f"{anchor}"
                anchors[anchor] = 1
    
    
    @property
    def page(self):
        if self._page is None:
            return self
        else:
            return self._page
        
    @page.setter
    def page(self, value):
        self._page = None if value == self else value
        for section in self:
            section.page = value
        
    @property
    def is_page(self):
        return self._page is None
    
    @is_page.setter
    def is_page(self, value):
        if value == True:
            self.page  = self
        else:
            self.page = value
        
    
    @property
    def file_name(self):
        if self.is_page:
            return title_to_file_name(self.title if self.key is None else self.key)
        else:
            return self.page.file_name

    @property
    def anchor(self):
        if self._anchor is None:
            return title_to_anchor(self.title)
        else:
            return self._anchor
        
    def mdlink(self, title=None, local=False):
        link = f"#{self.anchor}"
        if not local:
            link = self.file_name + link
        if title is None:
            title = self.title
        return f"[{title}]({link})"
    
    
    # ====================================================================================================
    # Dynamic documentation

    def new_section(self, title, comment=None):
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

        section = Section(title, comment=comment)
        self.append(section)

        return section

    def write_header(self, comment):
        """ Append text to the header comment

        Arguments
        ---------
        - comment (str) : the text to write
        """
        
        if comment is None:
            return

        if self._comment is None:
            self._comment = comment
        else:
            self._comment += comment

    def write(self, comment):
        """ Append text to the current text

        The current text is either the comment if this section if there is not sub sections,
        or the comment of the last sub sections.

        Arguments
        ---------
        - comment (str) : the text to write
        """
        
        if comment is None:
            return

        if len(self):
            self[-1].write(comment)

        else:
            if self.comment is None:
                self.comment = comment
            else:
                self.comment += comment

    def write_source(self, source):
        self.write("\n\n``` python\n")
        self.write(source.replace("`", "'"))
        self.write("\n```\n\n")       

    # ====================================================================================================
    # Add a table of contents
    
    def add_toc(self, name='Content', sub_sections=False):
        
        if sub_sections:
            section_names = []
            for section in self:
                section_names.extend([s.title for s in section])
            section_names = sorted(section_names)
            
        else:
            section_names = sorted([s.title for s in self])
            
        toc = Section(name, comment = "\n".join([f"<#{section_name}>" for section_name in section_names]))
        self.insert(0, toc)
        return toc
    
    # ====================================================================================================
    # A table of contents
    
    @classmethod
    def Toc(cls, items, title='Content'):
        """ Create a table of content from the given list
        
        Arguments
        ---------
        - items (list) : list of couples (key, value)
        
        Returns
        -------
        - Section
        """
        
        sorted_items = sorted(items, key=lambda item: item[0])
        
        # ----------------------------------------------------------------------------------------------------
        # A simple ordered list
        
        if len(items) < 10:
            text = "\n- ".join([item[1] for item in sorted_items])
            
        # ----------------------------------------------------------------------------------------------------
        # One line per initial
        
        else:
            alpha = {}
            for item in items:
                first = item[0][0].upper()
                first_list = alpha.get(first)
                if first_list is None:
                    first_list = [item[1]]
                    alpha[first] = first_list
                else:
                    first_list.append(item[1])
            
            text = ""
            for first in sorted(list(alpha.keys())):
                text += f"\n- {first} : " + " :black_small_square: ".join(alpha[first])
                
        # Done
                
        return cls(title, comment=text)
        
    # ====================================================================================================
    # From parsed documentation
    
    @classmethod
    def FromParsed(cls, struct, ignore_uncommented=True):
        
        name    = struct['name']
        section = cls(name, struct['comment'])
        
        # ----------------------------------------------------------------------------------------------------
        # Module
        
        if struct['obj'] == 'module':
            
            functions = section.new_section('Functions')
            classes   = section.new_section('Classes')
            toc_items = []
            
            for obj in struct['subs'].values():

                if obj['comment'] is None and ignore_uncommented:
                    continue
                
                obj_section = Section.FromParsed(obj, ignore_uncommented=ignore_uncommented)
                
                obj_section.comment += section.navigation
                
                if obj['obj'] == 'function':
                    functions.append(obj_section)
                    
                elif obj['obj'] == 'class':
                    classes.append(obj_section)
                    
                else:
                    assert(False)
                    
                toc_items.append((obj_section.title, f"[{obj_section.title}](#{obj_section.anchor})"))
                    
            # ----- Format the page
                    
            functions.sort(key=lambda s: s.title)
            classes.sort(key=lambda s: s.title)
            
            section.insert(0, Section.Toc(toc_items, 'Content'))
                    
        # ----------------------------------------------------------------------------------------------------
        # Class
        
        elif struct['obj'] == 'class':
            
            properties = section.new_section('Properties')
            methods    = section.new_section('Methods')
            toc_items  = []
            
            if struct.get('__init__') is not None:
                if struct.get('args') is not None:
                    section.write_source(f"{name}({struct['args']})")
                
                if struct['__init__']['comment'] is not None:
                    init_ = Section.FromParsed(struct['__init__'])
                    section.write("\n\n**__init__**\n\n")
                    section.write(init_.comment)
                
            
            for obj in struct['subs'].values():
                
                if obj['comment'] is None and ignore_uncommented:
                    continue
                
                obj_section = Section.FromParsed(obj, ignore_uncommented=ignore_uncommented)
                
                obj_section.comment += section.navigation
                
                
                if obj['obj'] == 'property':
                    properties.append(obj_section)
                    
                elif obj['obj'] == 'function':
                    methods.append(obj_section)
                    
                else:
                    assert(False)
                    
                toc_items.append((obj_section.title, f"[{obj_section.title}](#{obj_section.anchor})"))

            # ----- Format the page
                    
            properties.sort(key=lambda s: s.title)
            methods.sort(key=lambda s: s.title)
            
            section.insert(0, Section.Toc(toc_items, 'Content'))
                

        # ----------------------------------------------------------------------------------------------------
        # Function / Method
        
        elif struct['obj'] == 'function':
            
            if struct.get('args') is not None:
                section.write_source(f"{name}({struct['args']})")
            
            if len(struct['raises']):
                sub = section.new_section('Raises', "\n- ".join([format_list_line(d) for d in struct['raises']]))
                                      
            if len(struct['arguments']):
                sub = section.new_section('Arguments', "\n- ".join([format_list_line(d) for d in struct['arguments']]))
                                      
            if len(struct['returns']):
                sub = section.new_section('Returns', "\n- ".join([format_list_line(d) for d in struct['returns']]))
                                      
        # ----------------------------------------------------------------------------------------------------
        # Function / Method
        
        elif struct['obj'] == 'property':
            
            if struct.get('type') is not None:
                section.write(f"> type {struct['type']}\n")
            if struct.get('default') is not None:
                section.write(f"> default {struct['default']}\n")
                
            if struct.get('getter') is not None:
                sct = Section.FromParsed(struct['getter'], ignore_uncommented=ignore_uncommented)
                sct.title = 'Getter'
                section.append(sct)
                
            if struct.get('setter') is not None:
                sct = Section.FromParsed(struct['setter'], ignore_uncommented=ignore_uncommented)
                sct.title = 'Setter'
                section.append(sct)
                
        else:
            assert(False)
            
        
        return section
    
    # ====================================================================================================
    # yield lines   
    
    def yield_content(self):
        
        if True:
            #yield f'<h{self.depth+1} id="{self._anchor}">{self.title}</h{self.depth+1}>'
            yield f"#{'#'*self.depth} {self.title}\n\n"
        else:
            a_, _a = '{', '}'
            yield f"#{'#'*self.depth} {self.title} {a_} #{self._anchor} {_a}\n\n"
        
        if self.comment is not None:
            yield self.comment + '\n\n'
            
        for section in self:
            for line in section.yield_content():
                yield line
            

    # ====================================================================================================
    # Debug

    def print(self, full=False):
        """ Print the documentation in the console

        For debug purpose.
        """
        INDENT = '   '
        print(f"{INDENT*(self.depth+1)} # {self.title}")
        if self.comment is not None and full:
            print(self.comment)
            
        for section in self:
            section.print(full=full)
            continue


# =============================================================================================================================
# Documentation        
                
class Documentation(Section):
    def __init__(self, title, comment=None):
        """ Whole project documentation
        
        A **Project** is a <!Section> which is the top level page of the document,
        and whose sections are alse pages.
        
        <!Section> <!Section#title> must be unique.
        """
        
        super().__init__(title, comment=comment)
        
        self.key     = 'index'
        self._anchor  = 'index'
        self.is_page = True
        
        # ----- A module of modules
        
        self.parsed = {'obj': 'module', 'name': 'title', 'comment': None, 'subs': {}}
        
        # ----- Compile regex expression to solve links
        
        self.solve_links_expr = r'<(!(?P<page>[^#">]*))?(#(?P<section>[^">]*))?("(?P<display>[^>]*))?>'
        self.solve_links_re   = re.compile(self.solve_links_expr, flags=re.MULTILINE)
        
        # ----- Custom hooks
        
        self.hooks = []
        
    # =============================================================================================================================
    # Documentation from file management
    
    @property
    def modules(self):
        return self.parsed['subs']
    
    def modules_search(self, **kwargs):
        return struct_search(self.parsed, **kwargs)
    
    def modules_iter(self, f, *args, **kwargs):
        return struct_iter(self.parsed, f, *args, **kwargs)
    
    def modules_list(self, name_only=True, **kwargs):
        return struct_list(self.parsed, name_only=name_only, **kwargs)
    
    def get_class(self, class_name):
        return self.modules_search(obj='class', name=class_name)
    
    @property
    def classes_list(self):
        return self.modules_list(obj='class')
    
        
    # ----------------------------------------------------------------------------------------------------
    # Add a source file

    def load_source(self, key, text):
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
        
        if key in self.modules:
            raise Exception(f"Impossible to add the source keyed by '{key}': key already exists in {list(self.modules.keys())}")

        self.modules[key] = parse_module(text, module_name=Path(key).stem)

        return key
    
    # ----------------------------------------------------------------------------------------------------
    # Load source files from a folder

    def load_file(self, file_name, key=None):
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
        
        path = Path(file_name)
        if not path.exists():
            raise Exception(f"File {file_name} doesn't exist")

        if key is None:
            key = path(folder).stem
            
        self.load_source(key, path.read_text())
        
        return key

    # ----------------------------------------------------------------------------------------------------
    # Load source files from a folder

    def load_files(self, folder=None, sub_folders=[], key=None, verbose=True):
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

        root_folder = Path(folder)
        if not root_folder.exists():
            raise Exception(f"File {file_name} doesn't exist")
        if not root_folder.is_dir():
            raise Exception(f"Path {file_name} is not a folded")
        
        if key is None:
            key = root_folder.stem

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
                load_key = str(Path(file_key) / fpath.stem)

                self.load_source(load_key, fpath.read_text())
                if verbose:
                    print(f"load {fpath.name} : ", self.module_info(load_key))

        return self
    
    def module_info(self, key):
        module = self.modules.get(key)
        if module is None:
            return f"Module '{key}' not founds"
        else:
            nclasses = len([s for s in module['subs'].values() if s['obj'] == 'class'])
            nfuncs   = len([s for s in module['subs'].values() if s['obj'] == 'function'])
            return f"Module '{key}' : {nclasses} classes, {nfuncs} functions"
    
    def modules_content(self):
        return f"{len(self.modules)} modules:\n" + "\n".join([self.module_info(key) for key in self.modules])
    
    # ----------------------------------------------------------------------------------------------------
    # Hidden inheritance
    
    def hide_classes(self, classes, verbose=True):
        """ Undocument classes
        
        Properties and methods of undocumented classes are capture by inherited classes
        """
        
        if isinstance(classes, str):
            classes = [classes]
        
        for base_name in classes:
            base_ = self.modules_search(obj='class', name=base_name)
            if base_ is None:
                raise Exception(f"Hide classes: class '{base_name}' not found")
                
            base_['hidden'] = True
                
            def hide(class_):
                if base_name in class_['inherits']:
                    if verbose:
                        print(f"Hide '{base_name}' inheritance in '{class_['name']}'")
                    capture_inheritance(class_, base_, remove=True)
                
            self.modules_iter(hide, obj='class')
    
    
    # =============================================================================================================================
    # Add pages to the documentation
    
    def get_page(self, title):
        
        if title == 'index' or title == self.title:
            return self
        
        
        for section in self:
            if section.title == title:
                return section
        return None
    
    # ----------------------------------------------------------------------------------------------------
    # Add a page

    def add_page(self, section):
        """ Add a page in the documentation

        Arguments
        ---------
        - page (<!Section>) : the page to add

        Returns
        -------
        - <!Section> : the argument **page**
        """
        if self.get_section(section.title) is not None:
            print("Existing pages:", [s.title for s in self])
            return
            #raise Exception(f"Error when adding page '{section.title}' : the page already exists!")
            
        section._page = None
        self.append(section)
            
        return section

    # ----------------------------------------------------------------------------------------------------
    # Create a new page

    def new_page(self, title, comment=None):
        """ Add a page in the documentation

        > [!CAUTION]
        > **title** argument is used a as key in <!#pages> dictionary. It must be unique
        > in the scope of the project

        Arguments
        ---------
        - title (str) : page title
        - comment (str) : comment

        Returns
        -------
        - <!Section>
        """
        return self.add_page(Section(title, comment))
    
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
    # Creating the documentation files
    
    # -----------------------------------------------------------------------------------------------------------------------------
    # Custom links
        
    
    
    # -----------------------------------------------------------------------------------------------------------------------------
    # Compilation
    
    def compile(self):
        """ Initialize sections parameters at their good values
        """
        
        # ----------------------------------------------------------------------------------------------------
        # Section proper structure paremeters
        
        for section in self:
            section.is_page = True
            section.depth = 0
            section.set_anchors()
            
        # ----------------------------------------------------------------------------------------------------
        # Apply the hooks
        
        self.solve_hooks(include_links=True)
            
            
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

        self.compile()

        doc_folder = Path(doc_folder)
        
        for page in self:
            file_path = doc_folder / page.file_name
            print(f"Create ‘{page.title}' : {file_path}")
            with file_path.open(mode='w') as f:
                for line in page.yield_content():
                    f.write(line)

        #self.create_index_file(doc_folder / 'index.md')
            

    

    
# =============================================================================================================================
# Test on the current folder

def gen_docgen():
    
    # ====================================================================================================
    # Step 1 : Load project files from root folder

    comment = "This is the **DocGen** documentation generated with the projet itself."
    
    if True:
        root = Path(__file__).parents[0]
        proj = Documentation('Simple Python Documentation Generator', comment=comment)
        
        proj.load_files(root, sub_folders=[])
        
        
    else:
        folder = Path("/Users/alain/Documents/blender/scripts/modules/geonodes")
        proj = Documentation('Script nodes')
        #proj.load_files(folder)
        proj.load_files(folder / 'geonodes')
        
        print('-'*50)
        print('CLASSES', proj.classes_list)
        #proj.load_files(folder / 'shadernodes')

        gn = proj.get_class('GeoNodes')
        pprint(gn['inherits'])
        proj.hide_classes('Tree')
        pprint(gn['inherits'])
        
    # ====================================================================================================
    # Tune reference doc
    
    for module in proj.modules.values():
        print("Module", module['name'])
        proj.add_page(Section.FromParsed(module))
    
    proj.create_documentation(doc_folder=root / 'testdoc')
    
    

        
    
    # ====================================================================================================
    # Step 2 : Build the pages

    page = proj.new_page("Parser module", "Simple python source parser\n\n")
    page.write("The module <!Parser> parse source file and returns the documentation as a liste of <!Doc> instances.")
    
    return

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
    

gen_docgen()