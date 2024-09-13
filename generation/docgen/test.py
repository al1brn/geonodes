#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 08:33:58 2024

@author: alain
"""

def title_to_file_name(title):
    return f"{title.lower().replace(' ', '_')}.md"

def title_to_anchor(title):
    return title.lower().replace(' ', '-')


class Section:
    
    def __init__(self, title, comment=None, sort_sections=False, in_toc=False, module=None, is_page=False, ignore_if_empty=True):
        """ Section
        
        
        Properties
        ----------
        - is_page (bool = False) : is a page if <#module> is not None
        - module (string = None) : module the page belongs to, section is not a page if None
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
        
    def __str__(self):
        stype   = "P" if self.is_page else "S"
        if self.is_module:
            stype = "M"
        if self.is_top:
            stype = "T"
        shidden = "H" if self.hidden  else "D"
            
        return f"<{stype} {self.depth} {self.depth_in_page} {shidden} [{self.module}] {self.title}>"
        
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
    
    def dump(self):

        def func(sct):
            print(f"{'   '*sct.depth_in_page}- {sct.title}")

        self.iteration(func)
    
    # =============================================================================================================================
    # Properties
    
    # -----------------------------------------------------------------------------------------------------------------------------
    # Hierarchy
    
    @property
    def is_top(self):
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
    def has_content(self):

        if not self.ignore_if_empty:
            return True
        
        if self.comment is not None:
            return True
        
        for section in self.children:
            if section.is_page:
                continue
            
            if not section.hidden:
                return True
            
        return False
    
    @property
    def hidden(self):
        return not self.has_content
            
    # -----------------------------------------------------------------------------------------------------------------------------
    # file name / anchor

    @property
    def file_name(self):
        if self.is_page:
            module_path = self.module_path
            if module_path != '':
                module_path += '-'
            return '//' + module_path + title_to_file_name(self.title)
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
    
    # =============================================================================================================================
    # dev and test
    
    def dump_struct(self, title='Section dump'):
        print(title)
        print('-'*50)
        def func(section):
            print(str(section), section.anchor)
            
        self.iteration(func)
        print()
    
    @classmethod
    def TestStructure(cls):
        
        top = Section("Top")
        page = top.add_section("Top section")
        page = top.add_section("Top section")

        module = top.add_module("M1", "Module 1")
        module.add_section("M1 Section")
        module.add_section("M1 Section")
        
        module = top.add_module("M2", "Module 2")
        module.add_section("M2 Section")
        module.add_section("M2 Section")
        
        submodule = module.add_module("M21", "Section 1")
        submodule.add_page("Far page").add_section("Far section")
        
        page = module.add_page("Page 1")
        page = module.add_page("Page 2")
        
        
        return top


top = Section.TestStructure()
top.dump_struct() 
            
        
        
