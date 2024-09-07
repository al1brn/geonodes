# Function



``` python
Function(self, name, comment=None, level=1)
```

Section dedicated to function documentation.

A **Function** is made of two sections:
- Properties
- Methods

The comment can contain description of Arguments and Returns.
The comment is parsed in order to extract this information and to
write the document is a homogeneous way.




> inherits from: [Section](section.md) 

## Methods and Properties
- A : [arguments](#arguments) [arguments](#arguments) 
- F : [FromDoc](#fromdoc) 
- P : [parse_comment](#parse_comment) 
- R : [returns](#returns) 

# Properties

## arguments

``` python
Function.arguments
```





# Methods

## FromDoc

> **Decorators**: Class method

``` python
Function.FromDoc(cls, doc, class_name=None)
```

Create a class from an instance of Doc

Doc is a class read by the **Parser**.


Create additional comment


##### Arguments

- **doc** (_Doc_) : Doc parsed by **Parser**


## arguments

``` python
Function.arguments
```




## parse_comment

``` python
Function.parse_comment(self, comment)
```

Function comment parser

The Function parser extracts Arguments and Returns sections.
The corresponding lines are remove from the comment to feed the two sections.

The lists are generated from the structure




## returns

``` python
Function.returns
```





