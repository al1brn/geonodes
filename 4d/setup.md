# Global setup

## Groups

Around 30 nodes trees are generated with **geonodes**.

To keep the things clean are ordered, we me use of the *goenodes.Groups* class:

``` python

import geonodes as gn

modifiers = gn.Groups("4D")
maths     = gn.Groups("Maths 4D")

```

A *Groups* class manages a prefix which is added to the node trees name.
In *geonodes*, it can be then used to call a node has a python function.

The following code shows how building and then using a utility nodes tree.

``` python

import geonodes as gn

# Utility nodes tree

with gn.Tree("Maths 4D Do something", group=True) as tree:

  # Return 1 ;-)
  
  gn.Float(1).to_output("One")
  
# We need this utility somewhere

with gn.Tree("Maths 4D Do something else", group=True) as tree:

  node = gn.Group("Maths 4D Do something")
  my_one = node.one

```

In the following code, we use the *Groups* class to ease this naming process.
Note that the python names are the snake_case version of the trees and sockets names.
The result of these two pieces of code are exactly the same.

``` python

import geonodes as gn

# Utility nodes tree

with gn.Tree(maths.name("Do something"), group=True) as tree:

  # Return 1 ;-)
  
  gn.Float(1).to_output("One")
  
# We need this utility somewhere

with gn.Tree(maths.name("Do something else"), group=True) as tree:

  node = maths.do_something()
  my_one = node.one

```


  
 



