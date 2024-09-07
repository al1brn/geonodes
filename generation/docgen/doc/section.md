# Section



Elementary base of a documentation

A **Section** is basically a title and a comment.

It inherits from a list into which sub sections can be stored.
A Section produces documentation:
- Header
- Comment
- Loop on sub sections



# Methods
- M : md_file_name 
- L : link_token link_to 
- G : get_section 
- S : sorted_sections 
- A : alphabetical_sections 
- B : build_header build_sections build 
- P : print 

## Methods

### md_file_name

MD Document file name



***Returns***:
- _str_ : markdown file name


### link_token

MD link token

The markdown token is the lower case title where spaces are replaces by '-' char



***Returns***:
- _str_ : markdown token


### link_to

MD link



***Returns***:
- _str_ : [title](url + link_token)


### get_section

Look for a sub section by its title



***Arguments***:
- **title** (_str_) : the section to look for

***Returns***:
- _Section_


### sorted_sections

Sort the sub sections in alphabetical order



***Returns***:
- _List_ : list of the sub sections sorted in alphabetical order


### alphabetical_sections

Build a dictionary keyed by the section title initials

Used to diplay a table of content when there is a great number of sections.

```
{'A': ['a section', 'another section',
'O': ['other section']
}
```



***Returns***:
- _dict_


### build_header

Yield the lines of the header part




### build_sections

Yield the lines of the sections parts




### build

Yield the lines of the section

The method yields the lines from method **build_header** and the from
**build_sections**.

If the flag **with_sections_only** is set, nothing is yield if there is no
sub sections.



***Returns***:
- _str_ : documentation lines for the sections


### print

Print the documentation in the console

For debug purpose.






