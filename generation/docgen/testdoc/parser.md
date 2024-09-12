<h1 id="parser">parser</h1>
Created on Tue Sep 10 07:44:18 2024

@author: alain


Module parser

This module implements a simple python parser which extract comments
form a source code file.

The parsing returns nested dicts where a dict contains information on the documented item

A base dict structure is:

- obj      : module, class, function, ...
- name     : python name
- comment  : the first multilines string after item declaration
- subs     : dict of dicts containing sub items

In addition to this structure, a dict can contain complementory values such as inheritance for
classes or arguments for functions


<h2 id="functions">Functions</h2><h3 id="del_margin">del_margin</h3>Move lines leftwards to suppress margin.

Comment read in source code can have a non nul left margin whcih is interprated in markdown.
This method:
- suppresses the margin of the first line
- move leftwards the lines after in order that the leftmost line has no margin and
  that the relative indentation remains the same

The following text:
|     Example of text
|               This text is aligned
|               with a margin:
|               - because it is written as a multiline comment string
|                 with indentation
|               Text continues here

Is realigned:
| Example of text
| This texte is aligned
| with a margin:
| - because it is written as a multiline comment string
|   with indentation
| Text continues here

``` python
del_margin(comment)
```



<h4 id="arguments">Arguments</h4>- **comment** (str) : the comment

<h4 id="returns">Returns</h4>- **str** : the realigned comment

<h3 id="extract_strings">extract_strings</h3>Replace string by an index.

This pretreatment ensure that the content of strings won't interfer with
regular expression

``` python
extract_strings(text)
```



<h4 id="arguments-1">Arguments</h4>- **text** (str) : text to extract strings from

<h4 id="returns-1">Returns</h4>- **str** : cleaned text and list of extracted strings

<h3 id="replace_strings">replace_strings</h3>Replace the extracted strings.

``` python
replace_strings(text, strings)
```



<h4 id="arguments-2">Arguments</h4>- **text** (str) : text with replaced strings
- - **strings** : list of strings

<h4 id="returns-2">Returns</h4>- **Text** :  with original strings


<h3 id="extract_source">extract_source</h3>Replace source code block by an index.

This pretreatment ensure that the content of sourcode won't interfer with
regular expression

``` python
extract_source(text)
```



<h4 id="arguments-3">Arguments</h4>- **text** (str) : text to extract source code from

<h4 id="returns-3">Returns</h4>- **str** : cleaned text and list of extracted pieces of code

<h3 id="replace_source">replace_source</h3>Replace the extracted strings.

``` python
replace_source(text, strings)
```



<h4 id="arguments-4">Arguments</h4>- **text** (str) : text with replaced pieces of code
- - **strings** : list of pieces of code

<h4 id="returns-4">Returns</h4>- **Text** :  with original strings


<h3 id="clean_python">clean_python</h3>Clean python source code

- Replace the comments by an comment index
- Replace the strings by an index
- Remove the blank lines
- Group multilines instructions between ( and )

Comments and strings are store in lists.
Comments are replaced by <COMMENT index> and strings by "index"

``` python
clean_python(text)
```



<h4 id="arguments-5">Arguments</h4>- **text** (str) : source code to clean

<h4 id="returns-5">Returns</h4>- **str** : cleaned text
- - **list** : list of comments
- - **list** : list of strings

<h3 id="parse_list_line">parse_list_line</h3>Parse a list line in a comment

syntax:
- name (type = default) : description

Default value could contain parenthesis as in `Vector = (1, 2, 3)`,
the parsing is done by reading the line char per char to handle
parenthesis nesting.

``` python
line = "- text (str = None) : text to parse"
pprint(parse_list_line(line))
# > {'default': 'None',
# > 'description': 'text to parse',
# > 'name': 'text',
# > 'obj' : 'str'}
```

``` python
parse_list_line(line)
```



<h3 id="extract_lists">extract_lists</h3>Extract lists from a comment.

This parser extracts Properties, Arguments and Returns sections.
The corresponding lines are removed to build the 'new_comment' text.

The lists are generated from the structure

``` python
extract_lists(comment, titles)
```



