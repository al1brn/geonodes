#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 08:33:58 2024

@author: alain
"""

from pprint import pprint
from pathlib import Path

from parser import format_list_line, parse_file_source, parse_files
from parser import struct_search, struct_iter, struct_list, capture_inheritance
from parser import extract_source, replace_source


def title_to_file_name(title):
    return f"{title.lower().replace(' ', '_')}.md"

def title_to_anchor(title):
    return title.lower().replace(' ', '-')


class Section:
    
    def __init__(self, title, comment=None, sort_sections=False, in_toc=False, module=None, is_page=False, ignore_if_empty=True, top_bar=None):
        """ Document section
        
        Project documentation is made of **pages** organized in **modules**.
        Modules and pages are articulated as folders and files but the document
        hierarchy doesn't have to stick to the structure of the source folders.
        
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
        
        if include_top:
            res = func(self, *args)
            if res == True:
                return self
            
        for section in self.children:
            res = section.iteration(func, *args, include_top=True)
            if res is not None:
                return res
            
        return None
        
    # =============================================================================================================================
    # Children management
    
    def append(self, section):
        section.owner = self
        self.children.append(section)
        if self.sort_sections:
            self.sort()
        return section
            
    def sort(self):
        self.children.sort(key=lambda s: s.title)
        
    def get_section(self, title=None, condition=None, **kwargs):
        
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
        return self.get_section(title, condition=condition, is_module=True, **kwargs)

    def get_page(self, title, condition=None, **kwargs):
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
    def depth(self):
        if self.owner is None:
            return 0
        else:
            return self.owner.depth + 1
    
    # -----------------------------------------------------------------------------------------------------------------------------
    # Pages
    
    @property
    def is_page(self):
        return self.is_top or self._is_page
    
    @is_page.setter
    def is_page(self, value):
        self._is_page = value
    
    @property
    def page(self):
        return self if self.is_page else self.owner.page
            
    @property
    def depth_in_page(self):
        if self.is_page:
            return 0
        else:
            return self.owner.depth_in_page + 1
        
    # -----------------------------------------------------------------------------------------------------------------------------
    # Module
    
    @property
    def is_module(self):
        return self.is_top or self._module is not None
    
    @property
    def module(self):
        if self.is_top:
            return ""
        elif self._module is None:
            return self.owner.module
        else:
            return self._module

    @property
    def module_path(self):
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
        if self.is_page:
            return self.iteration(lambda s: s.in_toc)
        else:
            return False
        
    @property
    def has_content(self):
        
        DEBUG = self.title == 'Section'

        if not self.ignore_if_empty:
            return True
        
        if self.comment is not None:
            return True
        
        for section in self.children:
            if section.is_page:
                continue
            
            if DEBUG:
                print("DEBUG", section.title, section.hidden)
            
            if not section.hidden:
                return True
            
        if self.has_toc:
            return True
            
        return False
    
    @property
    def hidden(self):
        if self.is_top:
            return False
        
        return not self.has_content
            
    # -----------------------------------------------------------------------------------------------------------------------------
    # file name / anchor

    @property
    def file_name(self):
        if self.is_top:
            return "/index.md"
        
        if self.is_page:
            module_path = self.module_path
            if module_path != '':
                module_path += '-'
            return '/' + module_path + title_to_file_name(self.title)
        else:
            return self.page.file_name
        
    @property
    def homonyms_count(self):
            
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
        return f"[{self.title if title is None else title}]({self.file_name if absolute else ''}#{self.anchor})"
        
    # =============================================================================================================================
    # Add sections
    
    def add_module(self, module, title, comment=None, **kwargs):
        return self.add_section(title, comment, module=module, **kwargs)
    
    def add_page(self, title, comment=None, **kwargs):
        return self.add_section(title, comment, is_page=True, **kwargs)

    def add_section(self, title, comment=None, **kwargs):
        return self.append(Section(title, comment, **kwargs))
    
    def get_create_section(self, title, comment=None,**kwargs):
        for section in self.children:
            if section.title == title:
                return section
        return self.add_section(title, comment=comment, **kwargs)
            
    
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
        self.write("\n\n``` python\n")
        self.write(source.replace("`", "'"))
        self.write("\n```\n\n")
        
    def write_navigation(self):
        self.write("\n\n<sub>[top](#{self.page.anchor}) [index](index.md)</sub>\n\n")
        
        
    # =============================================================================================================================
    # Build the whole documentation
    
    def get_content(self):
        """ Returns the text to write in the page
        """
        
        if self.top_bar is None:
            header = ""
        else:
            header = self.top_bar * 10 + "\n"
        header += f"#{'#'*self.depth_in_page} {self.title}\n\n"
        
        text = None
        
        if not self.ignore_if_empty:
            text = header
            
        if self.comment is not None:
            if text is None:
                text = header + self.comment
            else:
                text += self.comment
                
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
    
    def get_documentation(self, doc_folder=None):
        """ Write the section into a dict
        
        Arguments
        ---------
        - doc (dict) : the dict where to write the documentation        
        """
        
        doc = {}
        if doc_folder is not None:
            doc_folder = Path(doc_folder)
        
        def create_file(section):
            if not section.is_page:
                return
            
            text = section.get_content()
            if text is not None:
                file_name = section.file_name
                assert(file_name not in doc)
                doc[file_name] = text
                
                if doc_folder is not None:
                    with (doc_folder / str(file_name)[1:]).open(mode='w') as f:
                        f.write(text)
                
        self.iteration(create_file)
        
        return doc
    
    # =============================================================================================================================
    # Add dict description (structure returned by code parsing)
    
    # -----------------------------------------------------------------------------------------------------------------------------
    # Add a file
    
    def add_file_dict(self, file_dict):
        
        assert(file_dict['obj'] == 'file')
        
        #page = self.add_page(struct['name'], comment=struct['comment'], in_toc=True)
        
        # ---- Two main sections
        
        functions = self.get_create_section('Functions', sort_sections=True)
        classes   = self.get_create_section('Classes',   sort_sections=True)
        
        # ----- Loop on the file content
            
        for obj in file_dict['subs'].values():

            if obj.get('hidden', False):
                continue
            
            if obj['obj'] == 'function':
                functions.add_function_dict(obj)
                
            elif obj['obj'] == 'class':
                classes.add_class_dict(obj)
                
            else:
                assert(False)
                    
                #toc_items.append((obj_section.title, f"[{obj_section.title}](#{obj_section.anchor})"))
                    
            # ----- Format the page
                    
            #functions.sort(key=lambda s: s.title)
            #classes.sort(key=lambda s: s.title)
            
            #section.insert(0, Section.Toc(toc_items, 'Content'))    
            
    # -----------------------------------------------------------------------------------------------------------------------------
    # Add a class
    
    def add_class_dict(self, class_dict, ignore_uncommented=False):
        
        assert(class_dict['obj'] == 'class')
        
        # ----- Page dedicated to the class
        
        page = self.add_page(class_dict['name'], comment=class_dict['comment'], in_toc=True)
            
        properties = page.add_section('Properties', sort_sections=True)
        methods    = page.add_section('Methods',    sort_sections=True)
        
        if class_dict.get('__init__') is not None:
            if class_dict.get('args') is not None:
                page.write_source(f"{page.title}({class_dict['args']})")
            
            #if struct['__init__']['comment'] is not None:
            #    init_ = Section.FromParsed(struct['__init__'])
            #    class_page.write("\n\n**__init__**\n\n")
            #    class_page.write(init_.comment)
            
        # ----- Loop on properties and methods 
        
        for obj in class_dict['subs'].values():
            
            if obj.get('hidden', False):
                continue
            
            if obj['obj'] == 'property':
                properties.add_property_dict(obj)
                
            elif obj['obj'] == 'function':
                methods.add_function_dict(obj)
                
            else:
                assert(False)
                
            #toc_items.append((obj_section.title, f"[{obj_section.title}](#{obj_section.anchor})"))

        # ----- Format the page
                
        #properties.sort(key=lambda s: s.title)
        #methods.sort(key=lambda s: s.title)
        
        #section.insert(0, Section.Toc(toc_items, 'Content'))
        
    # -----------------------------------------------------------------------------------------------------------------------------
    # Add a property
    
    def add_property_dict(self, prop_dict):
        
        assert(prop_dict['obj'] == 'property')
        
        section = self.add_section(prop_dict['name'], prop_dict['comment'], in_toc=True, top_bar='-')
        
        sepa = '\n\n'
        
        if prop_dict.get('getter') is not None or prop_dict.get('setter') is not None:
            section.write(f"{sepa}- {'getter' if prop_dict.get('getter') is not None else ''} {'setter' if prop_dict.get('setter') is not None else ''}")
            sepa = '\n'
            
        if prop_dict.get('type') is not None:
            section.write(f"{sepa}- type **{prop_dict['type']}**")
            sepa = '\n'
            
        if prop_dict.get('default') is not None:
            section.write(f"{sepa}- default {prop_dict['default']}")
            sepa = '\n'
            
        section.write(sepa)
        
        section.write_navigation()

        #if prop_dict.get('getter') is not None:
        #    section.add_function_dict(prop_dict['getter'])
            
        #if prop_dict.get('setter') is not None:
        #    section.add_function_dict(prop_dict['setter'])
                

    # ----------------------------------------------------------------------------------------------------
    # Function / Method
    
    def add_function_dict(self, func_dict):
    
        assert(func_dict['obj'] == 'function')
        
        section = self.add_section(func_dict['name'], func_dict['comment'], in_toc=True, top_bar='-')
        
        if func_dict.get('args') is not None:
            section.write_source(f"{section.title}({func_dict['args']})")
        
        if len(func_dict['raises']):
            sub = section.add_section('Raises', "\n- ".join([format_list_line(d) for d in func_dict['raises']]))
                                  
        if len(func_dict['arguments']):
            sub = section.add_section('Arguments', "\n- ".join([format_list_line(d) for d in func_dict['arguments']]))
                                  
        if len(func_dict['returns']):
            sub = section.add_section('Returns', "\n- ".join([format_list_line(d) for d in func_dict['returns']]))
                                      
    
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
        
        
    @staticmethod
    def test_self():
        
        proj = Section("Documentation")
        folder = Path(__file__).parents[0]
        print(str(folder))
        
        text = parse_file_source(Path(__file__).read_text())
        
        proj.add_file_dict(text)
        
        #proj.dump()
        
        #proj.print()
        
        proj.get_documentation(folder / "testdoc")
        
                    
Section.test_self()
                
