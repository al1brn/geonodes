# Section



``` python
Section(self, title, comment=None, level=0, with_sections_only=False, sort_sections=False)
```

Elementary base of a documentation

A **Section** is basically a title and a comment.

It inherits from a list into which sub sections can be stored.
A Section produces documentation:
- Header
- Comment
- Loop on sub sections




> subclasses: [Argument](argument.md) [Return](return.md) [Function](function.md) [Class](class.md) [Classes](classes.md) 

## Methods and Properties
- A : [alphabetical_sections](#alphabetical_sections) 
- B : [build](#build) [build_header](#build_header) [build_sections](#build_sections) 
- C : [comment](#comment) 
- G : [get_section](#get_section) 
- I : [init](#init) 
- L : [link_to](#link_to) 
- M : [md_file_name](#md_file_name) 
- P : [parse_comment](#parse_comment) [print](#print) 
- S : [sorted_sections](#sorted_sections) [sorted_sections](#sorted_sections) 

# Properties

## comment

``` python
Section.comment
```

Comment property



##### Returns

- _str_ : Section header comment


## md_file_name

``` python
Section.md_file_name
```

MD Document file name



##### Returns

- _str_ : markdown file name


## sorted_sections

``` python
Section.sorted_sections
```

Sort the sub sections in alphabetical order



##### Returns

- _List_ : list of the sub sections sorted in alphabetical order



# Methods

## alphabetical_sections

``` python
Section.alphabetical_sections(self, alpha=None)
```

Build a dictionary keyed by the section title initials

Used to diplay a table of content when there is a great number of sections.

```
{'A': ['a section', 'another section',
'O': ['other section']
}
```



##### Arguments

- **alpha** (_dict_ = None) : dictionary to feed

##### Returns

- _dict_


## build

``` python
Section.build(self)
```

Yield the lines of the section

The method yields the lines from method **build_header** and the from
**build_sections**.

If the flag **with_sections_only** is set, nothing is yield if there is no
sub sections.



##### Returns

- _str_ : documentation lines for the sections


## build_header

``` python
Section.build_header(self)
```

Yield the lines of the header part




## build_sections

``` python
Section.build_sections(self)
```

Yield the lines of the sections parts




## get_section

``` python
Section.get_section(self, title)
```

Look for a sub section by its title



##### Arguments

- **title** (_str_) : the section to look for

##### Returns

- _Section_


## init

``` python
Section.init(self)
```




## link_to

``` python
Section.link_to(self, url="")
```

MD link



##### Returns

- _str_ : [title](url + link_token)


## parse_comment

``` python
Section.parse_comment(self, comment)
```

Parse comment to extract information

This method extract information embbeded in the comment and returns the cleaned text.
The default implementation returns the argument without change.



##### Arguments

- **comment** (_str_) : the raw comment

##### Returns

- _str_ : the cleaned comment


## print

``` python
Section.print(self)
```

Print the documentation in the console

For debug purpose.




## sorted_sections

``` python
Section.sorted_sections
```

Sort the sub sections in alphabetical order



##### Returns

- _List_ : list of the sub sections sorted in alphabetical order