<h4 id="arguments-6">Arguments</h4>- **comment** (str) : the raw comment
- - **titles** (str or list of strs) : the titles of the lists to extract

<h4 id="returns-6">Returns</h4>- **str** : comment without the lists, lists as dict

<h3 id="parse_module">parse_module</h3>Parse a python file source

The parser returns a dictionary giving the content of the module:

- module
  - comment
  - subs : dict of classes and functions
- class
  - name
  - comment
  - inherits (list)
  - subs : dict of properties and functions (methods)
- function
  - name
  - comment
  - args (str)
  - decorators (list of strs)
  - raises: list of dicts for raises
  - arguments: list of dicts for arguments
  - returns: list of dicts for returns
- property
  - name
  - comment
  - type
  - default
  - setter : function
  - getter : function

The parsing is done with regular expressions.

``` python
parse_module(text, module_name="119")
```



<h4 id="arguments-7">Arguments</h4>- **text** (str) : source code to parse

<h4 id="returns-7">Returns</h4>- **dict** : classes and functions

<h3 id="parse_files">parse_files</h3>Load files from a folder.

All the files with `.py` extension are parsed.

``` python
parse_files(folder, sub_folders=[], key=None, verbose=False)
```



<h4 id="arguments-8">Arguments</h4>- **folder** (str) : main folder
- - **sub_folders** (str) : sub folders to explore
- - **key** (_str_ = None) : 

<h4 id="returns-8">Returns</h4>- **dict** : 


<h3 id="capture_inheritance">capture_inheritance</h3>Capture properties et methods from another class

Allow to document class items as it were not inherited.

> [!Note]
> if the name of the base class is in the inherits list, it is removed from it

``` python
capture_inheritance(class_, base_, remove=True)
```



<h4 id="arguments-9">Arguments</h4>- **class_** (dict) : the class to enrich
- - **base_** (dict) : the class to capture properties and methods from
- - **remove** (_bool_ = True) : remove base name from inheritance list

<h3 id="capture_inheritances">capture_inheritances</h3>Capture inheritances

Allow to document class items as it were not inherited.

> [!Note]
> if the name of the base class is in the inherits list, it is removed from it

``` python
capture_inheritances(class_, modules_, include=None, exclude=[], verbose=True)
```



<h4 id="arguments-10">Arguments</h4>- **class_** (dict) : the class to enrich
- - **modules_** (dict) : the hierarchy containing base classes to capture from
- - **include** (_list_ = None) : limit capture to the given list
- - **exclude** (_list_ = []) : exclude classes in the given list

<h2 id="classes">Classes</h2><h3 id="text">Text</h3>Implements a simple text reader.

The Text class manages a cursor on a multilines string.
It offers basic function to read around the cursor (backward and forwards).
It also implements features to move to (or after) a target and
to replace a text segment by replacement string.

Properties
----------
- cursor (int) : current position

<h4 id="properties">Properties</h4><h5 id="eof">eof</h5>End of text is reached> type bool


<h6 id="getter">Getter</h6>End of text is reached

``` python
eof()
```



<h7 id="returns-9">Returns</h7>- **bool** : True if end of text is reached

<h5 id="eol">eol</h5>End of line is reached> type bool


<h6 id="getter-1">Getter</h6>End of line is reached

``` python
eol()
```



<h7 id="returns-10">Returns</h7>- **bool** : True if current char is eol (or if eof is True)

<h5 id="c">c</h5>Current character

Note that an error is raised if [LINK ERROR: page 'eof' not found]() is True.

``` python
return self.text[self.cursor]
```> type str


<h6 id="getter-2">Getter</h6>Current character

Note that an error is raised if [LINK ERROR: page 'eof' not found]() is True.

``` python
return self.text[self.cursor]
```

``` python
c()
```



<h7 id="returns-11">Returns</h7>- **str** : the character at cursor

<h5 id="from_cursor">from_cursor</h5>Return the text from the cursor.> type str


<h6 id="getter-3">Getter</h6>Return the text from the cursor.

``` python
from_cursor()
```



<h7 id="returns-12">Returns</h7>- **str** : text from the cursor

