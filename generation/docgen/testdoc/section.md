# Section

Section


Properties
----------
- is_page (bool = False) : is a page if <#module> is not None
- module (string = None) : module the page belongs to, section is not a page if None

``` python
Section(title, comment=None, sort_sections=False, in_toc=False, module=None, is_page=False, ignore_if_empty=True)
```



## Properties

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
----------



## Methods

### TestStructure



``` python
TestStructure()
```



### __str__



``` python
__str__()
```



### add_class_dict



``` python
add_class_dict(class_dict, ignore_uncommented=False)
```



### add_file_dict



``` python
add_file_dict(file_dict)
```



### add_function_dict



``` python
add_function_dict(func_dict)
```



### add_module



``` python
add_module(module, title, comment=None, **kwargs)
```



### add_page



``` python
add_page(title, comment=None, **kwargs)
```



### add_property_dict



``` python
add_property_dict(prop_dict)
```



### add_section



``` python
add_section(title, comment=None, **kwargs)
```



### append



``` python
append(section)
```



### create_file



``` python
create_file(section)
```



### dump



``` python
dump()
```



### func



``` python
func(section)
```



### get_content

Returns the text to write in the page

``` python
get_content()
```



### get_create_section



``` python
get_create_section(title, comment=None,**kwargs)
```



### get_documentation

Write the section into a dict

``` python
get_documentation(doc_folder=None)
```



#### Arguments

- **doc** (dict) : the dict where to write the documentation

### get_module



``` python
get_module(title, condition=None, **kwargs)
```



### get_page



``` python
get_page(title, condition=None, **kwargs)
```



### get_section



``` python
get_section(title=None, condition=None, **kwargs)
```



### iteration



``` python
iteration(func, *args, include_top=True)
```



### link_to



``` python
link_to(absolute=True, title=None)
```



### print



``` python
print(text_max=100)
```



### sort



``` python
sort()
```



### test_doc



``` python
test_doc()
```



### test_dump



``` python
test_dump()
```



### test_get



``` python
test_get()
```



### test_self



``` python
test_self()
```



### write

Append text to the header comment

``` python
write(text)
```



#### Arguments

- **text** (str) : the text to write

### write_navigation



``` python
write_navigation()
```



### write_source



``` python
write_source(source)
```

