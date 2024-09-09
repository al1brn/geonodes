# Class


> inherits from: [Section](section.md) 

> inherited: [FromSource](section.md#section), [__init__](section.md#section), [alphabetical_sections](section.md#section), [as_dict](section.md#section), [build_extra](section.md#section), [build_header](section.md#section), [build_sections](section.md#section), [comment](section.md#section), [extra](section.md#section), [fixed_level](section.md#section), [get_section](section.md#section), [in_toc](section.md#section), [init](section.md#section), [iteration](section.md#section), [level](section.md#section), [link_to](section.md#section), [link_token](section.md#section), [md_file_name](section.md#section), [new_section](section.md#section), [page](section.md#section), [parse_comment](section.md#section), [print](section.md#section), [sort_sections](section.md#section), [sorted_sections](section.md#section), [title](section.md#section), [toc](section.md#section), [with_sections_only](section.md#section), [write](section.md#section), [write_header](section.md#section)


# Properties



## properties

``` python
Class.properties
```



##### Returns



- _Section_ : title is 'Properties', sub sections are documented properties



<sub>[top](#class) [index](index.md)</sub>

# Methods



## FromDoc

> **Decorators**: Class method

``` python
Class.FromDoc(cls, doc, ignore_uncommented=True, **kwargs)
```

Creates a Class document from a Doc parsed from source file

The **doc** argument contains the list of documents methods and properties.



##### Arguments



- **doc** (_Doc_) : Doc parsed from a sourc file
- **exclude_uncommented** (_bool_ = True) : exclude the methods which are not commented in the source file

##### Returns



- _Class_ : document on the class



<sub>[top](#class) [index](index.md)</sub>
## build

``` python
Class.build(self)
```

Yield the Class documentation lines





<sub>[top](#class) [index](index.md)</sub>
## capture_class

``` python
Class.capture_class(self, other, with_comment=False)
```

Capture methods and properties from another Class

This method allows to get the documentation of inherited items of a class which is not documentated.



##### Arguments



- **other** (_Class_) : class to copy methods and properties from

##### Returns



- _self_ : 



<sub>[top](#class) [index](index.md)</sub>
## compile

``` python
Class.compile(self, project)
```

Compile the class

**project** refers to the global [Project](project.md) documentation.

Class compilation is:
- Load each class based on this one into to the **subclasses** attribute.
- Load the methods and properties inherited from parent classes



##### Arguments



- **project** : 

##### Returns



- _self_ : 



<sub>[top](#class) [index](index.md)</sub>
## methods

``` python
Class.methods
```

Methods Section



##### Returns



- _Section_ : title is 'Methods', sub sections are documented methods



<sub>[top](#class) [index](index.md)</sub>

