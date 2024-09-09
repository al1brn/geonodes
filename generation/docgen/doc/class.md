# Class




> inherits from: [Section](section.md) 

> inherited: <!Section#FromSource>, <!Section#__init__>, <!Section#alphabetical_sections>, <!Section#as_dict>, <!Section#build_extra>, <!Section#build_header>, <!Section#build_sections>, <!Section#comment>, <!Section#extra>, <!Section#fixed_level>, <!Section#get_section>, <!Section#in_toc>, <!Section#init>, <!Section#iteration>, <!Section#level>, <!Section#link_to>, <!Section#link_token>, <!Section#md_file_name>, <!Section#new_section>, <!Section#page>, <!Section#parse_comment>, <!Section#print>, <!Section#sort_sections>, <!Section#sorted_sections>, <!Section#title>, <!Section#toc>, <!Section#with_sections_only>, <!Section#write>
## Methods and Properties
- B : [build](#build) 
- C : [capture_class](#capture_class) [compile](#compile) 
- F : [FromDoc](#fromdoc) 
- M : [methods](#methods) 
- P : [properties](#properties) 

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
Class.compile(self, project=None)
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

