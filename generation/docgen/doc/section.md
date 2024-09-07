# Section



Elementary base of a documentation

A **Section** is basically a title and a comment.

It inherits from a list into which sub sections can be stored.
A Section produces documentation:
- Header
- Comment
- Loop on sub sections



# Methods
- A : [alphabetical_sections](#alphabetical_sections) 
- B : [build](#build) [build_header](#build_header) [build_sections](#build_sections) 
- G : [get_section](#get_section) 
- L : [link_to](#link_to) [link_token](#link_token) 
- M : [md_file_name](#md_file_name) 
- P : [print](#print) 
- S : [sorted_sections](#sorted_sections) 

## alphabetical_sections

Build a dictionary keyed by the section title initials

Used to diplay a table of content when there is a great number of sections.

```
{'A': ['a section', 'another section',
'O': ['other section']
}
```



$${\color{blue}\large\textsf{Returns}}$$:\n- _dict_



## build

Yield the lines of the section

The method yields the lines from method **build_header** and the from
**build_sections**.

If the flag **with_sections_only** is set, nothing is yield if there is no
sub sections.



$${\color{blue}\large\textsf{Returns}}$$:\n- _str_ : documentation lines for the sections



## build_header

Yield the lines of the header part





## build_sections

Yield the lines of the sections parts





## get_section

Look for a sub section by its title



$${\color{blue}\large\textsf{Arguments}}$$:\n- **title** (_str_) : the section to look for

$${\color{blue}\large\textsf{Returns}}$$:\n- _Section_



## link_to

MD link



$${\color{blue}\large\textsf{Returns}}$$:\n- _str_ : [title](url + link_token)



## link_token

MD link token

The markdown token is the lower case title where spaces are replaces by '-' char



$${\color{blue}\large\textsf{Returns}}$$:\n- _str_ : markdown token



## md_file_name

MD Document file name



$${\color{blue}\large\textsf{Returns}}$$:\n- _str_ : markdown file name



## print

Print the documentation in the console

For debug purpose.





## sorted_sections

Sort the sub sections in alphabetical order



$${\color{blue}\large\textsf{Returns}}$$:\n- _List_ : list of the sub sections sorted in alphabetical order



