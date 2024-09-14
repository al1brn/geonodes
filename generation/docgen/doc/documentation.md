# Documentation

Project Documentation

Properties
----------
- doc_folder (str) : target folder for documentation files
- source_folder (str) : root folder for files
- parsed (dict) : dictionary of loaded and parsed filed
- hooks (list) : list of regular expressions and hook function to apply on the documentation

``` python
Documentation(title, doc_folder, source_folder=None)
```



## Content


- C : [classes_list](#classes_list)
- D : [docgen_documentation](#docgen_documentation) :black_small_square: [document_folder](#document_folder)
- G : [get_class](#get_class)
- H : [hide](#hide) :black_small_square: [hide_classes](#hide_classes)
- L : [load_file](#load_file) :black_small_square: [load_folder](#load_folder) :black_small_square: [load_source](#load_source)
- M : [module_info](#module_info) :black_small_square: [modules](#modules) :black_small_square: [modules_content](#modules_content) :black_small_square: [modules_iter](#modules_iter) :black_small_square: [modules_list](#modules_list) :black_small_square: [modules_search](#modules_search)
- S : [set_hook](#set_hook) :black_small_square: [solve_hooks](#solve_hooks) :black_small_square: [solve_links](#solve_links) :black_small_square: [solve_section](#solve_section) :black_small_square: [solve_section_links](#solve_section_links)
- T : [test_file](#test_file)



## Properties

----------
### classes_list

List of classes

- getter 
- type **list**


<sub>[top](#documentation) [index](index.md)</sub>



----------
### modules

Dictionary of parsed files.

- getter 
- type **dict**


<sub>[top](#documentation) [index](index.md)</sub>



## Methods

----------
### docgen_documentation



``` python
docgen_documentation()
```



<sub>[top](#documentation) [index](index.md)</sub>



----------
### document_folder



``` python
document_folder(folder_key)
```



<sub>[top](#documentation) [index](index.md)</sub>



----------
### get_class



``` python
get_class(class_name)
```



<sub>[top](#documentation) [index](index.md)</sub>



----------
### hide



``` python
hide(class_)
```



<sub>[top](#documentation) [index](index.md)</sub>



----------
### hide_classes

Undocument classes

Properties and methods of undocumented classes are capture by inherited classes

``` python
hide_classes(classes, verbose=True)
```



<sub>[top](#documentation) [index](index.md)</sub>



----------
### load_file

Enrich the reference doc by parsing source files.

All the files with `.py` extension are parsed.

``` python
load_file(file_key, file_name, verbose=False)
```



### Arguments

- **file_key** (str) : file key in <#modules>
- - **file_name** (str) : file path



<sub>[top](#documentation) [index](index.md)</sub>



----------
### load_folder

Enrich the reference doc by parsing source files.

> [!CAUTION]
> if <#source_folder> is not None, folder is relative to it

All the files with `.py` extension are parsed.

``` python
load_folder(folder, verbose=True)
```



### Arguments

- **folder** (str) : absolute folder or folder relative to <#source_folder> if not None



### Returns

- **self** : 



<sub>[top](#documentation) [index](index.md)</sub>



----------
### load_source

Add a source code.

The source code is parsed and the resulting dict is stored in the <!#parsed> dict.

``` python
load_source(key, text)
```



### Arguments

- **key** (str) : source file key
- - **text** (str) : the source code



### Returns

- **Section** : 



<sub>[top](#documentation) [index](index.md)</sub>



----------
### module_info



``` python
module_info(key)
```



<sub>[top](#documentation) [index](index.md)</sub>



----------
### modules_content



``` python
modules_content()
```



<sub>[top](#documentation) [index](index.md)</sub>



----------
### modules_iter



``` python
modules_iter(f, *args, **kwargs)
```



<sub>[top](#documentation) [index](index.md)</sub>



----------
### modules_list



``` python
modules_list(name_only=True, **kwargs)
```



<sub>[top](#documentation) [index](index.md)</sub>



----------
### modules_search



``` python
modules_search(**kwargs)
```



<sub>[top](#documentation) [index](index.md)</sub>



----------
### set_hook

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
> syntax : `<!Section title#Sub section title>` which is converted in <!Project#set_hook>.

``` python
set_hook(expr, repl)
```



### Arguments

- **expr** (str) : RegEx expression - repl (str or function) : replacement string or function



<sub>[top](#documentation) [index](index.md)</sub>



----------
### solve_hooks

Solve all the hooks for a section.

``` python
solve_hooks(include_links=True)
```



### Arguments

- **include_links** (_bool_ = True) : solve also the links



<sub>[top](#documentation) [index](index.md)</sub>



----------
### solve_links

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
> <#_anchor> and <#is_page> must have been set correctly before solving the links.

``` python
solve_links(ignore_source=False)
```



### Arguments

- **ignore_source** (_bool_ = False) : Do not extract source before solving (already done)



<sub>[top](#documentation) [index](index.md)</sub>



----------
### solve_section



``` python
solve_section(section)
```



<sub>[top](#documentation) [index](index.md)</sub>



----------
### solve_section_links



``` python
solve_section_links(section, ignore_source=False)
```



<sub>[top](#documentation) [index](index.md)</sub>



----------
### test_file



``` python
test_file(file_name=None, doc_folder=None)
```



<sub>[top](#documentation) [index](index.md)</sub>

