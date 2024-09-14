#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 07:41:35 2024

@author: alain


$ DOC START

This module generates a simple but yet acceptable project documentation package
for a python package.

Documentation files are generated in markdown format which can be used on GitHub.

The documentation is generated in 3 majors steps:
1. Loading descriptors
2. Setting up the documentation structure
3. Creating the files

## Loading descriptors

Descriptors are dictionaries giving informations on each element to document such as
files, classes, functions, properties...

Descriptors can come from 3 sources:
- by parsing source files
- by getting description from python inspect module (future dev)
- by manually creating python objects descriptors

> [!NOTE]
> The capability to build descriptors directly by parsing source files
  avoids to have to import the modules in main program
  
Some changes can be made before passing to the next step.

## Setting up the documentation structure

Use select which descriptors must be part of the documentation.

## Creating the files

Documentation files are created

## Example

The piece of code below gives the structure of building a documentation package:

  
``` python

# Initialize the documentation

doc = Documentation("Project documentation", doc_folder="/Documentation/Folder", source_folder="python/project/demo")

# STEP 1 : Load source files relatively to source_folder

doc.load_folder(".")
doc.load_folder("core")

# STEP 2 : documentation structure

doc.document_folder('.')
doc.document_folder('core')

# STEP 3 : create the documentation files

doc.get_documentation()
```

$ DOC STOP

This is not displayed

"""


