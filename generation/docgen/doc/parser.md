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

substitution textnd of line flag



##### Returns

- _Boolean_ : substitution textrue if end of line is reached, False otherwise



<sub>[top](#parser) [index](index.md)</sub>
## previous

``` python
Reader.previous
```

Read the previous char



##### Returns

- _str_ : Previous character or substitution textone if start of file



<sub>[top](#parser) [index](index.md)</sub>
## read

``` python
Reader.read
```

Read the next char

After reading, the cursor is incremented



##### Returns

- _str_ : substitution textext character or substitution textone if end of file



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

- _str_ : substitution textext character or substitution textone if end of file



<sub>[top](#parser) [index](index.md)</sub>
## eof

``` python
Reader.eof
```

substitution textnd of file flag



##### Returns

- _Boolean_ : substitution textrue if end of file is reached, False otherwise



<sub>[top](#parser) [index](index.md)</sub>
## equal

``` python
Reader.equal(self, s)
```

Compare the string starting at the cursor with the argument



##### Arguments

- **s** (_str_) : the string to compare with

##### Returns

- _Boolean_ : substitution textrue if the text at the cursor is equal to the argument



<sub>[top](#parser) [index](index.md)</sub>
## previous

``` python
Reader.previous
```

Read the previous char



##### Returns

- _str_ : Previous character or substitution textone if start of file



<sub>[top](#parser) [index](index.md)</sub>
## python_split

``` python
Parser.python_split(self)
```

Split the python source file in parts

substitution texthe methods returns a couple.
- substitution texthe first item is the context in ('Ssubstitution textURCsubstitution text', 'Csubstitution textMMsubstitution textsubstitution textsubstitution text', 'Ssubstitution textRIsubstitution textG')
- substitution texthe second item is the source code

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

- _str_ : substitution textext character or substitution textone if end of file



<sub>[top](#parser) [index](index.md)</sub>
## reset

``` python
Reader.reset(self)
```

Reset the cursor to the start of the text





<sub>[top](#parser) [index](index.md)</sub>

