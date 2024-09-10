# Demo

This demo file is the source code used to generate this documentation

``` python
def gen_docgen():

    # ====================================================================================================
    # Step 1 : Read project files from root folder

    comment = "This is the **DocGen** documentation generated with the projet itself."

    root = Path(__file__).parents[0]
    proj = Project('Simple Python Documentation Generator', comment=comment)
    proj.load_files(root, sub_folders=[])

    # ====================================================================================================
    # Step 2 : Build the pages

    page = proj.new_page("Parser module", "Simple python source parser\n\n")
    page.write("The module <!Parser> parse source file and returns the documentation as a liste of <!Doc> instances.")

    proj.add_class('Parser', page,  capture = ['Reader'])
    proj.add_class('Doc', page)
    proj.add_function('.', page=page, file_key='docgen/pyparser', exact=False, only_commented=True)

    proj.add_class('Section')
    proj.add_class('Argument', bases=['Section'])
    proj.add_class('Return',   bases=['Section'])
    proj.add_class('Function', bases=['Section'])
    proj.add_class('Class',    bases=['Section'])
    proj.add_class('Project')

    # ====================================================================================================
    # Step 3 : Add complementary pages

    page = proj.new_page("Demo", "This demo file is the source code used to generate this documentation\n\n")

    page.write_source(inspect.getsource(gen_docgen))

    # ====================================================================================================
    # Finalize the index file (the project Section)

    struct = proj.new_section("Project classes", comment="""
        The project is made of two layers.
        1. The first layer is the reference document read from source files
        2. The second layer is a the set of pages of the documentation

        Pages are created and manually fed by reference documentation
        or by manuel additions.
        """)

    struct.new_section("Parser classes")
    struct.write("- <!Parser> : simple python source code parser\n")
    struct.write("- <!Doc> : list of items documentation returned by the [Parser](parser.md)\n")
    struct.write()

    struct.new_section("DocGen classes")
    struct.write("- <!Project> : Project documentation\n")
    struct.write("- <!Class> : Class documentation\n")
    struct.write("- <!Function> : Function documentation\n")
    struct.write("- <!Section> : Base documentation section\n")

    proj.new_section("Demo", "You can see in <!Demo> the source code used to generate this documentation.")

    # ====================================================================================================
    # Step 5 : Create the documentation

    # Demo custom hook
    proj.set_hook(r"\[!TOKEN\]", "substitution text")

    proj.create_documentation(doc_folder=root / 'doc')
```




