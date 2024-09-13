# parser


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


## Content


- C : [clean_python](#clean_python) :black_small_square: [capture_inheritance](#capture_inheritance) :black_small_square: [capture_inheritances](#capture_inheritances)
- D : [del_margin](#del_margin)
- E : [extract_strings](#extract_strings) :black_small_square: [extract_source](#extract_source) :black_small_square: [extract_lists](#extract_lists)
- P : [parse_list_line](#parse_list_line) :black_small_square: [parse_module](#parse_module) :black_small_square: [parse_files](#parse_files)
- R : [replace_strings](#replace_strings) :black_small_square: [replace_source](#replace_source)
- T : [Text](#text)

## Functions

### capture_inheritance

Capture properties et methods from another class

Allow to document class items as it were not inherited.

> [!Note]
> if the name of the base class is in the inherits list, it is removed from it

``` python
capture_inheritance(class_, base_, remove=True)
```



<sub>[top](#parser) [index](index.md)</sub>



#### Arguments

- **class_** (dict) : the class to enrich
- - **base_** (dict) : the class to capture properties and methods from
- - **remove** (_bool_ = True) : remove base name from inheritance list

### capture_inheritances

Capture inheritances

Allow to document class items as it were not inherited.

> [!Note]
> if the name of the base class is in the inherits list, it is removed from it

``` python
capture_inheritances(class_, modules_, include=None, exclude=[], verbose=True)
```



<sub>[top](#parser) [index](index.md)</sub>



#### Arguments

- **class_** (dict) : the class to enrich
- - **modules_** (dict) : the hierarchy containing base classes to capture from
- - **include** (_list_ = None) : limit capture to the given list
- - **exclude** (_list_ = []) : exclude classes in the given list

### clean_python

Clean python source code

- Replace the comments by an comment index
- Replace the strings by an index
- Remove the blank lines
- Group multilines instructions between ( and )

Comments and strings are store in lists.
Comments are replaced by <COMMENT index> and strings by "index"

``` python
clean_python(text)
```



<sub>[top](#parser) [index](index.md)</sub>



#### Arguments

- **text** (str) : source code to clean

#### Returns

- **str** : cleaned text
- - **list** : list of comments
- - **list** : list of strings

### del_margin

Move lines leftwards to suppress margin.

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



<sub>[top](#parser) [index](index.md)</sub>



#### Arguments

- **comment** (str) : the comment

#### Returns

- **str** : the realigned comment

### extract_lists

Extract lists from a comment.

This parser extracts Properties, Arguments and Returns sections.
The corresponding lines are removed to build the 'new_comment' text.

The lists are generated from the structure

``` python
extract_lists(comment, titles)
```



<sub>[top](#parser) [index](index.md)</sub>



#### Arguments

- **comment** (str) : the raw comment
- - **titles** (str or list of strs) : the titles of the lists to extract

#### Returns

- **str** : comment without the lists, lists as dict

### extract_source

Replace source code block by an index.

This pretreatment ensure that the content of sourcode won't interfer with
regular expression

``` python
extract_source(text)
```



<sub>[top](#parser) [index](index.md)</sub>



#### Arguments

- **text** (str) : text to extract source code from

#### Returns

- **str** : cleaned text and list of extracted pieces of code

### extract_strings

Replace string by an index.

This pretreatment ensure that the content of strings won't interfer with
regular expression

``` python
extract_strings(text)
```



<sub>[top](#parser) [index](index.md)</sub>



#### Arguments

- **text** (str) : text to extract strings from

#### Returns

- **str** : cleaned text and list of extracted strings

### parse_files

Load files from a folder.

All the files with `.py` extension are parsed.

``` python
parse_files(folder, sub_folders=[], key=None, verbose=False)
```



<sub>[top](#parser) [index](index.md)</sub>



#### Arguments

- **folder** (str) : main folder
- - **sub_folders** (str) : sub folders to explore
- - **key** (_str_ = None) : 

#### Returns

- **dict** : 

### parse_list_line

Parse a list line in a comment

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



<sub>[top](#parser) [index](index.md)</sub>



### parse_module

Parse a python file source

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
parse_module(text, module_name="124")
```



<sub>[top](#parser) [index](index.md)</sub>



#### Arguments

- **text** (str) : source code to parse

#### Returns

- **dict** : classes and functions

### replace_source

Replace the extracted strings.

``` python
replace_source(text, strings)
```



<sub>[top](#parser) [index](index.md)</sub>



#### Arguments

- **text** (str) : text with replaced pieces of code
- - **strings** : list of pieces of code

#### Returns

- **Text** : 

### replace_strings

Replace the extracted strings.

``` python
replace_strings(text, strings)
```



<sub>[top](#parser) [index](index.md)</sub>



#### Arguments

- **text** (str) : text with replaced strings
- - **strings** : list of strings

#### Returns

- **Text** : 

## Classes

### Text

Implements a simple text reader.

The Text class manages a cursor on a multilines string.
It offers basic function to read around the cursor (backward and forwards).
It also implements features to move to (or after) a target and
to replace a text segment by replacement string.

Properties
----------
- cursor (int) : current position

<sub>[top](#parser) [index](index.md)</sub>



#### Content


- C : [c](#c)
- E : [eof](#eof) :black_small_square: [eol](#eol) :black_small_square: [extract_strings](#extract_strings)
- F : [from_cursor](#from_cursor) :black_small_square: [find](#find)
- M : [move](#move) :black_small_square: [move_to](#move_to) :black_small_square: [move_after](#move_after)
- R : [replace](#replace)
- _ : [__call__](#__call__)

#### Properties

##### c

Current character

Note that an error is raised if [LINK ERROR: page 'eof' not found]() is True.

``` python
return self.text[self.cursor]
```> type str


<sub>[top](#text) [index](index.md)</sub>



###### Getter

Current character

Note that an error is raised if [LINK ERROR: page 'eof' not found]() is True.

``` python
return self.text[self.cursor]
```

``` python
c()
```



####### Returns

- **str** : the character at cursor

##### eof

End of text is reached> type bool


<sub>[top](#text) [index](index.md)</sub>



###### Getter

End of text is reached

``` python
eof()
```



####### Returns

- **bool** : True if end of text is reached

##### eol

End of line is reached> type bool


<sub>[top](#text) [index](index.md)</sub>



###### Getter

End of line is reached

``` python
eol()
```



####### Returns

- **bool** : True if current char is eol (or if eof is True)

##### from_cursor

Return the text from the cursor.> type str


<sub>[top](#text) [index](index.md)</sub>



###### Getter

Return the text from the cursor.

``` python
from_cursor()
```



####### Returns

- **str** : text from the cursor

#### Methods



``` python
Text(text)
```



##### __call__

Read the string around the cursor

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



<sub>[top](#text) [index](index.md)</sub>



##### extract_strings

Extract strings from a text and returns the extracted text and the list of extracted strings.

``` python
extract_strings(text)
```



<sub>[top](#text) [index](index.md)</sub>



###### Arguments

- **text** (str) : the text to extract strings from

###### Returns

- **str** : text with strings replaced by 'index'
- - **list** : list of extracted strings

##### find

Find a target into the text

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



<sub>[top](#text) [index](index.md)</sub>



###### Arguments

- **target** (str or tuple of strs) : the string(s) to reach
- - **regex** (_bool_ = False) : target is a regular expression or not
- - **halt** (_bool_ = True) : raise an exception if not found

###### Returns

- **int** : the new cursor position

##### move

Move the cursor of the given offset

``` python
move(offset=1)
```



<sub>[top](#text) [index](index.md)</sub>



###### Arguments

- **offset** (_int_ = 1) : cursor offset

###### Returns

- **int** : new cursor position

##### move_after

Move the cursor until it reaches the given target.

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



<sub>[top](#text) [index](index.md)</sub>



###### Arguments

- **target** (str or tuple of strs) : the string(s) to reach

###### Returns

- **int** : the new cursor position

##### move_to

Move the cursor until it reaches the given target.

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



<sub>[top](#text) [index](index.md)</sub>



###### Arguments

- **target** (str or tuple of strs) : the string(s) to reach

###### Returns

- **int** : the new cursor position

##### replace

Replace the text between two positions by a replacement string.

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



<sub>[top](#text) [index](index.md)</sub>



###### Arguments

- **start** (int) : start index of replaced part
- - **end** (int) : end index of replace part
- - **repl** (str) : the replacement string

###### Returns

- **str** : the replaced string

