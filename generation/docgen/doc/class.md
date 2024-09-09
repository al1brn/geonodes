# Class


> inherits from: [Section](section.md) 

> inherited: [FromSource](section.md#fromsource), [__init__](section.md#__init__), [alphabetical_sections](section.md#alphabetical_sections), [as_dict](section.md#as_dict), [build_extra](section.md#build_extra), [build_header](section.md#build_header), [build_sections](section.md#build_sections), [comment](section.md#comment), [extra](section.md#extra), [fixed_level](section.md#fixed_level), [get_section](section.md#get_section), [in_toc](section.md#in_toc), [init](section.md#init), [iteration](section.md#iteration), [level](section.md#level), [link_to](section.md#link_to), [link_token](section.md#link_token), [md_file_name](section.md#md_file_name), [new_section](section.md#new_section), [page](section.md#page), [parse_comment](section.md#parse_comment), [print](section.md#print), [sort_sections](section.md#sort_sections), [sorted_sections](section.md#sorted_sections), [title](section.md#title), [toc](section.md#toc), [with_sections_only](section.md#with_sections_only), [write](section.md#write), [write_header](section.md#write_header)


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