<h4 id="methods">Methods</h4>

``` python
Text(text)
```



#### __init__



<h5 id="__call__">__call__</h5>Read the string around the cursor

One or two argumentscan be passed:
- If only one argument is passed (**count** is None), it is used as the number of chars
  to read after the cursoor
- If two arguments are passed, they are interpreted as the starting position to read
  from and the number of characters to read

 > [!NOTE]
 > The start position is relative to the cursor

 ``` python
 # Read 3 characters from the cursor
 a = text(3)

 # Read the character preceeding the cursor
 b = text(-1, 1)

 # Note that the two following lines return the same result
 c = text()
 c = text.c
 ```

 Arguments
 ---------
 - start (int) : number of characters to read from the cursor if count is None,
   position to start to read otherwise
 - count (int) : number of characters to read, 1 is read if None

 Returns
 -------
 - str : the read characters

``` python
__call__(start=1, count=None)
```



<h5 id="move">move</h5>Move the cursor of the given offset

``` python
move(offset=1)
```



<h6 id="arguments-11">Arguments</h6>- **offset** (_int_ = 1) : cursor offset

<h6 id="returns-13">Returns</h6>- **int** : new cursor position

<h5 id="find">find</h5>Find a target into the text

> [!IMPORTANT]
> The search starts at the cursor

The target can be a single string or a tuple of strings.
The function return the target and the cursor is place just after
the target

An error is raised if the target is not found and **halt** is True.

``` python
text = Text("Search for A B C")

print(text.find("B"))
# > B

text.cursor = 0
print(text.find(("A", "B", "C")))
# > A

print(Text("Find this number: 123!").find(r"\d+"))
# > 123
```

``` python
find(target, regex=False, halt=True)
```



<h6 id="arguments-12">Arguments</h6>- **target** (str or tuple of strs) : the string(s) to reach
- - **regex** (_bool_ = False) : target is a regular expression or not
- - **halt** (_bool_ = True) : raise an exception if not found

<h6 id="returns-14">Returns</h6>- **int** : the new cursor position

<h5 id="move_to">move_to</h5>Move the cursor until it reaches the given target.

This function execute a [LINK ERROR: page 'find' not found]() on the target and places the
cursor just before the target.

``` python
found = self.find(target)
return self.move(-len(found))
```

``` python
text = Text("Just go HERE")

text.move_to("HERE")
print(text.from_cursor)
# > HERE
```

``` python
move_to(target, regex=False, halt=True)
```



<h6 id="arguments-13">Arguments</h6>- **target** (str or tuple of strs) : the string(s) to reach

<h6 id="returns-15">Returns</h6>- **int** : the new cursor position

<h5 id="move_after">move_after</h5>Move the cursor until it reaches the given target.

This function execute a [LINK ERROR: page 'find' not found]() on the target and places the
cursor just before the target.

``` python
self.find(target)
return self.cursor
```

``` python
text = Text("Go after TARGET: here")

text.move_after("TARGET")
print(text.from_cursor)
# > : here
```

``` python
move_after(target, regex=False, halt=True)
```



<h6 id="arguments-14">Arguments</h6>- **target** (str or tuple of strs) : the string(s) to reach

<h6 id="returns-16">Returns</h6>- **int** : the new cursor position

<h5 id="replace">replace</h5>Replace the text between two positions by a replacement string.

After the operation, the cursor is placed after the replacement string.

This method return the **replaced** string.

> [!NOTE]
> The **start** and **end** position are absolute positions, note relative
> to the cursor

Typical use is given here below:

```python
line = "Line of text with a token <My Token>."

text = Text(line)
start = text.move_to('<')
end = text.move_after('>')
token = text.replace(start, end, "HERE WAS A TOKEN")

print(text.text)
# Line of text with a token HERE WAS A TOKEN.

print(token)
# <My Token>
```

``` python
replace(start, end, repl)
```



<h6 id="arguments-15">Arguments</h6>- **start** (int) : start index of replaced part
- - **end** (int) : end index of replace part
- - **repl** (str) : the replacement string

<h6 id="returns-17">Returns</h6>- **str** : the replaced string

