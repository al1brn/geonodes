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

End of line flag



##### Returns

- _Boolean_ : True if end of line is reached, False otherwise


## previous

``` python
Reader.previous
```

Read the previous char



##### Returns

- _str_ : Previous character or None if start of file


## read

``` python
Reader.read
```

Read the next char

After reading, the cursor is incremented



##### Returns

- _str_ : Next character or None if end of file



# Methods

## FromFile

> **Decorators**: Class method

``` python
Reader.FromFile(cls, fname)
```

Initialize a parser from a file.



##### Arguments

- **fname** (_str_) : full path of the file top parse


## back

``` python
Reader.back(self)
```

Move the cursor one step backwards




## current

``` python
Reader.current
```

Read the current char

Getting the current char doesn't move the cursor.



##### Returns

- _str_ : Next character or None if end of file


## eof

``` python
Reader.eof
```

End of file flag



##### Returns

- _Boolean_ : True if end of file is reached, False otherwise


## equal

``` python
Reader.equal(self, s)
```

Compare the string starting at the cursor with the argument



##### Arguments

- **s** (_str_) : the string to compare with

##### Returns

- _Boolean_ : True if the text at the cursor is equal to the argument


## previous

``` python
Reader.previous
```

Read the previous char



##### Returns

- _str_ : Previous character or None if start of file


## python_split

``` python
Parser.python_split(self)
```

Split the python source file in parts

The methods returns a couple.
- The first item is the context in ('SOURCE', 'COMMENT', 'STRING')
- The second item is the source code

yield
-----
- tuple (str, str) : context, source code




## read

``` python
Reader.read
```

Read the next char

After reading, the cursor is incremented



##### Returns

- _str_ : Next character or None if end of file


## reset

``` python
Reader.reset(self)
```

Reset the cursor to the start of the text





