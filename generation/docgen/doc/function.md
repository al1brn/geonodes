# Function




> inherits from: [Section](section.md) 

> inherited: [FromSource](section.md#fromsource), [__init__](section.md#__init__), [alphabetical_sections](section.md#alphabetical_sections), [as_dict](section.md#as_dict), [build](section.md#build), [build_extra](section.md#build_extra), [build_header](section.md#build_header), [build_sections](section.md#build_sections), [comment](section.md#comment), [extra](section.md#extra), [fixed_level](section.md#fixed_level), [get_section](section.md#get_section), [in_toc](section.md#in_toc), [iteration](section.md#iteration), [level](section.md#level), [link_to](section.md#link_to), [link_token](section.md#link_token), [md_file_name](section.md#md_file_name), [new_section](section.md#new_section), [page](section.md#page), [print](section.md#print), [sort_sections](section.md#sort_sections), [sorted_sections](section.md#sorted_sections), [title](section.md#title), [toc](section.md#toc), [with_sections_only](section.md#with_sections_only), [write](section.md#write)
## Methods and Properties
- A : [arguments](#arguments) 
- F : [FromDoc](#fromdoc) 
- I : [init](#init) 
- P : [parse_comment](#parse_comment) 
- R : [returns](#returns) 

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

