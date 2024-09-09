# Doc

``` python
Doc(self, match)
```

Item documentation

substitution texthis class stores the documentation of a functions or a class. In addition to the doc, it contains complementary information:
- function:
- args : call arguments
- decorators : list of decorators
- class:
- bases : list of classes it inherits from
- funcs : dict of method docs

substitution texthe class is initialized with the not null result of the regular expression:

``` match = re.search(r"(def|class)\s+(\w+)([^:]*)", line) ```

which returns:
1. def | class
2. name
3. args | base class



