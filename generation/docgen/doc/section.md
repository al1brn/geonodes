# Section



``` python
Section(self, title, comment=None, level=0, **kwargs)
```

Elementary base of a documentation

A **Section** is basically a title, a header section and sub sections

It inherits from a list into which sub sections are stored. A Section produces documentation:
- Header (level 0)
- Header
- Table of content section (level 1)
- Loop on sub sections (level 1)
- Extra (for intrapage links)




> subclasses: [Argument](argument.md) [Return](return.md) [Function](function.md) [Class](class.md) 

## Methods and Properties
- A : [alphabetical_sections](#alphabetical_sections) [as_dict](#as_dict) 
- B : [build](#build) [build_extra](#build_extra) [build_header](#build_header) [build_sections](#build_sections) 
- C : [comment](#comment) 
- E : [extra](#extra) 
- F : [fixed_level](#fixed_level) 
- G : [get_section](#get_section) 
- I : [in_toc](#in_toc) [init](#init) [iteration](#iteration) 
- L : [link_to](#link_to) [link_token](#link_token) 
- M : [md_file_name](#md_file_name) [md_file_name](#md_file_name) 
- N : [new_section](#new_section) 
- P : [page](#page) [parse_comment](#parse_comment) [print](#print) 
- S : [sort_sections](#sort_sections) [sorted_sections](#sorted_sections) [sorted_sections](#sorted_sections) 
- T : [title](#title) [toc](#toc) 
- W : [with_sections_only](#with_sections_only) [write](#write) 

# Properties



## as_dict

``` python
Section.as_dict
```



##### Returns



- _dict_ : section title: section



<sub>[top](#section) [index](index.md)</sub>
## comment

``` python
Section.comment
```

Comment property



##### Returns



- _str_ : Section header comment



<sub>[top](#section) [index](index.md)</sub>
# extra

Extra text at the end of the documentation



##### Returns



- _str_ : 



<sub>[top](#section) [index](index.md)</sub>
# fixed_level

level is fixed and can't be changed



##### Returns



- _bool_ : 



<sub>[top](#section) [index](index.md)</sub>
# in_toc

section is included in the owner section table of content



##### Returns



- _bool_ : 



<sub>[top](#section) [index](index.md)</sub>
## md_file_name

``` python
Section.md_file_name
```

MD Document file name



##### Returns



- _str_ : markdown file name



<sub>[top](#section) [index](index.md)</sub>
# page




##### Returns



- _None_ : 



<sub>[top](#section) [index](index.md)</sub>
# sort_sections

The sections are placed in alphabetical order



##### Returns



- _bool_ : 



<sub>[top](#section) [index](index.md)</sub>
## sorted_sections

``` python
Section.sorted_sections
```

Sort the sub sections in alphabetical order



##### Returns



- _List_ : list of the sub sections sorted in alphabetical order



<sub>[top](#section) [index](index.md)</sub>
# title

Section title



##### Returns



- _str_ : 



<sub>[top](#section) [index](index.md)</sub>
# toc

name of the toc section, None if no toc is generated



##### Returns



- _str_ : 



<sub>[top](#section) [index](index.md)</sub>
# with_sections_only

The section is printed only if the list of sub sections is not empty



##### Returns



- _bool_ : 



<sub>[top](#section) [index](index.md)</sub>

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



- _dict_ : 



<sub>[top](#section) [index](index.md)</sub>
## build

``` python
Section.build(self)
```

Yield the lines of the section

The method yields the lines from method **build_header** and the from
**build_sections**.

If the flag **with_sections_only** is set, nothing is yield if there is no sub sections.



##### Returns



- _str_ : documentation lines for the sections



<sub>[top](#section) [index](index.md)</sub>
## build_extra

``` python
Section.build_extra(self)
```

Yield extra lines at the end of the section documentation





<sub>[top](#section) [index](index.md)</sub>
## build_header

``` python
Section.build_header(self)
```

Yield the lines of the header part





<sub>[top](#section) [index](index.md)</sub>
## build_sections

``` python
Section.build_sections(self)
```

Yield the lines of the sections parts





<sub>[top](#section) [index](index.md)</sub>
## get_section

``` python
Section.get_section(self, title)
```

Look for a sub section by its title

> [!NOTE]
> This function searches only in the direct children, not in the whole tree.

To search a section in the whole tree, use [iteration](#) method:

``` python
sub_section = parent_section.iteration(lambda s: s.title == 'The title')
```



##### Arguments



- **title** (_str_) : the section to look for

##### Returns



- _Section_ : 



<sub>[top](#section) [index](index.md)</sub>
## init

``` python
Section.init(self)
```

Class initialisation

This complementary initialisation takes place at the end of **__init__**, before
[parse_comment](#parse_comment) is called.

Allows to initialize attributes which are used in [parse_comment](#parse_comment) method.

Default method is empty.





<sub>[top](#section) [index](index.md)</sub>
## iteration

``` python
Section.iteration(self, f)
```

Run the function on the section and sub sections

The method halts on the first section for which the function return `True` and returns this section. If the function doesn't return `True`, the methods is run on all sections and return `None`.



##### Arguments



- **f** : 

##### Returns



- _Section_ : 



<sub>[top](#section) [index](index.md)</sub>
## link_to

``` python
Section.link_to(self, url="")
```

MD link



##### Returns



- _str_ : [title](url + link_token)



<sub>[top](#section) [index](index.md)</sub>
## link_token

``` python
Section.link_token
```

MD link token

The markdown token is the lower case title where spaces are replaces by '-' char



##### Returns



- _str_ : markdown token



<sub>[top](#section) [index](index.md)</sub>
## md_file_name

``` python
Section.md_file_name
```

MD Document file name



##### Returns



- _str_ : markdown file name



<sub>[top](#section) [index](index.md)</sub>
## new_section

``` python
Section.new_section(self, title, comment=None, sub_level=1)
```

Add a sub section



##### Arguments



- **title** (_str_) : section title
- **comment** (_str_) : header comment
- **sub_level** (_int_ = 1) : level increment

##### Returns



- _Section_ : 



<sub>[top](#section) [index](index.md)</sub>
## parse_comment

``` python
Section.parse_comment(self, comment)
```

Parse comment to extract information

This method extract information embbeded in the comment and returns the cleaned text. The default implementation normalizes the markdwon comment.



##### Arguments



- **comment** (_str_) : the raw comment

##### Returns



- _str_ : the cleaned comment



<sub>[top](#section) [index](index.md)</sub>
## print

``` python
Section.print(self)
```

Print the documentation in the console

For debug purpose.





<sub>[top](#section) [index](index.md)</sub>
## sorted_sections

``` python
Section.sorted_sections
```

Sort the sub sections in alphabetical order



##### Returns



- _List_ : list of the sub sections sorted in alphabetical order



<sub>[top](#section) [index](index.md)</sub>
## write

``` python
Section.write(self, comment='\n', parse=True)
```

Append text to the current text

The current text is either the comment if this section if there is not sub sections, or the comment of the last sub sections.



##### Arguments



- **comment** (_str_) : the text to write
- **parse** (_bool_ = True) : parse the comment



<sub>[top](#section) [index](index.md)</sub>

