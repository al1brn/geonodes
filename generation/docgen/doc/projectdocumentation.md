# ProjectDocumentation



``` python
ProjectDocumentation(self, name)
```



## Methods and Properties
- A : [add_class](#add_class) [add_module](#add_module) 
- C : [compile](#compile) 
- F : [FromFiles](#fromfiles) 
- G : [get_module_class](#get_module_class) 
- W : [write_documentation](#write_documentation) [write_index](#write_index) 

# Methods

## FromFiles

> **Decorators**: Class method

``` python
ProjectDocumentation.FromFiles(cls, name, folder, sub_folders=[])
```




## add_class

``` python
ProjectDocumentation.add_class(self, class_name, module_name=None, bases=[], capture=[])
```




## add_module

``` python
ProjectDocumentation.add_module(self, name, text)
```




## compile

``` python
ProjectDocumentation.compile(self)
```




## get_module_class

``` python
ProjectDocumentation.get_module_class(self, class_name, module_name=None, halt=True)
```




## write_documentation

``` python
ProjectDocumentation.write_documentation(self, doc_folder)
```




## write_index

``` python
ProjectDocumentation.write_index(self, file_name)
```

Write the index file



##### Arguments

- **file_name** (_str_) : file name to write



