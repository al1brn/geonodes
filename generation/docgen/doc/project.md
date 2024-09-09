# Project



``` python
Project(self, title, comment=None, toc='Content')
```

Project documentation

Project documentation allows to build a full project documentation from parsing source code, loading complementary documentation file and also by dynamically adding documentation.

The final documentation is written ad **MarkDown** files with **index.md** as main entrance for the documentation.

> [!IMPORTANT]
> All files are written in the same folder. The page titles must be unique in order
> to avoid overwritting content.

The document is built by:
- creating pages and writing content into it
- creating pages from parsed source code

The parsed source code is stored in [refdoc](#) dictionary with one entry per parsed file. The parsed source contain classes and function documentation which can be transfered into pages.

When transferring, a class can be enriched with other classed, either to specify inherited methods and properties or to complement the documentation with inheritance. See [add_class](#).

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



## Methods and Properties
- A : [add_class](#add_class) [add_page](#add_page) [add_source](#add_source) [apply_hooks](#apply_hooks) 
- C : [compile_project](#compile_project) [create_index_file](#create_index_file) 
- G : [get_refdoc](#get_refdoc) 
- L : [load_files](#load_files) 
- N : [new_page](#new_page) 
- O : [object_link](#object_link) 
- P : [pages](#pages) 
- R : [refdocs](#refdocs) 
- S : [sections](#sections) [set_hook](#set_hook) 

# Properties



# pages




##### Returns



- _None_ : 



<sub>[top](#project) [index](index.md)</sub>
# refdocs




##### Returns



- _None_ : 



<sub>[top](#project) [index](index.md)</sub>
# sections




##### Returns



- _None_ : 



<sub>[top](#project) [index](index.md)</sub>

# Methods



## add_class

``` python
Project.add_class(self, class_name, page=None, bases=[], capture=[], file_key=None)
```

Build documentation for a class from reference documentation.

The class must exist in one of the reference documentation [refdoc](#).

Class documentation is built with the following steps:
1. read the class documented in [refdoc](#)
2. reference the base classes in the array [Class](class.md#class)
3. add the documentation of properties and methods of classes included in **capture** argument

> **Explicit inheritance**
> _class_name_ : inherits from base_class
> inherited methods : **method1**, **method2**

> **Hidden inheritance**
> _class_name_
> methods : **method1**, **method2**

if **target_page** is None, a specific page will be create, otherwise, the class documentation will be append to the existing page specified by the argument.

> [!NOTE]
> The page where the class is documented can be retreive with attribute [Section](section.md#section).



##### Arguments



- **class_name** (_str_) : class name
- **page** : 
- **bases** : 
- **capture** : 
- **file_key** (_str_ = None) : file key in [files](#)

##### Returns



- _<!Class> : created class_ : 



<sub>[top](#project) [index](index.md)</sub>
## add_page

``` python
Project.add_page(self, page)
```

Add a page in the documentation



##### Arguments



- **page** : 

##### Returns



- _<!Section> : the argument **page**_ : 



<sub>[top](#project) [index](index.md)</sub>
## add_source

``` python
Project.add_source(self, key, text)
```

Add a source code.

The source code is parsed and the resulting [Section](section.md) is stored in the [refdoc](#) dict.



##### Arguments



- **key** (_str_) : source file key
- **text** (_str_) : the source code

##### Returns



- _Section_ : 



<sub>[top](#project) [index](index.md)</sub>
## apply_hooks

``` python
Project.apply_hooks(self, comment)
```

[LINK ERROR to 'Section title'](index.md) substitution




<sub>[top](#project) [index](index.md)</sub>
## compile_project

``` python
Project.compile_project(self)
```

Compile the classes




<sub>[top](#project) [index](index.md)</sub>
## create_index_file

``` python
Project.create_index_file(self, file_name)
```

Create the index file



##### Arguments



- **file_name** (_str_) : file name to write



<sub>[top](#project) [index](index.md)</sub>
## get_refdoc

``` python
Project.get_refdoc(self, name, key=None, halt=True)
```

Get a reference documentation from the base

If **key** argument is None, the **name** is searched in the whole dictionary, otherwise the search is performed only in the specified key.



##### Arguments



- **name** (_str_) : title of the reference documentation
- **key** (_str_ = None) : source file key
- **halt** (_bool_ = True) : raise an exception if not found

##### Returns



- _<!Section> : found section, None if not found_ : 



<sub>[top](#project) [index](index.md)</sub>
## load_files

``` python
Project.load_files(self, folder=None, sub_folders=[], key=None)
```

Enrich the reference doc by parsing source files.

All the files with `.py` extension are parsed.



##### Arguments



- **folder** (_str_) : main folder
- **sub_folders** (_str_) : sub folders to explore
- **key** (_str_ = None) : 

##### Returns



- _self_ : 



<sub>[top](#project) [index](index.md)</sub>
## new_page

``` python
Project.new_page(self, title, comment=None, toc=None, in_toc=True)
```

Add a page in the documentation

> [!CAUTION]
> **title** argument is used a as key in [pages](#) dictionary. It must be unique
> in the scope of the project



##### Arguments



- **title** (_str_) : page title
- **comment** (_str_) : comment
- **toc** (_str_ = None) : title of the content section, None if no content section is required
- **in_toc** (_bool_ = True) : include the the documentation table of content

##### Returns



- _<!Page>_ : 



<sub>[top](#project) [index](index.md)</sub>
## object_link

``` python
Project.object_link(self, name, token=None)
```

Token only




<sub>[top](#project) [index](index.md)</sub>
## set_hook

``` python
Project.set_hook(self, expr, repl)
```

Replace a regular expression by as substitution string

Hooks are applied to the documentation at compilation time.

``` python
# Instance of [!TOKEN] will be replaced by the substitution text.

proj.set_hook(r"\[!TOKEN\]", "substitution text")
```

Due to the piece of code above, the token `[!TOKEN]` is replaced here: **substitution text**

> [!NOTE]
> Text embedded in a _source code_ zone is not replaced

A function can be passed rather than a string as for `re.sub(expr, repl, text)`.

Here, the passed function can accept a second positional argument if a reference to the current section is required:

``` python
def replace(match_obj, section):
# section is the Section instance where the replacement occurs
pass
```

> [!NOTE]
> By default, a hook is used to define links between pages based on the
> syntax : `<!Section title#Sub section title>` which is converted in [Project](project.md#project).



##### Arguments



- **expr** (_str_) : RegEx expression
- **repl** : 



<sub>[top](#project) [index](index.md)</sub>

