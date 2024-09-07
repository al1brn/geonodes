# Section



``` python
__init__((, s, e, l, f, ,,  , t, i, t, l, e, ,,  , c, o, m, m, e, n, t, =, N, o, n, e, ,,  , l, e, v, e, l, =, 0, ,,  , w, i, t, h, _, s, e, c, t, i, o, n, s, _, o, n, l, y, =, F, a, l, s, e, ,,  , s, o, r, t, _, s, e, c, t, i, o, n, s, =, F, a, l, s, e, ))
```

Elementary base of a documentation

A **Section** is basically a title and a comment.

It inherits from a list into which sub sections can be stored.
A Section produces documentation:
- Header
- Comment
- Loop on sub sections



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
comment((, s, e, l, f, ))
```

Comment property



##### Returns

- _str_ : Section header comment


## md_file_name

``` python
md_file_name((, s, e, l, f, ))
```

MD Document file name



##### Returns

- _str_ : markdown file name


## sorted_sections

``` python
sorted_sections((, s, e, l, f, ))
```

Sort the sub sections in alphabetical order



##### Returns

- _List_ : list of the sub sections sorted in alphabetical order



# Methods

## alphabetical_sections

``` python
alphabetical_sections((, s, e, l, f, ,,  , a, l, p, h, a, =, N, o, n, e, ))
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
build((, s, e, l, f, ))
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
build_header((, s, e, l, f, ))
```

Yield the lines of the header part




## build_sections

``` python
build_sections((, s, e, l, f, ))
```

Yield the lines of the sections parts




## get_section

``` python
get_section((, s, e, l, f, ,,  , t, i, t, l, e, ))
```

Look for a sub section by its title



##### Arguments

- **title** (_str_) : the section to look for

##### Returns

- _Section_


## init

``` python
init((, s, e, l, f, ))
```




## link_to

``` python
link_to((, s, e, l, f, ,,  , u, r, l, =, ", ", ))
```

MD link



##### Returns

- _str_ : [title](url + link_token)


## parse_comment

``` python
parse_comment((, s, e, l, f, ,,  , c, o, m, m, e, n, t, ))
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
print((, s, e, l, f, ))
```

Print the documentation in the console

For debug purpose.




## sorted_sections

``` python
sorted_sections((, s, e, l, f, ))
```

Sort the sub sections in alphabetical order



##### Returns

- _List_ : list of the sub sections sorted in alphabetical order



