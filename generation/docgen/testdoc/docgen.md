<h1 id="docgen">docgen</h1>Markdown python documentation generator

Generate documentation for python project based on the source file.


<h2 id="functions">Functions</h2><h3 id="parse_comment">parse_comment</h3>Function comment parser

The Function parser extracts Properties, Arguments and Returns sections.
The corresponding lines are removed to build the 'new_comment' text.

The lists are generated from the structure

``` python
parse_comment(comment)
```



<h4 id="arguments">Arguments</h4>- **comment** (str) : the raw comment

<h4 id="returns">Returns</h4>- **dict** : {'new_comment', 'properties', 'arguments', 'returns', 'raises'}

<h2 id="classes">Classes</h2><h3 id="section">Section</h3>Elementary base of a documentation

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

<h4 id="properties">Properties</h4><h5 id="as_dict">as_dict</h5>Return as a dictionary> type dict


<h6 id="getter">Getter</h6>Return as a dictionary

``` python
as_dict()
```



<h7 id="returns-1">Returns</h7>- **dict** : section title: section

<h5 id="comment">comment</h5>Comment property> type str


<h6 id="getter-1">Getter</h6>Comment property

``` python
comment()
```



<h7 id="returns-2">Returns</h7>- **str** : Section header comment

<h6 id="setter">Setter</h6>

``` python
comment(value)
```



<h5 id="level">level</h5>Indentation level

When set, the sub sections levels are set with the passed value plus 1.> type int


<h6 id="getter-2">Getter</h6>Indentation level

When set, the sub sections levels are set with the passed value plus 1.

``` python
level()
```



<h7 id="returns-3">Returns</h7>- **int** : 


<h6 id="setter-1">Setter</h6>

``` python
level(value)
```



<h5 id="md_file_name">md_file_name</h5>MD Document file name> type str


<h6 id="getter-3">Getter</h6>MD Document file name

``` python
md_file_name()
```



<h7 id="returns-4">Returns</h7>- **str** : markdown file name

<h5 id="link_token">link_token</h5>MD link token

The markdown token is the lower case title where spaces are replaces by '-' char> type str


<h6 id="getter-4">Getter</h6>MD link token

The markdown token is the lower case title where spaces are replaces by '-' char

``` python
link_token()
```



<h7 id="returns-5">Returns</h7>- **str** : markdown token

<h5 id="sorted_sections">sorted_sections</h5>Sort the sub sections in alphabetical order> type List


<h6 id="getter-5">Getter</h6>Sort the sub sections in alphabetical order

``` python
sorted_sections()
```



<h7 id="returns-6">Returns</h7>- **List** : list of the sub sections sorted in alphabetical order

<h4 id="methods">Methods</h4>

``` python
Section(title, comment=None, level=0, **kwargs)
```



#### __init__



<h5 id="fromsource">FromSource</h5>Get the content from a source file.

The source is parsed and a [LINK ERROR: page 'Section' not found]() is added for each class and global function.

``` python
FromSource(name, text)
```



<h6 id="arguments-1">Arguments</h6>- **text** (str) : source code to parse

<h6 id="returns-7">Returns</h6>- **Section** : 


<h5 id="init">init</h5>Class initialisation

