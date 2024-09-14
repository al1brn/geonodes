# Section

Document section

Project documentation is made of **pages** organized in **modules**.
Modules and pages are articulated as folders and files but the document
hierarchy doesn't have to stick to the structure of the source folders.

The documentation is based on the versatile class [Section](section.md) which can be:
- a text section in a page
- a documentation page
- a module
- the whole documentation itself

A [Section](section.md) is basically a list of **sub sections** with a header [LINK ERROR: section 'comment' not found](section.md).
Its attributes drive its behavior:
    
- [is_page](section.md#is_page) : the section is written in a dedicated page, otherwise
  it is written if the flow of the [page](section.md#page) it belongs to.
  Wheter a section is a page or not is taken into account to build links toward this section.
  
  
``` python
doc = Documentation("Project documentation")

# ----- Load source files in the documentation main modules

doc.load_folder(folder_path1)
doc.load_folder(folder_path2)

# ----- Create another module from other folder

module = doc.new_module("Some module", folder_path3)
module.load_folder(folder_path3)
```

``` python
Section(title, comment=None, sort_sections=False, in_toc=False, module=None, is_page=False, ignore_if_empty=True, top_bar=None)
```



## Content


- A : [add_class_dict](#add_class_dict) :black_small_square: [add_file_dict](#add_file_dict) :black_small_square: [add_function_dict](#add_function_dict) :black_small_square: [add_module](#add_module) :black_small_square: [add_page](#add_page) :black_small_square: [add_property_dict](#add_property_dict) :black_small_square: [add_section](#add_section) :black_small_square: [anchor](#anchor) :black_small_square: [append](#append)
- C : [create_file](#create_file)
- D : [depth](#depth) :black_small_square: [depth_in_page](#depth_in_page) :black_small_square: [dump](#dump)
- F : [file_name](#file_name) :black_small_square: [func](#func)
- G : [get_content](#get_content) :black_small_square: [get_create_section](#get_create_section) :black_small_square: [get_documentation](#get_documentation) :black_small_square: [get_items](#get_items) :black_small_square: [get_module](#get_module) :black_small_square: [get_page](#get_page) :black_small_square: [get_section](#get_section) :black_small_square: [get_toc](#get_toc)
- H : [has_content](#has_content) :black_small_square: [has_toc](#has_toc) :black_small_square: [hidden](#hidden) :black_small_square: [homonyms_count](#homonyms_count)
- I : [is_module](#is_module) :black_small_square: [is_page](#is_page) :black_small_square: [is_top](#is_top) :black_small_square: [iteration](#iteration)
- L : [link_to](#link_to)
- M : [module](#module) :black_small_square: [module_path](#module_path)
- P : [page](#page) :black_small_square: [print](#print)
- S : [sort](#sort)
- T : [TestStructure](#teststructure) :black_small_square: [test_doc](#test_doc) :black_small_square: [test_dump](#test_dump) :black_small_square: [test_get](#test_get) :black_small_square: [top](#top)
- W : [write](#write) :black_small_square: [write_header](#write_header) :black_small_square: [write_navigation](#write_navigation) :black_small_square: [write_source](#write_source)
- _ : [__str__](#__str__)



## Properties

----------
### anchor



- getter 


<sub>[top](#section) [index](index.md)</sub>



----------
### depth



- getter 


<sub>[top](#section) [index](index.md)</sub>



----------
### depth_in_page



- getter 


<sub>[top](#section) [index](index.md)</sub>



----------
### file_name



- getter 


<sub>[top](#section) [index](index.md)</sub>



----------
### has_content



- getter 


<sub>[top](#section) [index](index.md)</sub>



----------
### has_toc



- getter 


<sub>[top](#section) [index](index.md)</sub>



----------
### hidden



- getter 


<sub>[top](#section) [index](index.md)</sub>



----------
### homonyms_count



- getter 


<sub>[top](#section) [index](index.md)</sub>



----------
### is_module



- getter 


<sub>[top](#section) [index](index.md)</sub>



----------
### is_page



- getter setter


<sub>[top](#section) [index](index.md)</sub>



----------
### is_top

Is top section

- getter 
- type **bool**


<sub>[top](#section) [index](index.md)</sub>



----------
### module



- getter 


<sub>[top](#section) [index](index.md)</sub>



----------
### module_path



- getter 


<sub>[top](#section) [index](index.md)</sub>



----------
### page



- getter 


<sub>[top](#section) [index](index.md)</sub>



----------
### top



- getter 


<sub>[top](#section) [index](index.md)</sub>



## Methods

----------
### TestStructure



``` python
TestStructure()
```



<sub>[top](#section) [index](index.md)</sub>



----------
### __str__



``` python
__str__()
```



<sub>[top](#section) [index](index.md)</sub>



----------
### add_class_dict



``` python
add_class_dict(class_dict, ignore_uncommented=False)
```



<sub>[top](#section) [index](index.md)</sub>



----------
### add_file_dict



``` python
add_file_dict(file_dict)
```



<sub>[top](#section) [index](index.md)</sub>



----------
### add_function_dict



``` python
add_function_dict(func_dict)
```



<sub>[top](#section) [index](index.md)</sub>



----------
### add_module



``` python
add_module(module, title, comment=None, **kwargs)
```



<sub>[top](#section) [index](index.md)</sub>



----------
### add_page



``` python
add_page(title, comment=None, **kwargs)
```



<sub>[top](#section) [index](index.md)</sub>



----------
### add_property_dict



``` python
add_property_dict(prop_dict)
```



<sub>[top](#section) [index](index.md)</sub>



----------
### add_section



``` python
add_section(title, comment=None, **kwargs)
```



<sub>[top](#section) [index](index.md)</sub>



----------
### append



``` python
append(section)
```



<sub>[top](#section) [index](index.md)</sub>



----------
### create_file



``` python
create_file(section)
```



<sub>[top](#section) [index](index.md)</sub>



----------
### dump



``` python
dump()
```



<sub>[top](#section) [index](index.md)</sub>



----------
### func



``` python
func(section)
```



<sub>[top](#section) [index](index.md)</sub>



----------
### get_content

Returns the text to write in the page

``` python
get_content()
```



<sub>[top](#section) [index](index.md)</sub>



----------
### get_create_section



``` python
get_create_section(title, comment=None,**kwargs)
```



<sub>[top](#section) [index](index.md)</sub>



----------
### get_documentation

Write the section into a dict

``` python
get_documentation(create_files=True)
```



#### Arguments

- **doc** (dict) : the dict where to write the documentation



<sub>[top](#section) [index](index.md)</sub>



----------
### get_items



``` python
get_items(section)
```



<sub>[top](#section) [index](index.md)</sub>



----------
### get_module



``` python
get_module(title, condition=None, **kwargs)
```



<sub>[top](#section) [index](index.md)</sub>



----------
### get_page



``` python
get_page(title, condition=None, **kwargs)
```



<sub>[top](#section) [index](index.md)</sub>



----------
### get_section



``` python
get_section(title=None, condition=None, **kwargs)
```



<sub>[top](#section) [index](index.md)</sub>



----------
### get_toc



``` python
get_toc(title="21", level=2)
```



<sub>[top](#section) [index](index.md)</sub>



----------
### iteration



``` python
iteration(func, *args, include_top=True)
```



<sub>[top](#section) [index](index.md)</sub>



----------
### link_to



``` python
link_to(absolute=True, title=None)
```



<sub>[top](#section) [index](index.md)</sub>



----------
### print



``` python
print(text_max=100)
```



<sub>[top](#section) [index](index.md)</sub>



----------
### sort



``` python
sort()
```



<sub>[top](#section) [index](index.md)</sub>



----------
### test_doc



``` python
test_doc()
```



<sub>[top](#section) [index](index.md)</sub>



----------
### test_dump



``` python
test_dump()
```



<sub>[top](#section) [index](index.md)</sub>



----------
### test_get



``` python
test_get()
```



<sub>[top](#section) [index](index.md)</sub>



----------
### write

Append text to the header comment

``` python
write(text)
```



#### Arguments

- **text** (str) : the text to write



<sub>[top](#section) [index](index.md)</sub>



----------
### write_header

Write a section in the text stream

This method write MD text corresponding to a header followed by text.

> [!NOTE]
> This method doesn't create a section in the hierarchy, contrary to [add_section](#add_section)

``` python
write_header(level, title, text)
```



#### Arguments

- **level** (int) : header level
- - **title** (str) : header title
- - **text** (str) : text



<sub>[top](#section) [index](index.md)</sub>



----------
### write_navigation



``` python
write_navigation()
```



<sub>[top](#section) [index](index.md)</sub>



----------
### write_source



``` python
write_source(source)
```



<sub>[top](#section) [index](index.md)</sub>

