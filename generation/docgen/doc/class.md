# Class



``` python
Class(self, class_name, comment)
```




> inherits from: [Section](section.md) 
> [alphabetical_sections](section.md#alphabetical_sections), [build_header](section.md#build_header), [build_sections](section.md#build_sections), [comment](section.md#comment), [get_section](section.md#get_section), [init](section.md#init), [link_to](section.md#link_to), [link_token](section.md#link_token), [md_file_name](section.md#md_file_name), [parse_comment](section.md#parse_comment), [print](section.md#print), [sorted_sections](section.md#sorted_sections)

## Methods and Properties
- B : [build](#build) 
- C : [capture_class](#capture_class) [compile](#compile) 
- M : [methods](#methods) 
- P : [properties](#properties) [properties](#properties) 

# Properties

## properties

``` python
Class.properties
```





# Methods

## build

``` python
Class.build(self)
```

__init__ comment as class comment



## capture_class

``` python
Class.capture_class(self, other)
```




## compile

``` python
Class.compile(self, classes)
```

Compile links with other classes

**classes** argument is a dict of **Class**:
- Load each class based on this one into to the **subclasses** attribute.
- Load the methods and properties inherited from parent classes



##### Arguments

- **classes** (_dict_) : dict of _Class_


## methods

``` python
Class.methods
```




## properties

``` python
Class.properties
```





