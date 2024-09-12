# pyparser


Created on Wed Jun  8 09:00:41 2022

@author: alain.bernard@loreal.com


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

### Reader

Simple python source code parser.

#### Properties

##### eol

End of line flag> type Boolean


###### Getter

End of line flag

``` python
eol()
```



####### Returns

- **Boolean** : True if end of line is reached, False otherwise

##### eof

End of file flag> type Boolean


###### Getter

End of file flag

``` python
eof()
```



####### Returns

- **Boolean** : True if end of file is reached, False otherwise

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

##### previous

Read the previous char> type str


###### Getter

Read the previous char

``` python
previous()
```



####### Returns

- **str** : Previous character or None if start of file

#### Methods



``` python
Reader(text)
```



#### __init__



##### FromFile

Initialize a parser from a file.

``` python
FromFile(fname)
```



###### Arguments

- **fname** (str) : full path of the file top parse

##### reset

Reset the cursor to the start of the text

``` python
reset()
```



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

#### Properties

#### Methods



``` python
Doc(match)
```



#### __init__



