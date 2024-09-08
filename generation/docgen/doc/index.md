# Test

This is the **DocGen** documentation generated with the projet itself.

See the demo source code in [ProjectDocumentation](projectdocumentation.md).


## Project classes


The project is made of two layers.
1. The first layer is the parser which parses python source code. It returns a list of items (classes and functions) with their comment.
2. The second layer builds documented classes from the results of the parsing. One can them organize the documentation in the desired hierarchy.

> [!NOTE]
> Documentating a class must be explicitly requested with [ProjectDocumentation](projectdocumentation.md#add_class)


### Parser classes

- [Parser](parser.md) : simple python source code parser
- [Doc](doc.md) : list of items documentation returned by the [Parser](parser.md)




### DocGen classes

- [ProjectDocumentation](projectdocumentation.md) : Project documentation
- [Class](class.md) : Class documentation
- [Function](function.md) : Function documentation
- [Section](section.md) : Base documentation section




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




