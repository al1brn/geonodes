# documentation


Created on Wed Sep 11 17:42:12 2024

@author: alain


## Content

[Documentation](#documentation)
- [Section](#section)

## Functions

## Classes

### Documentation

Whole project documentation

A **Project** is a [LINK ERROR: page 'Section' not found]() which is the top level page of the document,
and whose sections are alse pages.

[LINK ERROR: page 'Section' not found]() [LINK ERROR: page 'Section' not found]() must be unique.

<sub>[top](#documentation) [index](index.md)</sub>



#### Content


- A : [add_page](#add_page)
- C : [compile](#compile) :black_small_square: [create_index_file](#create_index_file)
- H : [hide_classes](#hide_classes)
- L : [load_source](#load_source) :black_small_square: [load_file](#load_file) :black_small_square: [load_files](#load_files)
- N : [new_page](#new_page)
- S : [set_hook](#set_hook) :black_small_square: [solve_links](#solve_links) :black_small_square: [solve_hooks](#solve_hooks)

#### Properties

#### Methods



``` python
Documentation(title, comment=None)
```



##### add_page

Add a page in the documentation

``` python
add_page(section)
```



<sub>[top](#documentation) [index](index.md)</sub>



###### Arguments

- **page** ([LINK ERROR: page 'Section' not found]()) : the page to add

###### Returns

- **Section** : the argument **page**

##### compile

Initialize sections parameters at their good values

``` python
compile()
```



<sub>[top](#documentation) [index](index.md)</sub>



##### create_index_file

Create the index file

``` python
create_index_file(file_name)
```



<sub>[top](#documentation) [index](index.md)</sub>



###### Arguments

- **file_name** (str) : file name to write

##### hide_classes

Undocument classes

Properties and methods of undocumented classes are capture by inherited classes

``` python
hide_classes(classes, verbose=True)
```



<sub>[top](#documentation) [index](index.md)</sub>



##### load_file

Enrich the reference doc by parsing source files.

All the files with `.py` extension are parsed.

``` python
load_file(file_name, key=None)
```



<sub>[top](#documentation) [index](index.md)</sub>



###### Arguments

- **folder** (str) : main folder
- - **sub_folders** (str) : sub folders to explore
- - **key** (_str_ = None) : 

###### Returns

- **self** : 

##### load_files

Enrich the reference doc by parsing source files.

All the files with `.py` extension are parsed.

``` python
load_files(folder=None, sub_folders=[], key=None, verbose=True)
```



<sub>[top](#documentation) [index](index.md)</sub>



###### Arguments

- **folder** (str) : main folder
- - **sub_folders** (str) : sub folders to explore
- - **key** (_str_ = None) : 

###### Returns

- **self** : 

##### load_source

Add a source code.

The source code is parsed and the resulting [LINK ERROR: page 'Section' not found]() is stored in the [LINK ERROR: page '' not found]() dict.

``` python
load_source(key, text)
```



<sub>[top](#documentation) [index](index.md)</sub>



###### Arguments

- **key** (str) : source file key
- - **text** (str) : the source code

###### Returns

- **Section** : 

##### new_page

Add a page in the documentation

> [!CAUTION]
> **title** argument is used a as key in [LINK ERROR: page '' not found]() dictionary. It must be unique
> in the scope of the project

``` python
new_page(title, comment=None)
```



<sub>[top](#documentation) [index](index.md)</sub>



###### Arguments

- **title** (str) : page title
- - **comment** (str) : comment

###### Returns

- **Section** : 

##### set_hook

Replace a regular expression by as substitution string

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
> syntax : `<!Section title#Sub section title>` which is converted in [LINK ERROR: page 'Project' not found]().

``` python
set_hook(expr, repl)
```



<sub>[top](#documentation) [index](index.md)</sub>



###### Arguments

- **expr** (str) : RegEx expression - repl (str or function) : replacement string or function

##### solve_hooks

Solve all the hooks for a section.

``` python
solve_hooks(include_links=True)
```



<sub>[top](#documentation) [index](index.md)</sub>



###### Arguments

- **include_links** (_bool_ = True) : solve also the links

##### solve_links

Solve user links into MD links.

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
> [LINK ERROR: section '_anchor' not found]() and [LINK ERROR: section 'is_page' not found]() must have been set correctly before solving the links.

``` python
solve_links(ignore_source=False)
```



<sub>[top](#documentation) [index](index.md)</sub>



###### Arguments

- **ignore_source** (_bool_ = False) : Do not extract source before solving (already done)

### Section

Version document item

<sub>[top](#documentation) [index](index.md)</sub>



#### Content

[Toc](#toc)
- [get_section](#get_section)
- [iteration](#iteration)
- [new_section](#new_section)
- [print](#print)
- [sections](#sections)
- [write](#write)
- [write_header](#write_header)

#### Properties

#### Methods



``` python
Section(title, comment=None)
```



##### Toc

Create a table of content from the given list

``` python
Toc(items, title="17")
```



<sub>[top](#section) [index](index.md)</sub>



###### Arguments

- **items** (list) : list of couples (key, value)

###### Returns

- **Section** : 

##### get_section

Get a section by its title or path

``` python
get_section(title)
```



<sub>[top](#section) [index](index.md)</sub>



##### iteration

Run the function on the section and sub sections

The method halts on the first section for which the function
return `True` and returns this section.
If the function doesn't return `True`, the methods is run on all sections
and return `None`.

``` python
iteration(f, *args)
```



<sub>[top](#section) [index](index.md)</sub>



###### Arguments

- **f** (function of template f(section)) : the function to run

###### Returns

- **Section** : 

##### new_section

Add a sub section

``` python
new_section(title, comment=None)
```



<sub>[top](#section) [index](index.md)</sub>



###### Arguments

- **title** (str) : section title
- - **comment** (str) : header comment
- - **sub_level** (_int_ = 1) : level increment

###### Returns

- **Section** : 

##### print

Print the documentation in the console

For debug purpose.

``` python
print(full=False)
```



<sub>[top](#section) [index](index.md)</sub>



##### sections

Flat list of sections and sub sections

``` python
sections(with_owner=False)
```



<sub>[top](#section) [index](index.md)</sub>



##### write

Append text to the current text

The current text is either the comment if this section if there is not sub sections,
or the comment of the last sub sections.

``` python
write(comment)
```



<sub>[top](#section) [index](index.md)</sub>



###### Arguments

- **comment** (str) : the text to write

##### write_header

Append text to the header comment

``` python
write_header(comment)
```



<sub>[top](#section) [index](index.md)</sub>



###### Arguments

- **comment** (str) : the text to write

