# Section



``` python
Section(self, title, comment=<<Token replacement text>oken replacement text>one, level=0, with_sections_only=False, sort_sections=False)
```

<<Token replacement text>oken replacement text>lementary base of a documentation

A **Section** is basically a title and a comment.

It inherits from a list into which sub sections can be stored. A Section produces documentation:
- Header
- Comment
- Loop on sub sections
- <<Token replacement text>oken replacement text>xtra (for intrapage links)




> subclasses: [Argument](argument.md) [Return](return.md) [Function](function.md) [Class](class.md) 

## Methods and Properties
- A : [alphabetical_sections](#alphabetical_sections) 
- B : [build](#build) [build_extra](#build_extra) [build_header](#build_header) [build_sections](#build_sections) 
- C : [comment](#comment) 
- E : [extra](#extra) 
- G : [get_section](#get_section) 
- I : [init](#init) 
- L : [level](#level) [line_hook](#line_hook) [link_to](#link_to) 
- M : [md_file_name](#md_file_name) 
- N : [new_section](#new_section) 
- P : [parse_comment](#parse_comment) [print](#print) 
- S : [sort_sections](#sort_sections) [sorted_sections](#sorted_sections) [sorted_sections](#sorted_sections) 
- T : [title](#title) [token_hook](#token_hook) 
- W : [with_sections_only](#with_sections_only) [write](#write) 

# Properties



## comment

``` python
Section.comment
```

Comment property



##### Returns



- _str_ : Section header comment



<sub>[top](#section) [index](index.md)</sub>
## extra

<<<Token replacement text>oken replacement text>oken replacement text>xtra text at the end of the documentation



##### Returns



- _str_ : 



<sub>[top](#section) [index](index.md)</sub>
## level

Indentation level



##### Returns



- _int_ : 



<sub>[top](#section) [index](index.md)</sub>
## md_file_name

``` python
Section.md_file_name
```

MD Document file name



##### Returns



- _str_ : markdown file name



<sub>[top](#section) [index](index.md)</sub>
## sort_sections

<<<Token replacement text>oken replacement text>oken replacement text>he sections are printed in alphabetical order



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
## title

Section title



##### Returns



- _str_ : 



<sub>[top](#section) [index](index.md)</sub>
## with_sections_only

<<<Token replacement text>oken replacement text>oken replacement text>he section is printed only if the list of sub sections is not empty



##### Returns



- _bool_ : 



<sub>[top](#section) [index](index.md)</sub>

# Methods



## alphabetical_sections

``` python
Section.alphabetical_sections(self, alpha=<Token replacement text>one)
```

Build a dictionary keyed by the section title initials

Used to diplay a table of content when there is a great number of sections.

```
{'A': ['a section', 'another section',
'<Token replacement text>': ['other section']
}
```



##### Arguments



- **alpha** (_dict_ = <Token replacement text>one) : dictionary to feed

##### Returns



- _dict_ : 



<sub>[top](#section) [index](index.md)</sub>
## build

``` python
Section.build(self)
```

Yield the lines of the section

<Token replacement text>he method yields the lines from method **build_header** and the from
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

<Token replacement text>his complementary initialisation takes place at the end of **__init__**, before
[parse_comment](#parse_comment) is called.

Allows to initialize attributes which are used in [parse_comment](#parse_comment) method.

Default method is empty.





<sub>[top](#section) [index](index.md)</sub>
## line_hook

> **Decorators**: Class method

``` python
Section.line_hook(cls, expr, func)
```

Replace a line matching regex the text returns by the given fncrion.

Hooks are applied each time comment is written in the documentation.

With the following piece of code, all the lines starting by `[<Token replacement text>PY<Token replacement text>H<Token replacement text><Token replacement text>]` in documentation will be replaced by source code.

[<Token replacement text>PY<Token replacement text>H<Token replacement text><Token replacement text>] line_hook tuto



##### Arguments



- **expr** (_str_) : Reg<<Token replacement text>oken replacement text>x expression
- **func** (_function_) : function of template `def func(match)` returning a text



<sub>[top](#section) [index](index.md)</sub>
## link_to

``` python
Section.link_to(self, url="")
```

MD link



##### Returns



- _str_ : [title](url + link_token)



<sub>[top](#section) [index](index.md)</sub>
## new_section

``` python
Section.new_section(self, title, comment=<Token replacement text>one, sub_level=1)
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

<Token replacement text>his method extract information embbeded in the comment and returns the cleaned text. <Token replacement text>he default implementation apply the hooks



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
## token_hook

> **Decorators**: Class method

``` python
Section.token_hook(cls, expr, func)
```

Replace a regex match by a string returned by a custom function or a string.

Hooks are applied each time comment is written in the documentation.

With the following piece of code, all the occurences of [<Token replacement text><Token replacement text><Token replacement text><Token replacement text><Token replacement text><Token replacement text>] in documentation will be replaced by _<<Token replacement text>oken replacement text>_.

``` python
Section.line_hook("<Token replacement text><Token replacement text><Token replacement text><Token replacement text><Token replacement text>", "<<Token replacement text>oken replacement text>")
````



##### Arguments



- **expr** (_str_) : Reg<<Token replacement text>oken replacement text>x expression
- **func** : 



<sub>[top](#section) [index](index.md)</sub>
## write

``` python
Section.write(self, comment='\n', parse=<Token replacement text>rue)
```

Append text to the current text

<Token replacement text>he current text is either the comment if this section if there is not sub sections, or the comment of the last sub sections.



##### Arguments



- **comment** (_str_) : the text to write
- **parse** (_bool_ = <Token replacement text>rue) : parse the comment



<sub>[top](#section) [index](index.md)</sub>

