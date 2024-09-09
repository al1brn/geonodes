# Class

``` python
Class(self, class_name, comment)
```

Section documenting a class

The structure of the document is:
- title (class name)
- header comment
- properties & methods table of contents
- Properties section with the documented properties as sub sections
- Methods section withe the documented methods as sub sections

The class documentation is completed afterward by the [compile](#compile) method which get the links coming from inheritance between classes.




> inherits from: [Section](section.md) 

> inherited: [add_hook](section.md#add_hook), [alphabetical_sections](section.md#alphabetical_sections), [build_extra](section.md#build_extra), [build_header](section.md#build_header), [build_sections](section.md#build_sections), [comment](section.md#comment), [extra](section.md#extra), [get_section](section.md#get_section), [init](section.md#init), [level](section.md#level), [link_to](section.md#link_to), [link_token](section.md#link_token), [md_file_name](section.md#md_file_name), [new_section](section.md#new_section), [parse_comment](section.md#parse_comment), [print](section.md#print), [sort_sections](section.md#sort_sections), [sorted_sections](section.md#sorted_sections), [title](section.md#title), [with_sections_only](section.md#with_sections_only), [write](section.md#write)
## Methods and Properties
- B : [build](#build) 
- C : [capture_class](#capture_class) [compile](#compile) 
- F : [FromDoc](#fromdoc) 
- M : [methods](#methods) 
- P : [properties](#properties) 

# Properties

## properties

``` python
Class.properties
```



##### Returns

- _Section_ : title is 'Properties', sub sections are documented properties



<sub>[top](#class) [index](index.md)</sub>

# Methods

## FromDoc

> **Decorators**: Class method

``` python
Class.FromDoc(cls, doc, ignore_uncommented=True)
```

Creates a Class document from a Doc parsed from source file

The **doc** argument contains the list of documents methods and properties.



##### Arguments

- **doc** (_Doc_) : Doc parsed from a sourc file
- **exclude_uncommented** (_bool_ = True) : exclude the methods which are not commented in the source file

##### Returns

- _Class_ : document on the class



<sub>[top](#class) [index](index.md)</sub>
## build

``` python
Class.build(self)
```

Yield the Class documentation lines





<sub>[top](#class) [index](index.md)</sub>
## capture_class

``` python
Class.capture_class(self, other)
```

Capture methods and properties from another Class

This method allows to get the documentation of inherited items of a class which is not documentated.



##### Arguments

- **other** (_Class_) : class to copy methods and properties from

##### Returns

- _self_



<sub>[top](#class) [index](index.md)</sub>
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



<sub>[top](#class) [index](index.md)</sub>
## methods

``` python
Class.methods
```

Methods Section



##### Returns

- _Section_ : title is 'Methods', sub sections are documented methods



<sub>[top](#class) [index](index.md)</sub>

