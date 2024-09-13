# Section

Document section

Project documentation is made of **pages** organized in **modules**.
Modules and pages are articulated as folders and files but the document
hierarchy doesn't have to stick to the structure of the source folders.

The documentation is based on the versatile class <!Section> which can be:
- a text section in a page
- a documentation page
- a module
- the whole documentation itself

A <!Section> is basically a list of **sub sections** with a header <!Section#comment>.
Its attributes drive its behavior:
    
- <!Section#is_page> : the section is written in a dedicated page, otherwise
  it is written if the flow of the <!Section#page> it belongs to.
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



Content


- A : add_class_dict :black_small_square: add_file_dict :black_small_square: add_function_dict :black_small_square: add_module :black_small_square: add_page :black_small_square: add_property_dict :black_small_square: add_section :black_small_square: anchor :black_small_square: append
- C : create_file
- D : depth :black_small_square: depth_in_page :black_small_square: dump
- F : file_name :black_small_square: func
- G : get_content :black_small_square: get_create_section :black_small_square: get_documentation :black_small_square: get_items :black_small_square: get_module :black_small_square: get_page :black_small_square: get_section :black_small_square: get_toc
- H : has_content :black_small_square: has_toc :black_small_square: hidden :black_small_square: homonyms_count
- I : is_module :black_small_square: is_page :black_small_square: is_top :black_small_square: iteration
- L : link_to
- M : module :black_small_square: module_path
- P : page :black_small_square: print
- S : Section :black_small_square: sort
- T : TestStructure :black_small_square: test_doc :black_small_square: test_dump :black_small_square: test_get :black_small_square: test_self
- W : write :black_small_square: write_navigation :black_small_square: write_source
- _ : __str__



## Properties

----------
### anchor



- getter 


<sub>[top](#{self.page.anchor}) [index](index.md)</sub>



----------
### depth



- getter 


<sub>[top](#{self.page.anchor}) [index](index.md)</sub>



----------
### depth_in_page



- getter 


<sub>[top](#{self.page.anchor}) [index](index.md)</sub>



----------
### file_name



- getter 


<sub>[top](#{self.page.anchor}) [index](index.md)</sub>



----------
### has_content



- getter 


<sub>[top](#{self.page.anchor}) [index](index.md)</sub>



----------
### has_toc



- getter 


<sub>[top](#{self.page.anchor}) [index](index.md)</sub>



----------
### hidden



- getter 


<sub>[top](#{self.page.anchor}) [index](index.md)</sub>



----------
### homonyms_count



- getter 


<sub>[top](#{self.page.anchor}) [index](index.md)</sub>



----------
### is_module



- getter 


<sub>[top](#{self.page.anchor}) [index](index.md)</sub>



----------
### is_page



- getter setter


<sub>[top](#{self.page.anchor}) [index](index.md)</sub>



----------
### is_top

Is top section

- getter 
- type **bool**


<sub>[top](#{self.page.anchor}) [index](index.md)</sub>



----------
### module



- getter 


<sub>[top](#{self.page.anchor}) [index](index.md)</sub>



----------
### module_path



- getter 


<sub>[top](#{self.page.anchor}) [index](index.md)</sub>



----------
### page



- getter 


<sub>[top](#{self.page.anchor}) [index](index.md)</sub>



## Methods

----------
### TestStructure



``` python
TestStructure()
```



----------
### __str__



``` python
__str__()
```



----------
### add_class_dict



``` python
add_class_dict(class_dict, ignore_uncommented=False)
```



----------
### add_file_dict



``` python
add_file_dict(file_dict)
```



----------
### add_function_dict



``` python
add_function_dict(func_dict)
```



----------
### add_module



``` python
add_module(module, title, comment=None, **kwargs)
```



----------
### add_page



``` python
add_page(title, comment=None, **kwargs)
```



----------
### add_property_dict



``` python
add_property_dict(prop_dict)
```



----------
### add_section



``` python
add_section(title, comment=None, **kwargs)
```



----------
### append



``` python
append(section)
```



----------
### create_file



``` python
create_file(section)
```



----------
### dump



``` python
dump()
```



----------
### func



``` python
func(section)
```



----------
### get_content

Returns the text to write in the page

``` python
get_content()
```



----------
### get_create_section



``` python
get_create_section(title, comment=None,**kwargs)
```



----------
### get_documentation

Write the section into a dict

``` python
get_documentation(doc_folder=None)
```



#### Arguments

- **doc** (dict) : the dict where to write the documentation

----------
### get_items



``` python
get_items(section)
```



----------
### get_module



``` python
get_module(title, condition=None, **kwargs)
```



----------
### get_page



``` python
get_page(title, condition=None, **kwargs)
```



----------
### get_section



``` python
get_section(title=None, condition=None, **kwargs)
```



----------
### get_toc



``` python
get_toc(title="21")
```



----------
### iteration



``` python
iteration(func, *args, include_top=True)
```



----------
### link_to



``` python
link_to(absolute=True, title=None)
```



----------
### print



``` python
print(text_max=100)
```



----------
### sort



``` python
sort()
```



----------
### test_doc



``` python
test_doc()
```



----------
### test_dump



``` python
test_dump()
```



----------
### test_get



``` python
test_get()
```



----------
### test_self



``` python
test_self()
```



----------
### write

Append text to the header comment

``` python
write(text)
```



#### Arguments

- **text** (str) : the text to write

----------
### write_navigation



``` python
write_navigation()
```



----------
### write_source



``` python
write_source(source)
```

