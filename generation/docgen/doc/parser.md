# Parser



``` python
Reader(self, text)
```

Simple python source code parser.



## Methods and Properties
- B : [back](#back) 
- C : [current](#current) 
- E : [eof](#eof) [eol](#eol) [equal](#equal) 
- F : [FromFile](#fromfile) 
- P : [previous](#previous) [previous](#previous) [python_split](#python_split) 
- R : [read](#read) [read](#read) [reset](#reset) 

# Properties



## eol

``` python
Reader.eol
```

<Token replacement text>nd of line flag



##### Returns



- _Boolean_ : <<Token replacement text>oken replacement text>rue if end of line is reached, False otherwise



<sub>[top](#parser) [index](index.md)</sub>
## previous

``` python
Reader.previous
```

Read the previous char



##### Returns



- _str_ : Previous character or <<Token replacement text>oken replacement text>one if start of file



<sub>[top](#parser) [index](index.md)</sub>
## read

``` python
Reader.read
```

Read the next char

After reading, the cursor is incremented



##### Returns



- _str_ : <<Token replacement text>oken replacement text>ext character or <<Token replacement text>oken replacement text>one if end of file



<sub>[top](#parser) [index](index.md)</sub>

# Methods



## FromFile

> **Decorators**: Class method

``` python
Reader.FromFile(cls, fname)
```

Initialize a parser from a file.



##### Arguments



- **fname** (_str_) : full path of the file top parse



<sub>[top](#parser) [index](index.md)</sub>
## back

``` python
Reader.back(self)
```

Move the cursor one step backwards





<sub>[top](#parser) [index](index.md)</sub>
## current

``` python
Reader.current
```

Read the current char

Getting the current char doesn't move the cursor.



##### Returns



- _str_ : <<Token replacement text>oken replacement text>ext character or <<Token replacement text>oken replacement text>one if end of file



<sub>[top](#parser) [index](index.md)</sub>
## eof

``` python
Reader.eof
```

<Token replacement text>nd of file flag



##### Returns



- _Boolean_ : <<Token replacement text>oken replacement text>rue if end of file is reached, False otherwise



<sub>[top](#parser) [index](index.md)</sub>
## equal

``` python
Reader.equal(self, s)
```

Compare the string starting at the cursor with the argument



##### Arguments



- **s** (_str_) : the string to compare with

##### Returns



- _Boolean_ : <<Token replacement text>oken replacement text>rue if the text at the cursor is equal to the argument



<sub>[top](#parser) [index](index.md)</sub>
## previous

``` python
Reader.previous
```

Read the previous char



##### Returns



- _str_ : Previous character or <<Token replacement text>oken replacement text>one if start of file



<sub>[top](#parser) [index](index.md)</sub>
## python_split

``` python
Parser.python_split(self)
```

Split the python source file in parts

<Token replacement text>he methods returns a couple.
- <Token replacement text>he first item is the context in ('S<Token replacement text>URC<Token replacement text>', 'C<Token replacement text>MM<Token replacement text><Token replacement text><Token replacement text>', 'S<Token replacement text>RI<Token replacement text>G')
- <Token replacement text>he second item is the source code

yield
-----
- tuple (str, str) : context, source code





<sub>[top](#parser) [index](index.md)</sub>
## read

``` python
Reader.read
```

Read the next char

After reading, the cursor is incremented



##### Returns



- _str_ : <<Token replacement text>oken replacement text>ext character or <<Token replacement text>oken replacement text>one if end of file



<sub>[top](#parser) [index](index.md)</sub>
## reset

``` python
Reader.reset(self)
```

Reset the cursor to the start of the text





<sub>[top](#parser) [index](index.md)</sub>

