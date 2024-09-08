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

The class documentation is completed afterward by the [compile](#compile) method
which get the links coming from inheritance between classes.




> inherits from: [Section](section.md) 

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

Properties Section



##### Returns

- _Section_ : title is 'Properties', sub sections are documented properties



# Methods

## FromDoc

> **Decorators**: Class method

``` python
Class.FromDoc(cls, doc, ignore_uncommented=True)
```

Creates a Class document from a Doc parsed from source file

The **doc** argument contains the list of documents methods and properties.


in the source file



##### Arguments

- **doc** (_Doc_) : Doc parsed from a sourc file
- **exclude_uncommented** (_bool_ = True) : exclude the methods which are not commented

##### Returns

- _Class_ : document on the class


## build

``` python
Class.build(self)
```

Yield the Class documentation lines




## capture_class

``` python
Class.capture_class(self, other)
```

Capture methods and properties from another Class

This method allows to get the documentation of inherited items of a class
which is not documentated.



##### Arguments

- **other** (_Class_) : class to copy methods and properties from

##### Returns

- _self_


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

Methods Section



##### Returns

- _Section_ : title is 'Methods', sub sections are documented methods