This complementary initialisation takes place at the end of **__init__**, before
[parse_comment](#parse_comment) is called.

Allows to initialize attributes which are used in [parse_comment](#parse_comment) method.

Default method is empty.

``` python
init()
```



<h5 id="iteration">iteration</h5>Run the function on the section and sub sections

The method halts on the first section for which the function
return `True` and returns this section.
If the function doesn't return `True`, the methods is run on all sections
and return `None`.

``` python
iteration(f)
```



<h6 id="arguments-2">Arguments</h6>- **f** (function of template f(section)) : the function to run

<h6 id="returns-8">Returns</h6>- **Section** :  or None


<h5 id="parse_comment-1">parse_comment</h5>Parse comment to extract information

This method extract information embbeded in the comment and returns the cleaned text.
The default implementation normalizes the markdwon comment.

``` python
parse_comment(comment)
```



<h6 id="arguments-3">Arguments</h6>- **comment** (str) : the raw comment

<h6 id="returns-9">Returns</h6>- **str** : the cleaned comment

<h5 id="new_section">new_section</h5>Add a sub section

``` python
new_section(title, comment=None, sub_level=1)
```



<h6 id="arguments-4">Arguments</h6>- **title** (str) : section title
- - **comment** (str) : header comment
- - **sub_level** (_int_ = 1) : level increment

<h6 id="returns-10">Returns</h6>- **Section** : 


<h5 id="write_header">write_header</h5>Append text to the header comment

``` python
write_header(comment="51", parse=True)
```



<h6 id="arguments-5">Arguments</h6>- **comment** (str) : the text to write
- - **parse** (_bool_ = True) : parse the comment

<h5 id="write">write</h5>Append text to the current text

The current text is either the comment if this section if there is not sub sections,
or the comment of the last sub sections.

``` python
write(comment="52", parse=True)
```



<h6 id="arguments-6">Arguments</h6>- **comment** (str) : the text to write
- - **parse** (_bool_ = True) : parse the comment

<h5 id="link_to">link_to</h5>MD link

``` python
link_to(url="57")
```



<h6 id="returns-11">Returns</h6>- **str** : [title](url + link_token)

<h5 id="get_section">get_section</h5>Look for a sub section by its title

> [!NOTE]
> This function searches only in the direct children, not in the whole tree.

To search a section in the whole tree, use [LINK ERROR: page '' not found]() method:

``` python
sub_section = parent_section.iteration(lambda s: s.title == 'The title')
```

``` python
get_section(title)
```



<h6 id="arguments-7">Arguments</h6>- **title** (str) : the section to look for

<h6 id="returns-12">Returns</h6>- **Section** :  if found, None otherwise


<h5 id="alphabetical_sections">alphabetical_sections</h5>Build a dictionary keyed by the section title initials

Used to diplay a table of content when there is a great number of sections.

```
{'A': ['a section', 'another section',
 'O': ['other section']
 }
```

``` python
alphabetical_sections(alpha=None)
```



<h6 id="arguments-8">Arguments</h6>- **alpha** (_dict_ = None) : dictionary to feed

<h6 id="returns-13">Returns</h6>- **dict** :  of list of Sections


<h5 id="build_header">build_header</h5>Yield the lines of the header part

``` python
build_header()
```



<h5 id="build_sections">build_sections</h5>Yield the lines of the sections parts

``` python
build_sections()
```



<h5 id="build_extra">build_extra</h5>Yield extra lines at the end of the section documentation

``` python
build_extra()
```



<h5 id="build">build</h5>Yield the lines of the section

The method yields the lines from method **build_header** and the from
**build_sections**.

If the flag **with_sections_only** is set, nothing is yield if there is no
sub sections.

``` python
build()
```



<h6 id="returns-14">Returns</h6>- **str** : documentation lines for the sections

<h5 id="print">print</h5>Print the documentation in the console

For debug purpose.

``` python
print()
```



<h3 id="argument">Argument</h3>Function argument

Yield a line for argument documentation:
```
- name (type = default) : description
```

<h4 id="properties-1">Properties</h4><h4 id="methods-1">Methods</h4>

``` python
Argument(name, type=None, default=None, description=None)
```



#### __init__



<h5 id="build-1">build</h5>Yield line argument

``` python
build()
```



<h6 id="returns-15">Returns</h6>- **str** : formatted argument line

<h3 id="return">Return</h3>Function returns

Yield a line for return documentation:
```
- name  : description
```

<h4 id="properties-2">Properties</h4><h4 id="methods-2">Methods</h4>

``` python
Return(name, description=None)
```



#### __init__



<h5 id="build-2">build</h5>Yield line return

``` python
build()
```



<h6 id="returns-16">Returns</h6>- **str** : formatted return line

<h3 id="function">Function</h3>Section dedicated to function documentation.

The comment can contain description of Arguments and Returns.
The comment is parsed in order to extract this information and to
write the document is a homogeneous way.

Arguments
---------
- name (str) : function or method name
- comment (str = None) : header comment
- level (int = 1) : indentation level

<h4 id="properties-3">Properties</h4><h5 id="arguments-9">arguments</h5>Arguments Section> type Section


<h6 id="getter-6">Getter</h6>Arguments Section

``` python
arguments()
```



<h7 id="returns-17">Returns</h7>- **Section** : title is 'Arguments', sub sections are [Argument](#argument)

<h5 id="returns-18">returns</h5>Arguments Section> type Section


<h6 id="getter-7">Getter</h6>Arguments Section

``` python
returns()
```



<h7 id="returns-19">Returns</h7>- **Section** : title is 'Arguments', sub sections are [Return](#return)

<h4 id="methods-3">Methods</h4><h5 id="init-1">init</h5>Function section specific init

A Function section is made of two sections:
- Arguments
- Returns

It also create stores other information:
- decorators
- arguments

``` python
init()
```



<h5 id="parse_comment-2">parse_comment</h5>Function comment parser

The Function parser extracts Properties, Arguments and Returns sections.
The corresponding lines are remove from the comment to feed the two sections.

The lists are generated from the structure

``` python
parse_comment(comment)
```



<h5 id="fromdoc">FromDoc</h5>Create a class from an instance of Doc

Doc is a class read by the **Parser**.

``` python
FromDoc(doc, class_name=None, **kwargs)
```



<h6 id="arguments-10">Arguments</h6>- **doc** (Doc) : Doc parsed by **Parser**

<h3 id="class">Class</h3>Section documenting a class

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

<h4 id="properties-4">Properties</h4><h5 id="bases">bases</h5>name of the base classes> type list of str


<h5 id="subclasses">subclasses</h5>name of the sub classes> type list of str


<h5 id="inherited">inherited</h5>properties and methods inherited from base classes> type list of str


<h5 id="properties-5">properties</h5>Properties Section> type Section


<h6 id="getter-8">Getter</h6>Properties Section

``` python
properties()
```



<h7 id="returns-20">Returns</h7>- **Section** : title is 'Properties', sub sections are documented properties

<h5 id="methods-4">methods</h5>Methods Section> type Section


<h6 id="getter-9">Getter</h6>Methods Section

``` python
methods()
```



<h7 id="returns-21">Returns</h7>- **Section** : title is 'Methods', sub sections are documented methods

<h4 id="methods-5">Methods</h4><h5 id="fromdoc-1">FromDoc</h5>Creates a Class document from a Doc parsed from source file

The **doc** argument contains the list of documents methods and properties.

``` python
FromDoc(doc, ignore_uncommented=True, **kwargs)
```



<h6 id="arguments-11">Arguments</h6>- **doc** (Doc) : Doc parsed from a sourc file
- - **exclude_uncommented** (_bool_ = True) : exclude the methods which are not commented in the source file

<h6 id="returns-22">Returns</h6>- **Class** : document on the class

<h5 id="compile">compile</h5>Compile the class

**project** refers to the global [LINK ERROR: page 'Project' not found]() documentation.

Class compilation is:
- Load each class based on this one into to the **subclasses** attribute.
- Load the methods and properties inherited from parent classes

``` python
compile(project)
```



<h6 id="arguments-12">Arguments</h6>- **project** ([LINK ERROR: page 'Project' not found]()) : main project

<h6 id="returns-23">Returns</h6>- **self** : 


<h5 id="capture_class">capture_class</h5>Capture methods and properties from another Class

This method allows to get the documentation of inherited items of a class
which is not documentated.

``` python
capture_class(other, with_comment=False)
```



<h6 id="arguments-13">Arguments</h6>- **other** (Class) : class to copy methods and properties from

<h6 id="returns-24">Returns</h6>- **self** : 


<h5 id="build-3">build</h5>Yield the Class documentation lines

``` python
build()
```



<h3 id="project">Project</h3>Project documentation

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

<h4 id="properties-6">Properties</h4><h4 id="methods-6">Methods</h4>

``` python
Project(title, comment=None, toc="174")
```



#### __init__



<h5 id="add_source">add_source</h5>Add a source code.

The source code is parsed and the resulting [LINK ERROR: page 'Section' not found]() is stored in the [LINK ERROR: page '' not found]() dict.

``` python
add_source(key, text)
```



<h6 id="arguments-14">Arguments</h6>- **key** (str) : source file key
- - **text** (str) : the source code

<h6 id="returns-25">Returns</h6>- **Section** : 


<h5 id="load_files">load_files</h5>Enrich the reference doc by parsing source files.

All the files with `.py` extension are parsed.

``` python
load_files(folder=None, sub_folders=[], key=None)
```



<h6 id="arguments-15">Arguments</h6>- **folder** (str) : main folder
- - **sub_folders** (str) : sub folders to explore
- - **key** (_str_ = None) : 

<h6 id="returns-26">Returns</h6>- **self** : 


<h5 id="get_refdoc">get_refdoc</h5>Get a reference documentation from the base

If **key** argument is None, the **name** is searched in the whole dictionary,
otherwise the search is performed only in the specified key.

If **exact** is False, name is considered as a regular expression.
All the title matching this expression is returned in a list.

``` python
get_refdoc(name, key=None, exact=True, halt=True)
```



<h6 id="arguments-16">Arguments</h6>- **name** (str) : title of the reference documentation
- - **key** (_str_ = None) : source file key
- - **exact** (_bool_ = True) : use exact name if True, regular expression otherwise
- - **halt** (_bool_ = True) : raise an exception if not found

<h6 id="returns-27">Returns</h6>- **Section** : found section if exact is True, list of sections otherwise

<h5 id="add_page">add_page</h5>Add a page in the documentation

``` python
add_page(page)
```



<h6 id="arguments-17">Arguments</h6>- **page** ([LINK ERROR: page 'Section' not found]()) : the page to add

<h6 id="returns-28">Returns</h6>- **Section** : the argument **page**

<h5 id="new_page">new_page</h5>Add a page in the documentation

> [!CAUTION]
> **title** argument is used a as key in [LINK ERROR: page '' not found]() dictionary. It must be unique
> in the scope of the project

``` python
new_page(title, comment=None, toc=None, in_toc=True)
```



<h6 id="arguments-18">Arguments</h6>- **title** (str) : page title
- - **comment** (str) : comment
- - **toc** (_str_ = None) : title of the content section, None if no content section is required
- - **in_toc** (_bool_ = True) : include the the documentation table of content

<h6 id="returns-29">Returns</h6>- **Page** : >


<h5 id="add_class">add_class</h5>Copy class documentation from reference documentation to pages

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



<h6 id="arguments-19">Arguments</h6>- **class_name** (str) : class name
- - **page** (_[LINK ERROR: page 'Section' not found]() or str_ = None) : name of the page where to include the class documentation
- - **bases** (_list of strs_ = []) : list of base classes
- - **capture** (_list of strs or [LINK ERROR: page 'Class' not found]()_ = []) : list of classes to copy methods and properties from
- - **file_key** (_str_ = None) : file key in [LINK ERROR: page '' not found]()

<h6 id="returns-30">Returns</h6>- **Class** : created class

<h5 id="add_function">add_function</h5>Copy function documentation reference documentation to pages.

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



<h6 id="arguments-20">Arguments</h6>- **function_name** (str) : class name
- - **page** (_[LINK ERROR: page 'Section' not found]() or str_ = None) : name of the page where to include the class documentation
- - **file_key** (_str_ = None) : file key in [LINK ERROR: page '' not found]()
- - **function_key** (_str_ = None) : key of the function in [LINK ERROR: page '' not found]()
- - **exact** (_bool_ = True) : use exact name if True, regular expression otherwise
- - **only_commented** (_bool_ = True) : don't include uncommented functions
- - **sub_level** (_int_ = 1) : incrementation level to page.level

<h6 id="returns-31">Returns</h6>- **Function** : created class

<h5 id="set_hook">set_hook</h5>Replace a regular expression by as substitution string

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



<h6 id="arguments-21">Arguments</h6>- **expr** (str) : RegEx expression - repl (str or function) : replacement string or function

<h5 id="create_index_file">create_index_file</h5>Create the index file

``` python
create_index_file(file_name)
```



<h6 id="arguments-22">Arguments</h6>- **file_name** (str) : file name to write

