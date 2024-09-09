# Function


> inherits from: [Section](section.md) 

> inherited: [FromSource](section.md#section), [__init__](section.md#section), [alphabetical_sections](section.md#section), [as_dict](section.md#section), [build](section.md#section), [build_extra](section.md#section), [build_header](section.md#section), [build_sections](section.md#section), [comment](section.md#section), [extra](section.md#section), [fixed_level](section.md#section), [get_section](section.md#section), [in_toc](section.md#section), [iteration](section.md#section), [level](section.md#section), [link_to](section.md#section), [link_token](section.md#section), [md_file_name](section.md#section), [new_section](section.md#section), [page](section.md#section), [print](section.md#section), [sort_sections](section.md#section), [sorted_sections](section.md#section), [title](section.md#section), [toc](section.md#section), [with_sections_only](section.md#section), [write](section.md#section), [write_header](section.md#section)


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

