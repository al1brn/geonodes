# Parser module

Simple python source parser

The module [Parser](parser_module.md#parser) parse source file and returns the documentation as a liste of [Doc](parser_module.md#doc) instances.

# Parser



``` python
Reader(self, text)
```

Simple python source code parser.



## Properties



### eol

``` python
Reader.eol
```

End of line flag



#### Returns



- _Boolean_ : True if end of line is reached, False otherwise



<sub>[top](#parser) [index](index.md)</sub>
### previous

``` python
Reader.previous
```

Read the previous char



#### Returns



- _str_ : Previous character or None if start of file



<sub>[top](#parser) [index](index.md)</sub>
### read

``` python
Reader.read
```

Read the next char

After reading, the cursor is incremented



#### Returns



- _str_ : Next character or None if end of file



<sub>[top](#parser) [index](index.md)</sub>

## Methods



### FromFile

> **Decorators**: Class method

``` python
Reader.FromFile(cls, fname)
```

Initialize a parser from a file.



#### Arguments



- **fname** (_str_) : full path of the file top parse



<sub>[top](#parser) [index](index.md)</sub>
### back

``` python
Reader.back(self)
```

Move the cursor one step backwards





<sub>[top](#parser) [index](index.md)</sub>
### current

``` python
Reader.current
```

Read the current char

Getting the current char doesn't move the cursor.



#### Returns



- _str_ : Next character or None if end of file



<sub>[top](#parser) [index](index.md)</sub>
### eof

``` python
Reader.eof
```

End of file flag



#### Returns



- _Boolean_ : True if end of file is reached, False otherwise



<sub>[top](#parser) [index](index.md)</sub>
### equal

``` python
Reader.equal(self, s)
```

Compare the string starting at the cursor with the argument



#### Arguments



- **s** (_str_) : the string to compare with

#### Returns



- _Boolean_ : True if the text at the cursor is equal to the argument



<sub>[top](#parser) [index](index.md)</sub>
### previous

``` python
Reader.previous
```

Read the previous char



#### Returns



- _str_ : Previous character or None if start of file



<sub>[top](#parser) [index](index.md)</sub>
### python_split

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





<sub>[top](#parser) [index](index.md)</sub>
### read

``` python
Reader.read
```

Read the next char

After reading, the cursor is incremented



#### Returns



- _str_ : Next character or None if end of file



<sub>[top](#parser) [index](index.md)</sub>
### reset

``` python
Reader.reset(self)
```

Reset the cursor to the start of the text





<sub>[top](#parser) [index](index.md)</sub>

# Doc



``` python
Doc(self, match)
```

Item documentation

This class stores the documentation of a functions or a class. In addition to the doc, it contains complementary information:
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



## Functions



### ok_comment

``` python
ok_comment(s)
```




### md_normalize

``` python
md_normalize(text)
```

Normalize markdown text

Merge the lines not separated by a blank line



#### Arguments



- **text** (_srt_) : the mark down text to normalize

#### Returns



- _str_ : normalized mark down text


### extract_source

``` python
extract_source(comment)
```




### replace_source

``` python
replace_source(comment, d)
```






