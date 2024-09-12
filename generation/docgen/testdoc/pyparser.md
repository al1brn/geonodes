# pyparser {#pyparser}


Created on Wed Jun  8 09:00:41 2022

@author: alain.bernard@loreal.com


## Functions {#functions}

### md_normalize {#md_normalize}

Normalize markdown text

Merge the lines not separated by a blank line

``` python
md_normalize(text)
```



#### Arguments {#arguments}

- **text** (srt) : the mark down text to normalize

#### Returns {#returns}

- **str** : normalized mark down text

## Classes {#classes}

### Reader {#reader}

Simple python source code parser.

#### Properties {#properties}

##### eol {#eol}

End of line flag> type Boolean


###### Getter {#getter}

End of line flag

``` python
eol()
```



####### Returns {#returns-1}

- **Boolean** : True if end of line is reached, False otherwise

##### eof {#eof}

End of file flag> type Boolean


###### Getter {#getter-1}

End of file flag

``` python
eof()
```



####### Returns {#returns-2}

- **Boolean** : True if end of file is reached, False otherwise

##### read {#read}

Read the next char

After reading, the cursor is incremented> type str


###### Getter {#getter-2}

Read the next char

After reading, the cursor is incremented

``` python
read()
```



####### Returns {#returns-3}

- **str** : Next character or None if end of file

##### current {#current}

Read the current char

Getting the current char doesn't move the cursor.> type str


###### Getter {#getter-3}

Read the current char

Getting the current char doesn't move the cursor.

``` python
current()
```



####### Returns {#returns-4}

- **str** : Next character or None if end of file

##### previous {#previous}

Read the previous char> type str


###### Getter {#getter-4}

Read the previous char

``` python
previous()
```



####### Returns {#returns-5}

- **str** : Previous character or None if start of file

#### Methods {#methods}



``` python
Reader(text)
```



#### __init__



##### FromFile {#fromfile}

Initialize a parser from a file.

``` python
FromFile(fname)
```



###### Arguments {#arguments-1}

- **fname** (str) : full path of the file top parse

##### reset {#reset}

Reset the cursor to the start of the text

``` python
reset()
```



##### back {#back}

Move the cursor one step backwards

``` python
back()
```



##### equal {#equal}

Compare the string starting at the cursor with the argument

``` python
equal(s)
```



###### Arguments {#arguments-2}

- **s** (str) : the string to compare with

###### Returns {#returns-6}

- **Boolean** : True if the text at the cursor is equal to the argument

### Doc {#doc}

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

#### Properties {#properties-1}

#### Methods {#methods-1}



``` python
Doc(match)
```



#### __init__



