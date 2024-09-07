# Class



``` python
Class(self, class_name, comment)
```




> inherits from: [Section](section.md) 

## Methods and Properties
- B : [build](#build) 
- C : [capture_class](#capture_class) 
- L : [load_subclasses](#load_subclasses) 
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




## load_subclasses

``` python
Class.load_subclasses(self, classes)
```

Load the subclasses registers in classes

**classes** argument is a dict of **Class**. Load each class based on this one
into to the **subclasses** attribute.



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





