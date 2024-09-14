# Text

Implements a simple text reader.

The Text class manages a cursor on a multilines string.
It offers basic function to read around the cursor (backward and forwards).
It also implements features to move to (or after) a target and
to replace a text segment by replacement string.

``` python
Text(text)
```



## Content


- C : [c](#c) :black_small_square: [cursor](#cursor)
- E : [eof](#eof) :black_small_square: [eol](#eol) :black_small_square: [extract_strings](#extract_strings)
- F : [find](#find) :black_small_square: [from_cursor](#from_cursor)
- M : [move](#move) :black_small_square: [move_after](#move_after) :black_small_square: [move_to](#move_to)
- R : [replace](#replace) :black_small_square: [replace_strings](#replace_strings)
- T : [to_regex](#to_regex)
- _ : [__call__](#__call__) :black_small_square: [__str__](#__str__)



## Properties

----------
### c

Current character

Note that an error is raised if [LINK ERROR: page 'eof' not found]() is True.

``` python
return self.text[self.cursor]
```

- getter 
- type **str**


<sub>[top](#text) [index](index.md)</sub>



----------
### cursor

current position

- type **int**


<sub>[top](#text) [index](index.md)</sub>



----------
### eof

End of text is reached

- getter 
- type **bool**


<sub>[top](#text) [index](index.md)</sub>



----------
### eol

End of line is reached

- getter 
- type **bool**


<sub>[top](#text) [index](index.md)</sub>



----------
### from_cursor

Return the text from the cursor.

- getter 
- type **str**


<sub>[top](#text) [index](index.md)</sub>



## Methods

----------
### __call__

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



----------
### __str__



``` python
__str__()
```



<sub>[top](#text) [index](index.md)</sub>



----------
### extract_strings

Extract strings from a text and returns the extracted text and the list of extracted strings.

``` python
extract_strings(text)
```



#### Arguments

- **text** (str) : the text to extract strings from



#### Returns

- **str** : text with strings replaced by 'index'
- - **list** : list of extracted strings



<sub>[top](#text) [index](index.md)</sub>



----------
### find

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



#### Arguments

- **target** (str or tuple of strs) : the string(s) to reach
- - **regex** (_bool_ = False) : target is a regular expression or not
- - **halt** (_bool_ = True) : raise an exception if not found



#### Returns

- **int** : the new cursor position



<sub>[top](#text) [index](index.md)</sub>



----------
### move

Move the cursor of the given offset

``` python
move(offset=1)
```



#### Arguments

- **offset** (_int_ = 1) : cursor offset



#### Returns

- **int** : new cursor position



<sub>[top](#text) [index](index.md)</sub>



----------
### move_after

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



#### Arguments

- **target** (str or tuple of strs) : the string(s) to reach



#### Returns

- **int** : the new cursor position



<sub>[top](#text) [index](index.md)</sub>



----------
### move_to

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



#### Arguments

- **target** (str or tuple of strs) : the string(s) to reach



#### Returns

- **int** : the new cursor position



<sub>[top](#text) [index](index.md)</sub>



----------
### replace

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



#### Arguments

- **start** (int) : start index of replaced part
- - **end** (int) : end index of replace part
- - **repl** (str) : the replacement string



#### Returns

- **str** : the replaced string



<sub>[top](#text) [index](index.md)</sub>



----------
### replace_strings



``` python
replace_strings(text, strings)
```



<sub>[top](#text) [index](index.md)</sub>



----------
### to_regex



``` python
to_regex(s)
```



<sub>[top](#text) [index](index.md)</sub>

