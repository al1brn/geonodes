# Function

``` python Function(self, name, comment=None, level=1)
```

Section dedicated to function documentation.

A **Function** is made of two sections:
- Properties
- Methods

The comment can contain description of Arguments and Returns. The comment is parsed in order to extract this information and to write the document is a homogeneous way.




> inherits from: [Section](section.md) 

> inherited: [alphabetical_sections](section.md#alphabetical_sections), [build](section.md#build), [build_extra](section.md#build_extra), [build_header](section.md#build_header), [build_sections](section.md#build_sections), [comment](section.md#comment), [extra](section.md#extra), [get_section](section.md#get_section), [level](section.md#level), [link_to](section.md#link_to), [link_token](section.md#link_token), [md_file_name](section.md#md_file_name), [new_section](section.md#new_section), [print](section.md#print), [sort_sections](section.md#sort_sections), [sorted_sections](section.md#sorted_sections), [title](section.md#title), [with_sections_only](section.md#with_sections_only), [write](section.md#write)
## Methods and Properties
- A : [arguments](#arguments) 
- F : [FromDoc](#fromdoc) 
- I : [init](#init) 
- P : [parse_comment](#parse_comment) 
- R : [returns](#returns) 

# Properties

## arguments

``` python Function.arguments
```



##### Returns

- _Section_ : title is 'Arguments', sub sections are [Argument](#argument)



<sub>[top](#function) [index](index.md)</sub>

# Methods

## FromDoc

> **Decorators**: Class method

``` python Function.FromDoc(cls, doc, class_name=None)
```

Create a class from an instance of Doc

Doc is a class read by the **Parser**.



##### Arguments

- **doc** (_Doc_) : Doc parsed by **Parser**



<sub>[top](#function) [index](index.md)</sub>
## init

``` python Function.init(self)
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

``` python Function.parse_comment(self, comment)
```

Function comment parser

The Function parser extracts Arguments and Returns sections. The corresponding lines are remove from the comment to feed the two sections.

The lists are generated from the structure





<sub>[top](#function) [index](index.md)</sub>
## returns

``` python Function.returns
```



##### Returns

- _Section_ : title is 'Arguments', sub sections are [Return](#return)



<sub>[top](#function) [index](index.md)</sub>

