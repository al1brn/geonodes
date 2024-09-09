# Function



# Properties



## arguments

``` python
Function.arguments
```



##### Returns



- _Section_ : title is 'Arguments', sub sections are [Argument](#argument)



<sub>[top](#function) [index](index.md)</sub>

# Methods



## FromDoc

> **Decorators**: Class method

``` python
Function.FromDoc(cls, doc, class_name=None, **kwargs)
```

Create a class from an instance of Doc

Doc is a class read by the **Parser**.



##### Arguments



- **doc** (_Doc_) : Doc parsed by **Parser**



<sub>[top](#function) [index](index.md)</sub>
## init

``` python
Function.init(self)
```

Function section specific init

A Function section is made of two sections:
- Arguments
- Returns

It also create stores other information:
- decorators
- arguments





<sub>[top](#function) [index](index.md)</sub>
## parse_comment

``` python
Function.parse_comment(self, comment)
```

Function comment parser

The Function parser extracts Arguments and Returns sections. The corresponding lines are remove from the comment to feed the two sections.

The lists are generated from the structure





<sub>[top](#function) [index](index.md)</sub>
## returns

``` python
Function.returns
```



##### Returns



- _Section_ : title is 'Arguments', sub sections are [Return](#return)



<sub>[top](#function) [index](index.md)</sub>

