# Function




> inherits from: [Section](section.md) 

> inherited: <!Section#FromSource>, <!Section#__init__>, <!Section#alphabetical_sections>, <!Section#as_dict>, <!Section#build>, <!Section#build_extra>, <!Section#build_header>, <!Section#build_sections>, <!Section#comment>, <!Section#extra>, <!Section#fixed_level>, <!Section#get_section>, <!Section#in_toc>, <!Section#iteration>, <!Section#level>, <!Section#link_to>, <!Section#link_token>, <!Section#md_file_name>, <!Section#new_section>, <!Section#page>, <!Section#print>, <!Section#sort_sections>, <!Section#sorted_sections>, <!Section#title>, <!Section#toc>, <!Section#with_sections_only>, <!Section#write>
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

