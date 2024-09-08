# Test

This is the **DocGen** documentation generated with the projet itself.

See the demo source code in [ProjectDocumentation](projectdocumentation.md).


## Project classes


The project is made of two layers.
1. The first layer is the parser which parses python source code. It returns a list of items (classes and functions) with their comment.
2. The second layer builds documented classes from the results of the parsing. One can them organize the documentation in the desired hierarchy.

> [!NOTE]
> Documentating a class must be explicitly requested with
[ProjectDocumentation](projectdocumentation.md#add_class)


### Parser classes

- [Parser](parser.md) : simple python source code parser
- [Doc](doc.md) : list of items documentation returned by the [Parser](parser.md)




### DocGen classes

- [ProjectDocumentation](projectdocumentation.md) : Project documentation
- [Class](class.md) : Class documentation
- [Function](function.md) : Function documentation
- [Section](section.md) : Base documentation section




## Source code example


The example given below is the source code used to generate this documentation:

``` python
def gen_docgen():

    # ====================================================================================================
    # Step 1 : read project files from root folder

    comment = """ This is the **DocGen** documentation generated with the projet itself.

    See the demo source code in [ProjectDocumentation](projectdocumentation.md).
    """

    root = Path(__file__).parents[0]
    proj = ProjectDocumentation.FromFiles('Test', folder=root, sub_folders=[], comment=comment)

    # ====================================================================================================
    # Step 2 : build document hierarchy

    proj.add_class('Parser',   capture = ['Reader'])
    proj.add_class('Doc')

    proj.add_class('Section')
    proj.add_class('Argument', bases=['Section'])
    proj.add_class('Return',   bases=['Section'])
    proj.add_class('Function', bases=['Section'])
    proj.add_class('Class',    bases=['Section'])
    proj.add_class('Module')
    proj.add_class('ProjectDocumentation')

    # ====================================================================================================
    # Step 3 : add documentation

    struct = proj.new_section("Project classes", comment="""
        The project is made of two layers.
        1. The first layer is the parser which parses python source code. It returns
           a list of items (classes and functions) with their comment.
        2. The second layer builds documented classes from the results of the parsing.
           One can them organize the documentation in the desired hierarchy.

        > [!NOTE]
        > Documentating a class must be explicitly requested with
        [ProjectDocumentation](projectdocumentation.md#add_class)
        """)

    struct.new_section("Parser classes")
    struct.write("- [Parser](parser.md) : simple python source code parser\n")
    struct.write("- [Doc](doc.md) : list of items documentation returned by the [Parser](parser.md)\n")
    struct.write()

    struct.new_section("DocGen classes")
    struct.write("- [ProjectDocumentation](projectdocumentation.md) : Project documentation\n")
    struct.write("- [Class](class.md) : Class documentation\n")
    struct.write("- [Function](function.md) : Function documentation\n")
    struct.write("- [Section](section.md) : Base documentation section\n")

    proj.new_section("Source code example", comment="""
        The example given below is the source code used to generate this documentation:

        """)
    proj.write_source(inspect.getsource(gen_docgen))

    # ====================================================================================================
    # Step 4 : compile

    proj.compile()

    # ====================================================================================================
    # Step 5 : write the documentation

    proj.create_documentation(doc_folder=root / 'doc')

    print(inspect.getsource(tests))
```




## Classes

- [Argument](argument.md)
- [Class](class.md)
- [Doc](doc.md)
- [Function](function.md)
- [Module](module.md)
- [Parser](parser.md)
- [ProjectDocumentation](projectdocumentation.md)
- [Return](return.md)
- [Section](section.md)




