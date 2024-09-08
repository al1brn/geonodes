# ProjectDocumentation



``` python
ProjectDocumentation(self, title, comment=None, classes_section=True)
```

Project documentation

Building project documentation follows the following steps:
1. Creating the modules
2. Adding the classes to document. The classes must be documented in a module
3. Adding documentation
4. Compile the documentation to build links between pages
5. Write the documentation files

The example below write the documentation for this project:

``` python
# Step 1 : read project files from root folder

root = Path(__file__).parents[0] proj = ProjectDocumentation.FromFiles('Test', folder=root)

# Step 2 : build document hierarchy

proj.add_class('Parser', capture=['Reader']) proj.add_class('Doc')

proj.add_class('Section') proj.add_class('Argument', bases=['Section']) proj.add_class('Return',   bases=['Section']) proj.add_class('Function', bases=['Section']) proj.add_class('Class',    bases=['Section']) proj.add_class('Module') proj.add_class('ProjectDocumentation')

# Step 3 : compile

proj.compile()

# Step 4 : write the documentation

proj.write_documentation(doc_folder=root / 'doc')
```



## Methods and Properties
- A : [add_class](#add_class) [add_module](#add_module) 
- C : [compile](#compile) 
- W : [write_index](#write_index) 

# Methods



## add_class

``` python
ProjectDocumentation.add_class(self, class_name, module_name=None, bases=[], capture=[])
```

Add a class in the documented classes

The class is searched in all modules. If there exists homonymes in different modules, 'module_name' specifies the module to get the class from.

The 'capture' list contains base classes to copy documentation from. Hence, there exists two ways to manage inheritance:
- bases : the documentation makes the inheritance explicit by giving the base class and links to the inherited methods and properties
- capture : the documentation doesn't mention the inheritance but gives directly the documentation as if it were part of the class

> **Explicit inheritance**
> _class_name_ : inherits from base_class
> inherited methods : **method1**, **method2**

> **Hidden inheritance**
> _class_name_
> methods : **method1**, **method2**



##### Arguments



- **class_name** (_str_) : class name
- **module_name** (_str_ = None) : name of the source file module if the class exists in several modules
- **bases** (_list_ = []) : list of base classes
- **capture** (_list_ = []) : list of classes to copy methods and properties from



<sub>[top](#projectdocumentation) [index](index.md)</sub>
## add_module

``` python
ProjectDocumentation.add_module(self, name, text)
```

Add a module





<sub>[top](#projectdocumentation) [index](index.md)</sub>
## compile

``` python
ProjectDocumentation.compile(self)
```

Compile each class




<sub>[top](#projectdocumentation) [index](index.md)</sub>
## write_index

``` python
ProjectDocumentation.write_index(self, file_name)
```

Write the index file



##### Arguments



- **file_name** (_str_) : file name to write



<sub>[top](#projectdocumentation) [index](index.md)</sub>

