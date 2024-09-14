# Documentation Generator


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



## Content


- C : [capture_inheritance](#capture_inheritance) :black_small_square: [capture_inheritances](#capture_inheritances) :black_small_square: [clean_python](#clean_python)
- D : [Documentation](documentation.md#documentation) :black_small_square: [del_margin](#del_margin) :black_small_square: [dump_dict](#dump_dict)
- E : [extract_lists](#extract_lists) :black_small_square: [extract_source](#extract_source) :black_small_square: [extract_strings](#extract_strings)
- F : [format_list_line](#format_list_line)
- N : [new_class](#new_class) :black_small_square: [new_file](#new_file) :black_small_square: [new_function](#new_function) :black_small_square: [new_property](#new_property) :black_small_square: [new_struct](#new_struct)
- P : [parse_file_source](#parse_file_source) :black_small_square: [parse_files](#parse_files) :black_small_square: [parse_list_line](#parse_list_line) :black_small_square: [parse_meta_comment](#parse_meta_comment)
- R : [replace_source](#replace_source) :black_small_square: [replace_strings](#replace_strings)
- S : [Section](section.md#section) :black_small_square: [struct_iter](#struct_iter) :black_small_square: [struct_list](#struct_list) :black_small_square: [struct_search](#struct_search)
- T : [Text](text.md#text) :black_small_square: [test](#test) :black_small_square: [test_folder](#test_folder) :black_small_square: [title_to_anchor](#title_to_anchor) :black_small_square: [title_to_file_name](#title_to_file_name)



## Functions

----------
### capture_inheritance

Capture properties et methods from another class

Allow to document class items as it were not inherited.

> [!Note]
> if the name of the base class is in the inherits list, it is removed from it

``` python
capture_inheritance(class_, base_, remove=True)
```



#### Arguments

- **class_** (dict) : the class to enrich
- - **base_** (dict) : the class to capture properties and methods from
- - **remove** (_bool_ = True) : remove base name from inheritance list



<sub>[top](#documentation-generator) [index](index.md)</sub>



----------
### capture_inheritances

Capture inheritances

Allow to document class items as it were not inherited.

> [!Note]
> if the name of the base class is in the inherits list, it is removed from it

``` python
capture_inheritances(class_, files_, include=None, exclude=[], verbose=True)
```



#### Arguments

- **class_** (dict) : the class to enrich
- - **files_** (dict) : the hierarchy containing base classes to capture from
- - **include** (_list_ = None) : limit capture to the given list
- - **exclude** (_list_ = []) : exclude classes in the given list



<sub>[top](#documentation-generator) [index](index.md)</sub>



----------
### clean_python

Clean python source code

- Replace the comments by an comment index
- Replace the strings by an index
- Remove the blank lines
- Group multilines instructions between ( and )

Comments and strings are store in lists.
Comments are replaced by <COMMENT index> and strings by "index"

``` python
clean_python(text)
```



#### Arguments

- **text** (str) : source code to clean



#### Returns

- **str** : cleaned text
- - **list** : list of comments
- - **list** : list of strings



<sub>[top](#documentation-generator) [index](index.md)</sub>



----------
### del_margin

Move lines leftwards to suppress margin.

Comment read in source code can have a non nul left margin whcih is interprated in markdown.
This method:
- suppresses the margin of the first line
- move leftwards the lines after in order that the leftmost line has no margin and
  that the relative indentation remains the same

The following text:
|     Example of text
|               This text is aligned
|               with a margin:
|               - because it is written as a multiline comment string
|                 with indentation
|               Text continues here

Is realigned:
| Example of text
| This texte is aligned
| with a margin:
| - because it is written as a multiline comment string
|   with indentation
| Text continues here

``` python
del_margin(comment)
```



#### Arguments

- **comment** (str) : the comment



#### Returns

- **str** : the realigned comment



<sub>[top](#documentation-generator) [index](index.md)</sub>



----------
### dump_dict



``` python
dump_dict(d, indent=0)
```



<sub>[top](#documentation-generator) [index](index.md)</sub>



----------
### extract_lists

Extract lists from a comment.

This parser extracts Properties, Arguments and Returns sections.
The corresponding lines are removed to build the 'new_comment' text.

The lists are generated from the structure

``` python
extract_lists(comment, titles)
```



#### Arguments

- **comment** (str) : the raw comment
- - **titles** (str or list of strs) : the titles of the lists to extract



#### Returns

- **str** : comment without the lists, lists as dict



<sub>[top](#documentation-generator) [index](index.md)</sub>



----------
### extract_source

Replace source code block by an index.

This pretreatment ensure that the content of sourcode won't interfer with
regular expression

``` python
extract_source(text)
```



#### Arguments

- **text** (str) : text to extract source code from



#### Returns

- **str** : cleaned text and list of extracted pieces of code



<sub>[top](#documentation-generator) [index](index.md)</sub>



----------
### extract_strings

Replace string by an index.

This pretreatment ensure that the content of strings won't interfer with
regular expression

``` python
extract_strings(text)
```



#### Arguments

- **text** (str) : text to extract strings from



#### Returns

- **str** : cleaned text and list of extracted strings



<sub>[top](#documentation-generator) [index](index.md)</sub>



----------
### format_list_line



``` python
format_list_line(d)
```



<sub>[top](#documentation-generator) [index](index.md)</sub>



----------
### new_class



``` python
new_class(name, comment=None, subs=None, inherits=None)
```



<sub>[top](#documentation-generator) [index](index.md)</sub>



----------
### new_file



``` python
new_file(name, comment=None, subs=None)
```



<sub>[top](#documentation-generator) [index](index.md)</sub>



----------
### new_function



``` python
new_function(name, comment=None, decorators=None, args=None, arguments=None, raises=None, returns=None)
```



<sub>[top](#documentation-generator) [index](index.md)</sub>



----------
### new_property



``` python
new_property(name, comment=None, type=None, default=None, setter=None, getter=None)
```



<sub>[top](#documentation-generator) [index](index.md)</sub>



----------
### new_struct



``` python
new_struct(obj, name, comment=None, subs=None, **kwargs)
```



<sub>[top](#documentation-generator) [index](index.md)</sub>



----------
### parse_file_source

Parse a python file source

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

``` python
parse_file_source(text, file_name="134")
```



#### Arguments

- **text** (str) : source code to parse



#### Returns

- **dict** : classes and functions



<sub>[top](#documentation-generator) [index](index.md)</sub>



----------
### parse_files

Load files from a folder.

All the files with `.py` extension are parsed.

``` python
parse_files(folder, key="191", verbose=False)
```



#### Arguments

- **folder** (str) : main folder
- - **root** (_str_ = None) : 



#### Returns

- **dict** : 



<sub>[top](#documentation-generator) [index](index.md)</sub>



----------
### parse_list_line

Parse a list line in a comment

syntax:
- name (type = default) : description

Default value could contain parenthesis as in `Vector = (1, 2, 3)`,
the parsing is done by reading the line char per char to handle
parenthesis nesting.

``` python
line = "- text (str = None) : text to parse"
pprint(parse_list_line(line))
# > {'default': 'None',
# > 'description': 'text to parse',
# > 'name': 'text',
# > 'obj' : 'str'}
```

``` python
parse_list_line(line)
```



<sub>[top](#documentation-generator) [index](index.md)</sub>



----------
### parse_meta_comment

Parse the comment itsel to extract meta tags

Tags are `$` starting at the beginin of the line followed by a command line:
    
- DOC START : extract comment from here
- DOC END : don't extract after after
- SET property value : property value pair

``` python
parse_meta_comment(comment)
```



<sub>[top](#documentation-generator) [index](index.md)</sub>



----------
### replace_source

Replace the extracted strings.

``` python
replace_source(text, strings)
```



#### Arguments

- **text** (str) : text with replaced pieces of code
- - **strings** : list of pieces of code



#### Returns

- **Text** : 



<sub>[top](#documentation-generator) [index](index.md)</sub>



----------
### replace_strings

Replace the extracted strings.

``` python
replace_strings(text, strings)
```



#### Arguments

- **text** (str) : text with replaced strings
- - **strings** : list of strings



#### Returns

- **Text** : 



<sub>[top](#documentation-generator) [index](index.md)</sub>



----------
### struct_iter



``` python
struct_iter(struct, f, *args, **kwargs)
```



<sub>[top](#documentation-generator) [index](index.md)</sub>



----------
### struct_list



``` python
struct_list(struct, name_only=True, **kwargs)
```



<sub>[top](#documentation-generator) [index](index.md)</sub>



----------
### struct_search



``` python
struct_search(struct, **kwargs)
```



<sub>[top](#documentation-generator) [index](index.md)</sub>



----------
### test



``` python
test()
```



<sub>[top](#documentation-generator) [index](index.md)</sub>



----------
### test_folder



``` python
test_folder(folder=None, sub_folders=[])
```



<sub>[top](#documentation-generator) [index](index.md)</sub>



----------
### title_to_anchor



``` python
title_to_anchor(title)
```



<sub>[top](#documentation-generator) [index](index.md)</sub>



----------
### title_to_file_name



``` python
title_to_file_name(title)
```



<sub>[top](#documentation-generator) [index](index.md)</sub>

