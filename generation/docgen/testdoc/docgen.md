# docgen

Markdown python documentation generator

Generate documentation for python project based on the source file.


## Content

[Argument](#argument)
- [Class](#class)
- [Function](#function)
- [Project](#project)
- [Return](#return)
- [Section](#section)
- [parse_comment](#parse_comment)

## Functions

### parse_comment

Function comment parser

The Function parser extracts Properties, Arguments and Returns sections.
The corresponding lines are removed to build the 'new_comment' text.

The lists are generated from the structure

``` python
parse_comment(comment)
```



#### Arguments

- **comment** (str) : the raw comment

#### Returns

- **dict** : {'new_comment', 'properties', 'arguments', 'returns', 'raises'}

## Classes

### Argument

Function argument

Yield a line for argument documentation:
```
- name (type = default) : description
```

#### Content

[build](#build)

#### Properties

#### Methods



``` python
Argument(name, type=None, default=None, description=None)
```



##### build

Yield line argument

``` python
build()
```



###### Returns

- **str** : formatted argument line

### Class

Section documenting a class

The structure of the document is:
- title (class name)
- header comment
- properties & methods table of contents
- Properties section with the documented properties as sub sections
- Methods section withe the documented methods as sub sections

The class documentation is completed afterward by the [compile](#compile) method
which get the links coming from inheritance between classes.


Arguments
---------
- class_name (str) : class name
- comment (str) : header comment

#### Content

[FromDoc](#fromdoc)
- [bases](#bases)
- [build](#build)
- [capture_class](#capture_class)
- [compile](#compile)
- [inherited](#inherited)
- [methods](#methods)
- [properties](#properties)
- [subclasses](#subclasses)

#### Properties

##### bases

name of the base classes> type list of str


##### inherited

properties and methods inherited from base classes> type list of str


##### methods

Methods Section> type Section


###### Getter

Methods Section

``` python
methods()
```



####### Returns

- **Section** : title is 'Methods', sub sections are documented methods

##### properties

Properties Section> type Section


###### Getter

Properties Section

``` python
properties()
```



####### Returns

- **Section** : title is 'Properties', sub sections are documented properties

##### subclasses

name of the sub classes> type list of str


#### Methods

##### FromDoc

Creates a Class document from a Doc parsed from source file

The **doc** argument contains the list of documents methods and properties.

``` python
FromDoc(doc, ignore_uncommented=True, **kwargs)
```



###### Arguments

- **doc** (Doc) : Doc parsed from a sourc file
- - **exclude_uncommented** (_bool_ = True) : exclude the methods which are not commented in the source file

###### Returns

- **Class** : document on the class

##### build

Yield the Class documentation lines

``` python
build()
```



##### capture_class

Capture methods and properties from another Class

This method allows to get the documentation of inherited items of a class
which is not documentated.

``` python
capture_class(other, with_comment=False)
```



###### Arguments

- **other** (Class) : class to copy methods and properties from

###### Returns

- **self** : 

##### compile

Compile the class

**project** refers to the global [LINK ERROR: page 'Project' not found]() documentation.

Class compilation is:
- Load each class based on this one into to the **subclasses** attribute.
- Load the methods and properties inherited from parent classes

``` python
compile(project)
```



###### Arguments

- **project** ([LINK ERROR: page 'Project' not found]()) : main project

###### Returns

- **self** : 

### Function

Section dedicated to function documentation.

The comment can contain description of Arguments and Returns.
The comment is parsed in order to extract this information and to
write the document is a homogeneous way.

Arguments
---------
- name (str) : function or method name
- comment (str = None) : header comment
- level (int = 1) : indentation level

#### Content

[FromDoc](#fromdoc)
- [arguments](#arguments)
- [init](#init)
- [parse_comment](#parse_comment)
- [returns](#returns)

#### Properties

##### arguments

Arguments Section> type Section


###### Getter

Arguments Section

``` python
arguments()
```



####### Returns

- **Section** : title is 'Arguments', sub sections are [Argument](#argument)

##### returns

Arguments Section> type Section


###### Getter

Arguments Section

``` python
returns()
```



####### Returns

- **Section** : title is 'Arguments', sub sections are [Return](#return)

#### Methods

##### FromDoc

Create a class from an instance of Doc

Doc is a class read by the **Parser**.

``` python
FromDoc(doc, class_name=None, **kwargs)
```



###### Arguments

- **doc** (Doc) : Doc parsed by **Parser**

##### init

Function section specific init

A Function section is made of two sections:
- Arguments
- Returns

It also create stores other information:
- decorators
- arguments

``` python
init()
```



##### parse_comment

Function comment parser

The Function parser extracts Properties, Arguments and Returns sections.
The corresponding lines are remove from the comment to feed the two sections.

The lists are generated from the structure

``` python
parse_comment(comment)
```



### Project

Project documentation

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

The parsed source code is stored in [LINK ERROR: page '' not found]() dictionary with one entry per parsed file.
The parsed source contain classes and function documentation which can be transfered
into pages.

When transferring, a class can be enriched with other classed, either to specify
inherited methods and properties or to complement the documentation with inheritance.
See [LINK ERROR: page '' not found]().

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
- refdocs (dict of [LINK ERROR: page 'Section' not found]()) : reference documentation loaded from source file
- pages (dict of [LINK ERROR: page 'Section' not found]()) : the pages to create in the final documentation
- sections (list of [LINK ERROR: page 'Section' not found]()) : dictionary of documented items

#### Content

[add_class](#add_class)
- [add_function](#add_function)
- [add_page](#add_page)
- [add_source](#add_source)
- [create_index_file](#create_index_file)
- [get_refdoc](#get_refdoc)
- [load_files](#load_files)
- [new_page](#new_page)
- [set_hook](#set_hook)

#### Properties

#### Methods



``` python
Project(title, comment=None, toc="174")
```



##### add_class

Copy class documentation from reference documentation to pages

The class must exist in one of the reference documentation [LINK ERROR: page '' not found]().

The class documentation is completed with **bases** and **capture** arguments.

> Explicit inheritance with **bases**
> _class_name_ : inherits from base_class
> inherited methods : **method1**, **method2**

> Hidden inheritance with **capture**
> _class_name_
> methods : **method1**, **method2**

Once completed, the class is registered in [LINK ERROR: page '' not found]() and placed in the page.

if **page** is None, the resulting [LINK ERROR: page 'Class' not found]() is considered as a page and
added to [LINK ERROR: page '' not found](). If **page** is not None, the class documentation
is appended to it.

> [!NOTE]
> The page where the class is documented can be retreived with attribute [LINK ERROR: page 'Section' not found]().

``` python
add_class(class_name, page=None, bases=[], capture=[], file_key=None)
```



###### Arguments

- **class_name** (str) : class name
- - **page** (_[LINK ERROR: page 'Section' not found]() or str_ = None) : name of the page where to include the class documentation
- - **bases** (_list of strs_ = []) : list of base classes
- - **capture** (_list of strs or [LINK ERROR: page 'Class' not found]()_ = []) : list of classes to copy methods and properties from
- - **file_key** (_str_ = None) : file key in [LINK ERROR: page '' not found]()

###### Returns

- **Class** : created class

##### add_function

Copy function documentation reference documentation to pages.

The function must exist in one of the reference documentation [LINK ERROR: page '' not found]().

Once completed, the function is registered in [LINK ERROR: page '' not found]() and placed in the page.

if **page** is None, the resulting [LINK ERROR: page 'Function' not found]() is considered as a page and
added to [LINK ERROR: page '' not found](). If **page** is not None, the class documentation
is appended to it.

> [!NOTE]
> The page where the class is documented can be retrieved with attribute [LINK ERROR: page 'Section' not found]().

``` python
add_function(function_name, page=None, file_key=None, function_key=None, exact=True, only_commented=True, sub_level=1)
```



###### Arguments

- **function_name** (str) : class name
- - **page** (_[LINK ERROR: page 'Section' not found]() or str_ = None) : name of the page where to include the class documentation
- - **file_key** (_str_ = None) : file key in [LINK ERROR: page '' not found]()
- - **function_key** (_str_ = None) : key of the function in [LINK ERROR: page '' not found]()
- - **exact** (_bool_ = True) : use exact name if True, regular expression otherwise
- - **only_commented** (_bool_ = True) : don't include uncommented functions
- - **sub_level** (_int_ = 1) : incrementation level to page.level

###### Returns

- **Function** : created class

##### add_page

Add a page in the documentation

``` python
add_page(page)
```



###### Arguments

- **page** ([LINK ERROR: page 'Section' not found]()) : the page to add

###### Returns

- **Section** : the argument **page**

##### add_source

Add a source code.

The source code is parsed and the resulting [LINK ERROR: page 'Section' not found]() is stored in the [LINK ERROR: page '' not found]() dict.

``` python
add_source(key, text)
```



###### Arguments

- **key** (str) : source file key
- - **text** (str) : the source code

###### Returns

- **Section** : 

##### create_index_file

Create the index file

``` python
create_index_file(file_name)
```



###### Arguments

- **file_name** (str) : file name to write

##### get_refdoc

Get a reference documentation from the base

If **key** argument is None, the **name** is searched in the whole dictionary,
otherwise the search is performed only in the specified key.

If **exact** is False, name is considered as a regular expression.
All the title matching this expression is returned in a list.

``` python
get_refdoc(name, key=None, exact=True, halt=True)
```



###### Arguments

- **name** (str) : title of the reference documentation
- - **key** (_str_ = None) : source file key
- - **exact** (_bool_ = True) : use exact name if True, regular expression otherwise
- - **halt** (_bool_ = True) : raise an exception if not found

###### Returns

- **Section** : found section if exact is True, list of sections otherwise

##### load_files

Enrich the reference doc by parsing source files.

All the files with `.py` extension are parsed.

``` python
load_files(folder=None, sub_folders=[], key=None)
```



###### Arguments

- **folder** (str) : main folder
- - **sub_folders** (str) : sub folders to explore
- - **key** (_str_ = None) : 

###### Returns

- **self** : 

##### new_page

Add a page in the documentation

> [!CAUTION]
> **title** argument is used a as key in [LINK ERROR: page '' not found]() dictionary. It must be unique
> in the scope of the project

``` python
new_page(title, comment=None, toc=None, in_toc=True)
```



###### Arguments

- **title** (str) : page title
- - **comment** (str) : comment
- - **toc** (_str_ = None) : title of the content section, None if no content section is required
- - **in_toc** (_bool_ = True) : include the the documentation table of content

###### Returns

- **Page** : 

##### set_hook

Replace a regular expression by as substitution string

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
> syntax : `<!Section title#Sub section title>` which is converted in [LINK ERROR: page 'Project' not found]().

``` python
set_hook(expr, repl)
```



###### Arguments

- **expr** (str) : RegEx expression - repl (str or function) : replacement string or function

### Return

Function returns

Yield a line for return documentation:
```
- name  : description
```

#### Content

[build](#build)

#### Properties

#### Methods



``` python
Return(name, description=None)
```



##### build

Yield line return

``` python
build()
```



###### Returns

- **str** : formatted return line

### Section

Elementary base of a documentation

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
- page ([LINK ERROR: page 'Section' not found]()) : the page where this section will appear

#### Content


- F[FromSource](#fromsource)
- a[as_dict](#as_dict) [alphabetical_sections](#alphabetical_sections)
- b[build_header](#build_header) [build_sections](#build_sections) [build_extra](#build_extra) [build](#build)
- c[comment](#comment)
- g[get_section](#get_section)
- i[init](#init) [iteration](#iteration)
- l[level](#level) [link_token](#link_token) [link_to](#link_to)
- m[md_file_name](#md_file_name)
- n[new_section](#new_section)
- p[parse_comment](#parse_comment) [print](#print)
- s[sorted_sections](#sorted_sections)
- w[write_header](#write_header) [write](#write)

#### Properties

##### as_dict

Return as a dictionary> type dict


###### Getter

Return as a dictionary

``` python
as_dict()
```



####### Returns

- **dict** : section title: section

##### comment

Comment property> type str


###### Getter

Comment property

``` python
comment()
```



####### Returns

- **str** : Section header comment

###### Setter



``` python
comment(value)
```



##### level

Indentation level

When set, the sub sections levels are set with the passed value plus 1.> type int


###### Getter

Indentation level

When set, the sub sections levels are set with the passed value plus 1.

``` python
level()
```



####### Returns

- **int** : 

###### Setter



``` python
level(value)
```



##### link_token

MD link token

The markdown token is the lower case title where spaces are replaces by '-' char> type str


###### Getter

MD link token

The markdown token is the lower case title where spaces are replaces by '-' char

``` python
link_token()
```



####### Returns

- **str** : markdown token

##### md_file_name

MD Document file name> type str


###### Getter

MD Document file name

``` python
md_file_name()
```



####### Returns

- **str** : markdown file name

##### sorted_sections

Sort the sub sections in alphabetical order> type List


###### Getter

Sort the sub sections in alphabetical order

``` python
sorted_sections()
```



####### Returns

- **List** : list of the sub sections sorted in alphabetical order

#### Methods



``` python
Section(title, comment=None, level=0, **kwargs)
```



##### FromSource

Get the content from a source file.

The source is parsed and a [LINK ERROR: page 'Section' not found]() is added for each class and global function.

``` python
FromSource(name, text)
```



###### Arguments

- **text** (str) : source code to parse

###### Returns

- **Section** : 

##### alphabetical_sections

Build a dictionary keyed by the section title initials

Used to diplay a table of content when there is a great number of sections.

```
{'A': ['a section', 'another section',
 'O': ['other section']
 }
```

``` python
alphabetical_sections(alpha=None)
```



###### Arguments

- **alpha** (_dict_ = None) : dictionary to feed

###### Returns

- **dict** : 

##### build

Yield the lines of the section

The method yields the lines from method **build_header** and the from
**build_sections**.

If the flag **with_sections_only** is set, nothing is yield if there is no
sub sections.

``` python
build()
```



###### Returns

- **str** : documentation lines for the sections

##### build_extra

Yield extra lines at the end of the section documentation

``` python
build_extra()
```



##### build_header

Yield the lines of the header part

``` python
build_header()
```



##### build_sections

Yield the lines of the sections parts

``` python
build_sections()
```



##### get_section

Look for a sub section by its title

> [!NOTE]
> This function searches only in the direct children, not in the whole tree.

To search a section in the whole tree, use [LINK ERROR: page '' not found]() method:

``` python
sub_section = parent_section.iteration(lambda s: s.title == 'The title')
```

``` python
get_section(title)
```



###### Arguments

- **title** (str) : the section to look for

###### Returns

- **Section** : 

##### init

Class initialisation

This complementary initialisation takes place at the end of **__init__**, before
[parse_comment](#parse_comment) is called.

Allows to initialize attributes which are used in [parse_comment](#parse_comment) method.

Default method is empty.

``` python
init()
```



##### iteration

Run the function on the section and sub sections

The method halts on the first section for which the function
return `True` and returns this section.
If the function doesn't return `True`, the methods is run on all sections
and return `None`.

``` python
iteration(f)
```



###### Arguments

- **f** (function of template f(section)) : the function to run

###### Returns

- **Section** : 

##### link_to

MD link

``` python
link_to(url="57")
```



###### Returns

- **str** : [title](url + link_token)

##### new_section

Add a sub section

``` python
new_section(title, comment=None, sub_level=1)
```



###### Arguments

- **title** (str) : section title
- - **comment** (str) : header comment
- - **sub_level** (_int_ = 1) : level increment

###### Returns

- **Section** : 

##### parse_comment

Parse comment to extract information

This method extract information embbeded in the comment and returns the cleaned text.
The default implementation normalizes the markdwon comment.

``` python
parse_comment(comment)
```



###### Arguments

- **comment** (str) : the raw comment

###### Returns

- **str** : the cleaned comment

##### print

Print the documentation in the console

For debug purpose.

``` python
print()
```



##### write

Append text to the current text

The current text is either the comment if this section if there is not sub sections,
or the comment of the last sub sections.

``` python
write(comment="52", parse=True)
```



###### Arguments

- **comment** (str) : the text to write
- - **parse** (_bool_ = True) : parse the comment

##### write_header

Append text to the header comment

``` python
write_header(comment="51", parse=True)
```



###### Arguments

- **comment** (str) : the text to write
- - **parse** (_bool_ = True) : parse the comment

