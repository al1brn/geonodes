# Function



``` python
__init__((, s, e, l, f, ,,  , n, a, m, e, ,,  , c, o, m, m, e, n, t, =, N, o, n, e, ,,  , l, e, v, e, l, =, 1, ))
```

Section dedicated to function documentation.

A **Function** is made of two sections:
- Properties
- Methods

The comment can contain description of Arguments and Returns.
The comment is parsed in order to extract this information and to
write the document is a homogeneous way.




**inherits from** Section 

## Methods and Properties
- A : [arguments](#arguments) [arguments](#arguments) 
- F : [FromDoc](#fromdoc) 
- P : [parse_comment](#parse_comment) 
- R : [returns](#returns) 

# Properties

## arguments

``` python

```





# Methods

## FromDoc

**Decorators**: Class method

``` python
FromDoc((, c, l, s, ,,  , d, o, c, ))
```

Create a class from an instance of Doc

Doc is a class read by the **Parser**.



##### Arguments

- **doc** (_Doc_) : Doc parsed by **Parser**


## arguments

``` python

```




## parse_comment

``` python
parse_comment((, s, e, l, f, ,,  , c, o, m, m, e, n, t, ))
```

Function comment parser

The Function parser extracts Arguments and Returns sections.
The corresponding lines are remove from the comment to feed the two sections.

The lists are generated from the structure




## returns

``` python

```





