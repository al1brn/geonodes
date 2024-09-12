<h1 id="documentation">documentation</h1>
Created on Wed Sep 11 17:42:12 2024

@author: alain


<h2 id="functions">Functions</h2><h2 id="classes">Classes</h2><h3 id="section">Section</h3>Version document item

<h4 id="properties">Properties</h4><h4 id="methods">Methods</h4>

``` python
Section(title, comment=None)
```



#### __init__



<h5 id="iteration">iteration</h5>Run the function on the section and sub sections

The method halts on the first section for which the function
return `True` and returns this section.
If the function doesn't return `True`, the methods is run on all sections
and return `None`.

``` python
iteration(f, *args)
```



<h6 id="arguments">Arguments</h6>- **f** (function of template f(section)) : the function to run

<h6 id="returns">Returns</h6>- **Section** :  or None


<h5 id="sections">sections</h5>Flat list of sections and sub sections

``` python
sections(with_owner=False)
```



<h5 id="get_section">get_section</h5>Get a section by its title or path

``` python
get_section(title)
```



<h5 id="new_section">new_section</h5>Add a sub section

``` python
new_section(title, comment=None)
```



<h6 id="arguments-1">Arguments</h6>- **title** (str) : section title
- - **comment** (str) : header comment
- - **sub_level** (_int_ = 1) : level increment

<h6 id="returns-1">Returns</h6>- **Section** : 


<h5 id="write_header">write_header</h5>Append text to the header comment

``` python
write_header(comment)
```



<h6 id="arguments-2">Arguments</h6>- **comment** (str) : the text to write

<h5 id="write">write</h5>Append text to the current text

The current text is either the comment if this section if there is not sub sections,
or the comment of the last sub sections.

``` python
write(comment)
```



<h6 id="arguments-3">Arguments</h6>- **comment** (str) : the text to write

<h5 id="print">print</h5>Print the documentation in the console

For debug purpose.

``` python
print(full=False)
```



<h3 id="documentation-1">Documentation</h3>Whole project documentation

A **Project** is a [LINK ERROR: page 'Section' not found]() which is the top level page of the document,
and whose sections are alse pages.

[LINK ERROR: page 'Section' not found]() [LINK ERROR: page 'Section' not found]() must be unique.

<h4 id="properties-1">Properties</h4><h4 id="methods-1">Methods</h4>

``` python
Documentation(title, comment=None)
```



#### __init__



<h5 id="load_source">load_source</h5>Add a source code.

The source code is parsed and the resulting [LINK ERROR: page 'Section' not found]() is stored in the [LINK ERROR: page '' not found]() dict.

``` python
load_source(key, text)
```



<h6 id="arguments-4">Arguments</h6>- **key** (str) : source file key
- - **text** (str) : the source code

<h6 id="returns-2">Returns</h6>- **Section** : 


<h5 id="load_file">load_file</h5>Enrich the reference doc by parsing source files.

All the files with `.py` extension are parsed.

``` python
load_file(file_name, key=None)
```



<h6 id="arguments-5">Arguments</h6>- **folder** (str) : main folder
- - **sub_folders** (str) : sub folders to explore
- - **key** (_str_ = None) : 

<h6 id="returns-3">Returns</h6>- **self** : 


<h5 id="load_files">load_files</h5>Enrich the reference doc by parsing source files.

All the files with `.py` extension are parsed.

``` python
load_files(folder=None, sub_folders=[], key=None, verbose=True)
```



<h6 id="arguments-6">Arguments</h6>- **folder** (str) : main folder
- - **sub_folders** (str) : sub folders to explore
- - **key** (_str_ = None) : 

<h6 id="returns-4">Returns</h6>- **self** : 


<h5 id="hide_classes">hide_classes</h5>Undocument classes

Properties and methods of undocumented classes are capture by inherited classes

``` python
hide_classes(classes, verbose=True)
```



<h5 id="add_page">add_page</h5>Add a page in the documentation

``` python
add_page(section)
```



<h6 id="arguments-7">Arguments</h6>- **page** ([LINK ERROR: page 'Section' not found]()) : the page to add

<h6 id="returns-5">Returns</h6>- **Section** : the argument **page**

<h5 id="new_page">new_page</h5>Add a page in the documentation

> [!CAUTION]
> **title** argument is used a as key in [LINK ERROR: page '' not found]() dictionary. It must be unique
> in the scope of the project

``` python
new_page(title, comment=None)
```



<h6 id="arguments-8">Arguments</h6>- **title** (str) : page title
- - **comment** (str) : comment

<h6 id="returns-6">Returns</h6>- **Section** : >


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



<h6 id="arguments-9">Arguments</h6>- **expr** (str) : RegEx expression - repl (str or function) : replacement string or function

<h5 id="solve_links">solve_links</h5>Solve user links into MD links.

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
> [LINK ERROR: section '_token' not found]() and [LINK ERROR: section 'is_page' not found]() must have been set correctly before solving the links.

``` python
solve_links(ignore_source=False)
```



<h6 id="arguments-10">Arguments</h6>- **ignore_source** (_bool_ = False) : Do not extract source before solving (already done)

<h5 id="solve_hooks">solve_hooks</h5>Solve all the hooks for a section.

``` python
solve_hooks(include_links=True)
```



<h6 id="arguments-11">Arguments</h6>- **include_links** (_bool_ = True) : solve also the links

<h5 id="compile">compile</h5>Initialize sections parameters at their good values

``` python
compile()
```



<h5 id="create_index_file">create_index_file</h5>Create the index file

``` python
create_index_file(file_name)
```



<h6 id="arguments-12">Arguments</h6>- **file_name** (str) : file name to write

