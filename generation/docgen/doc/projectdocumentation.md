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

The example below illustrates the steps. For a working example, see <!Index>.

``` python
# Step 1 : Read project files from root folder

proj = ProjectDocumentation("Project", "Documentation starts here")
proj.load_files(my_folder, sub_folders=['sub1', 'sub2'])

# Step 2 : Declare the classes to document

proj.add_class('Point',  capture = ['Geometry'])
proj.add_class('Vector', bases=['Point'])

# Step 3 : Add documentation

proj.new_section("Presentation", comment = "This the a geometry project")

# Step 4 : Compile

proj.compile()

# Step 5 : Create the documentation

proj.create_documentation(doc_folder)
```



## Methods and Properties
- A : [add_class](#add_class) [add_module](#add_module) 
- C : [compile](#compile) [create_index_file](#create_index_file) 
- L : [load_files](#load_files) 

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
## create_index_file

``` python
ProjectDocumentation.create_index_file(self, file_name)
```

Create the index file



##### Arguments

- **file_name** (_str_) : file name to write



<sub>[top](#projectdocumentation) [index](index.md)</sub>
## load_files

``` python
ProjectDocumentation.load_files(self, folder, sub_folders=[])
```

Load content from source code files.

Each file is loaded in an instance of <!Module> in the <!#modules> list.



##### Arguments

- **folder** (_str_) : main folder
- **sub_folders** (_str_) : sub folders to explore

##### Returns

- _self_



<sub>[top](#projectdocumentation) [index](index.md)</sub>

