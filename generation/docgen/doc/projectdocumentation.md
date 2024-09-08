# ProjectDocumentation

``` python
ProjectDocumentation(self, name)
```

Project documentation

Buildinf project documentation follows the following steps:
1. Creating the modules
2. Adding the classes to document. The classes must be documented in a module
3. Compile the documentation to build links between pages
4. Write the documentation files

The example below write the documentation for this project:

``` python
# Step 1 : read project files from root folder

root = Path(__file__).parents[0]
proj = ProjectDocumentation.FromFiles('Test', folder=root)

# Step 2 : build document hierarchy

proj.add_class('Parser', capture=['Reader'])
proj.add_class('Doc')

proj.add_class('Section')
proj.add_class('Argument', bases=['Section'])
proj.add_class('Return',   bases=['Section'])
proj.add_class('Function', bases=['Section'])
proj.add_class('Class',    bases=['Section'])
proj.add_class('Module')
proj.add_class('ProjectDocumentation')

# Step 3 : compile

proj.compile()

# Step 4 : write the documentation

proj.write_documentation(doc_folder=root / 'doc')
```



## Methods and Properties
- A : [add_module](#add_module) 
- W : [write_index](#write_index) 

# Methods

## add_module

``` python
ProjectDocumentation.add_module(self, name, text)
```

Add a




## write_index

``` python
ProjectDocumentation.write_index(self, file_name)
```

Write the index file



##### Arguments

- **file_name** (_str_) : file name to write



