<h1 id="pyparser">pyparser</h1>
Created on Wed Jun  8 09:00:41 2022

@author: alain.bernard@loreal.com


<h2 id="functions">Functions</h2><h3 id="md_normalize">md_normalize</h3>Normalize markdown text

Merge the lines not separated by a blank line

``` python
md_normalize(text)
```



<h4 id="arguments">Arguments</h4>- **text** (srt) : the mark down text to normalize

<h4 id="returns">Returns</h4>- **str** : normalized mark down text

<h2 id="classes">Classes</h2><h3 id="reader">Reader</h3>Simple python source code parser.

<h4 id="properties">Properties</h4><h5 id="eol">eol</h5>End of line flag> type Boolean


<h6 id="getter">Getter</h6>End of line flag

``` python
eol()
```



<h7 id="returns-1">Returns</h7>- **Boolean** : True if end of line is reached, False otherwise

<h5 id="eof">eof</h5>End of file flag> type Boolean


<h6 id="getter-1">Getter</h6>End of file flag

``` python
eof()
```



<h7 id="returns-2">Returns</h7>- **Boolean** : True if end of file is reached, False otherwise

<h5 id="read">read</h5>Read the next char

After reading, the cursor is incremented> type str


<h6 id="getter-2">Getter</h6>Read the next char

After reading, the cursor is incremented

``` python
read()
```



<h7 id="returns-3">Returns</h7>- **str** : Next character or None if end of file

<h5 id="current">current</h5>Read the current char

Getting the current char doesn't move the cursor.> type str


<h6 id="getter-3">Getter</h6>Read the current char

Getting the current char doesn't move the cursor.

``` python
current()
```



<h7 id="returns-4">Returns</h7>- **str** : Next character or None if end of file

<h5 id="previous">previous</h5>Read the previous char> type str


<h6 id="getter-4">Getter</h6>Read the previous char

``` python
previous()
```



<h7 id="returns-5">Returns</h7>- **str** : Previous character or None if start of file

<h4 id="methods">Methods</h4>

``` python
Reader(text)
```



#### __init__



<h5 id="fromfile">FromFile</h5>Initialize a parser from a file.

``` python
FromFile(fname)
```



<h6 id="arguments-1">Arguments</h6>- **fname** (str) : full path of the file top parse

<h5 id="reset">reset</h5>Reset the cursor to the start of the text

``` python
reset()
```



<h5 id="back">back</h5>Move the cursor one step backwards

``` python
back()
```



<h5 id="equal">equal</h5>Compare the string starting at the cursor with the argument

``` python
equal(s)
```



<h6 id="arguments-2">Arguments</h6>- **s** (str) : the string to compare with

<h6 id="returns-6">Returns</h6>- **Boolean** : True if the text at the cursor is equal to the argument

<h3 id="doc">Doc</h3>Item documentation

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

<h4 id="properties-1">Properties</h4><h4 id="methods-1">Methods</h4>

``` python
Doc(match)
```



#### __init__



