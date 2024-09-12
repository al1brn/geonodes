# documentation


Created on Wed Sep 11 17:42:12 2024

@author: alain


## Functions

## Classes

### Section

Version document item

#### Properties

#### Methods



``` python
Section(title, comment=None)
```



#### __init__



##### iteration

Run the function on the section and sub sections

The method halts on the first section for which the function
return `True` and returns this section.
If the function doesn't return `True`, the methods is run on all sections
and return `None`.

``` python
iteration(f, *args)
```



###### Arguments

- **f** (function of template f(section)) : the function to run

###### Returns

- **Section** :  or None


##### sections

Flat list of sections and sub sections

``` python
sections(with_owner=False)
```



##### get_section

Get a section by its title or path

``` python
get_section(title)
```



##### new_section

Add a sub section

``` python
new_section(title, comment=None)
```



###### Arguments

- **title** (str) : section title
- - **comment** (str) : header comment
- - **sub_level** (_int_ = 1) : level increment

###### Returns

- **Section** : 


##### write_header

Append text to the header comment

``` python
write_header(comment)
```



###### Arguments

- **comment** (str) : the text to write

##### write

Append text to the current text

The current text is either the comment if this section if there is not sub sections,
or the comment of the last sub sections.

``` python
write(comment)
```



###### Arguments

- **comment** (str) : the text to write

##### print

Print the documentation in the console

For debug purpose.

``` python
print(full=False)
```



### Documentation

Whole project documentation

A **Project** is a [LINK ERROR: page 'Section' not found]() which is the top level page of the document,
and whose sections are alse pages.

[LINK ERROR: page 'Section' not found]() [LINK ERROR: page 'Section' not found]() must be unique.

#### Properties

#### Methods



``` python
Documentation(title, comment=None)
```



#### __init__



##### load_source

Add a source code.

The source code is parsed and the resulting [LINK ERROR: page 'Section' not found]() is stored in the [LINK ERROR: page '' not found]() dict.

``` python
load_source(key, text)
```



###### Arguments

- **key** (str) : source file key
- - **text** (str) : the source code

###### Returns

- **Section** : 


##### load_file

Enrich the reference doc by parsing source files.

All the files with `.py` extension are parsed.

``` python
load_file(file_name, key=None)
```



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



###### Arguments

- **folder** (str) : main folder
- - **sub_folders** (str) : sub folders to explore
- - **key** (_str_ = None) : 

###### Returns

- **self** : 


##### hide_classes

Undocument classes

Properties and methods of undocumented classes are capture by inherited classes

``` python
hide_classes(classes, verbose=True)
```



##### add_page

Add a page in the documentation

``` python
add_page(section)
```



###### Arguments

- **page** ([LINK ERROR: page 'Section' not found]()) : the page to add

###### Returns

- **Section** : the argument **page**

##### new_page

Add a page in the documentation

> [!CAUTION]
> **title** argument is used a as key in [LINK ERROR: page '' not found]() dictionary. It must be unique
> in the scope of the project

``` python
new_page(title, comment=None)
```



###### Arguments

- **title** (str) : page title
- - **comment** (str) : comment

###### Returns

- **Section** : >


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
> [LINK ERROR: section '_token' not found]() and [LINK ERROR: section 'is_page' not found]() must have been set correctly before solving the links.

``` python
solve_links(ignore_source=False)
```



###### Arguments

- **ignore_source** (_bool_ = False) : Do not extract source before solving (already done)

##### solve_hooks

Solve all the hooks for a section.

``` python
solve_hooks(include_links=True)
```



###### Arguments

- **include_links** (_bool_ = True) : solve also the links

##### compile

Initialize sections parameters at their good values

``` python
compile()
```



##### create_index_file

Create the index file

``` python
create_index_file(file_name)
```



###### Arguments

- **file_name** (str) : file name to write

