# pyparser


Created on Wed Jun  8 09:00:41 2022

@author: alain.bernard@loreal.com


## Content

[Doc](#doc)
- [Reader](#reader)
- [md_normalize](#md_normalize)

## Functions

### md_normalize

Normalize markdown text

Merge the lines not separated by a blank line

``` python
md_normalize(text)
```



#### Arguments

- **text** (srt) : the mark down text to normalize

#### Returns

- **str** : normalized mark down text

## Classes

### Doc

Item documentation

This class stores the documentation of a functions or a class.
In addition to the doc, it contains complementary information:
- function:
  - args : call arguments
  - decorators : list of decorators
- class:
  - bases : list of classes it inherits from
  - funcs : dict of method docs

The class is initialized with the not null result of the regular expression:

``` match = re.search(r"(def|class)\s+(\w+)([^:]*)", line) ```

which returns:
1. def | class
2. name
3. args | base class

#### Content



#### Properties

#### Methods



``` python
Doc(match)
```



### Reader

Simple python source code parser.

#### Content

[FromFile](#fromfile)
- [back](#back)
- [current](#current)
- [eof](#eof)
- [eol](#eol)
- [equal](#equal)
- [previous](#previous)
- [read](#read)
- [reset](#reset)

#### Properties

##### current

Read the current char

Getting the current char doesn't move the cursor.> type str


###### Getter

Read the current char

Getting the current char doesn't move the cursor.

``` python
current()
```



####### Returns

- **str** : Next character or None if end of file

##### eof

End of file flag> type Boolean


###### Getter

End of file flag

``` python
eof()
```



####### Returns

- **Boolean** : True if end of file is reached, False otherwise

##### eol

End of line flag> type Boolean


###### Getter

End of line flag

``` python
eol()
```



####### Returns

- **Boolean** : True if end of line is reached, False otherwise

##### previous

Read the previous char> type str


###### Getter

Read the previous char

``` python
previous()
```



####### Returns

- **str** : Previous character or None if start of file

##### read

Read the next char

After reading, the cursor is incremented> type str


###### Getter

Read the next char

After reading, the cursor is incremented

``` python
read()
```



####### Returns

- **str** : Next character or None if end of file

#### Methods



``` python
Reader(text)
```



##### FromFile

Initialize a parser from a file.

``` python
FromFile(fname)
```



###### Arguments

- **fname** (str) : full path of the file top parse

##### back

Move the cursor one step backwards

``` python
back()
```



##### equal

Compare the string starting at the cursor with the argument

``` python
equal(s)
```



###### Arguments

- **s** (str) : the string to compare with

###### Returns

- **Boolean** : True if the text at the cursor is equal to the argument

##### reset

Reset the cursor to the start of the text

``` python
reset()
```



