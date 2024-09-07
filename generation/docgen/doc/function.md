# Function



Section dedicated to function documentation.

A **Function** is made of two sections:
- Properties
- Methods

The comment can contain description of Arguments and Returns.
The comment is parsed in order to extract this information and to
write the document is a homogeneous way.




**inherits from** Section 

## Methods and Properties
- A : [arguments](#arguments) [arguments](#arguments) 
- F : [FromDoc](#fromdoc) 
- P : [parse_comment](#parse_comment) 
- R : [returns](#returns) 

# Properties

## arguments





# Methods

## FromDoc

Create a class from an instance of Doc

Doc is a class read by the **Parser**.



##### Arguments

- **doc** (_Doc_) : Doc parsed by **Parser**


## arguments




## parse_comment

Function comment parser

The Function parser extracts Arguments and Returns sections.
The corresponding lines are remove from the comment to feed the two sections.

The lists are generated from the structure




## returns





