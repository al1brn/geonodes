
# class Socket



## List of methods

- [\_\_init\_\_](#\_\_init\_\_)
- [bl\_idname](#bl\_idname)
- [enabled](#enabled)
- [enabling\_params](#enabling\_params)
- [gen\_init](#gen\_init)
- [is\_multi\_input](#is\_multi\_input)
- [is\_output](#is\_output)
- [user\_name](#user\_name)

## Methods




### \_\_init\_\_


<sub>go to  [Socket](#class-socket)</sub>


```python
def __init__(self, bsocket, index):
```


### bl\_idname


<sub>go to  [Socket](#class-socket)</sub>


```python
@property
def bl_idname(self):
```



### enabled


<sub>go to  [Socket](#class-socket)</sub>


```python
@property
def enabled(self):
```


### enabling\_params


<sub>go to  [Socket](#class-socket)</sub>


```python
@property
def enabling_params(self):
```


> When an enum parameter is read from a Node, all its possibles values are tried
At each try, the enablement of the socket is stored:


- param_1 if enabled
- param_0 otherwise

If one of these two lists is empty, it does mean that the parametert doesn't drive the enablement

### gen\_init


<sub>go to  [Socket](#class-socket)</sub>


```python
@property
def gen_init(self):
```


> Initalization source code

Input socket sample:
SocketIn(self, 'NodeSocketVectorEuler', 'rotation')

Output socket sample:

### is\_multi\_input


<sub>go to  [Socket](#class-socket)</sub>


```python
@property
def is_multi_input(self):
```


### is\_output


<sub>go to  [Socket](#class-socket)</sub>


```python
@property
def is_output(self):
```


### user\_name


<sub>go to  [Socket](#class-socket)</sub>


```python
@staticmethod
def user_name(name):
```





# class Sockets


> A list of sockets

## List of methods

- [Inputs](#inputs)
- [Outputs](#outputs)
- [build\_unames](#build\_unames)
- [check\_uniques](#check\_uniques)
- [enabled\_indices](#enabled\_indices)
- [enabled\_names](#enabled\_names)
- [enabled\_sockets](#enabled\_sockets)
- [enabled\_unique\_names](#enabled\_unique\_names)
- [enablement](#enablement)
- [geometry\_socket\_index](#geometry\_socket\_index)
- [get\_unames](#get\_unames)
- [has\_geometry\_socket](#has\_geometry\_socket)
- [multi\_input\_index](#multi\_input\_index)
- [names](#names)
- [new\_param](#new\_param)
- [new\_param\_value](#new\_param\_value)
- [self\_index](#self\_index)
- [set\_unames](#set\_unames)
- [unames](#unames)
- [unique\_names](#unique\_names)
- [uniques](#uniques)
- [update\_unames](#update\_unames)

## Methods




### Inputs


<sub>go to  [Sockets](#class-sockets)</sub>


```python
@classmethod
def Inputs(cls, bnode):
```


### Outputs


<sub>go to  [Sockets](#class-sockets)</sub>


```python
@classmethod
def Outputs(cls, bnode):
```


### build\_unames


<sub>go to  [Sockets](#class-sockets)</sub>


```python
@property
def build_unames(self):
```


### check\_uniques


<sub>go to  [Sockets](#class-sockets)</sub>


```python
def check_uniques(self):
```



### enabled\_indices


<sub>go to  [Sockets](#class-sockets)</sub>


```python
@property
def enabled_indices(self):
```


### enabled\_names


<sub>go to  [Sockets](#class-sockets)</sub>


```python
@property
def enabled_names(self):
```


### enabled\_sockets


<sub>go to  [Sockets](#class-sockets)</sub>


```python
@property
def enabled_sockets(self):
```


### enabled\_unique\_names


<sub>go to  [Sockets](#class-sockets)</sub>


```python
@property
def enabled_unique_names(self):
```


### enablement


<sub>go to  [Sockets](#class-sockets)</sub>


```python
@property
def enablement(self):
```


### geometry\_socket\_index


<sub>go to  [Sockets](#class-sockets)</sub>


```python
@property
def geometry_socket_index(self):
```



### get\_unames


<sub>go to  [Sockets](#class-sockets)</sub>


```python
def get_unames(self, enabled=True):
```


### has\_geometry\_socket


<sub>go to  [Sockets](#class-sockets)</sub>


```python
@property
def has_geometry_socket(self):
```


### multi\_input\_index


<sub>go to  [Sockets](#class-sockets)</sub>


```python
@property
def multi_input_index(self):
```



### names


<sub>go to  [Sockets](#class-sockets)</sub>


```python
@property
def names(self):
```


### new\_param


<sub>go to  [Sockets](#class-sockets)</sub>


```python
def new_param(self, param_name):
```



### new\_param\_value


<sub>go to  [Sockets](#class-sockets)</sub>


```python
def new_param_value(self, param_name, value):
```


### self\_index


<sub>go to  [Sockets](#class-sockets)</sub>


```python
def self_index(self, default=None):
```



### set\_unames


<sub>go to  [Sockets](#class-sockets)</sub>


```python
def set_unames(self, unames):
```


### unames


<sub>go to  [Sockets](#class-sockets)</sub>


```python
@unames.setter
def unames(self, values):
```


### unique\_names


<sub>go to  [Sockets](#class-sockets)</sub>


```python
@staticmethod
def unique_names(names):
```


### uniques


<sub>go to  [Sockets](#class-sockets)</sub>


```python
@property
def uniques(self):
```


> Some sockets can share the same unique name
'uniques' property return a dictionary of the unique names
Each value of the dictionary contains:


- None : the unique name is always valid and point on only one socket
- dict : a dict keyed by the socket indices with the {param: [values]} driving the enablement


'value' : {0: {'data_type': ['FLOAT']},
           1: {'data_type': ['INT']},

### update\_unames


<sub>go to  [Sockets](#class-sockets)</sub>


```python
def update_unames(self):
```




# class Parameter



## List of methods

- [\_\_init\_\_](#\_\_init\_\_)
- [get\_values](#get\_values)
- [set\_value](#set\_value)

## Methods




### \_\_init\_\_


<sub>go to  [Parameter](#class-parameter)</sub>


```python
def __init__(self, node, name):
```


### get\_values


<sub>go to  [Parameter](#class-parameter)</sub>


```python
def get_values(self):
```


> Get the enum values
When type is str, try to set a wrong attribute et interpret the error

### set\_value


<sub>go to  [Parameter](#class-parameter)</sub>


```python
def set_value(self, value=None):
```


> Set the parameter value



# class Argument


> Node argument

Argument is either a node or a parameter

arg_type : 'SOCKET', 'PARAMETER', 'VARIATION'


## List of methods

- [\_\_init\_\_](#\_\_init\_\_)
- [comment](#comment)
- [header](#header)
- [is\_input](#is\_input)
- [is\_parameter](#is\_parameter)
- [is\_variation](#is\_variation)
- [node\_call](#node\_call)

## Methods




### \_\_init\_\_


<sub>go to  [Argument](#class-argument)</sub>


```python
def __init__(self, name, default, class_name, arg_type, is_multi=False, is_self=False, hooks={}):
```


### comment


<sub>go to  [Argument](#class-argument)</sub>


```python
@property
def comment(self):
```


### header


<sub>go to  [Argument](#class-argument)</sub>


```python
@property
def header(self):
```


### is\_input


<sub>go to  [Argument](#class-argument)</sub>


```python
@property
def is_input(self):
```


### is\_parameter


<sub>go to  [Argument](#class-argument)</sub>


```python
@property
def is_parameter(self):
```


### is\_variation


<sub>go to  [Argument](#class-argument)</sub>


```python
@property
def is_variation(self):
```


### node\_call


<sub>go to  [Argument](#class-argument)</sub>


```python
@property
def node_call(self):
```




# class Arguments



## List of methods

- [header](#header)
- [node\_call](#node\_call)
- [node\_creation](#node\_creation)

## Methods




### header


<sub>go to  [Arguments](#class-arguments)</sub>


```python
@property
def header(self):
```


### node\_call


<sub>go to  [Arguments](#class-arguments)</sub>


```python
@property
def node_call(self):
```


### node\_creation


<sub>go to  [Arguments](#class-arguments)</sub>


```python
def node_creation(self, node_name, ret='NODE', socket_name=None):
```




# class Node



## List of methods

- [\_\_init\_\_](#\_\_init\_\_)
- [bl\_idname](#bl\_idname)
- [build\_arguments](#build\_arguments)
- [class\_out](#class\_out)
- [function\_name](#function\_name)
- [gen\_attribute](#gen\_attribute)
- [gen\_comments](#gen\_comments)
- [gen\_field](#gen\_field)
- [gen\_function](#gen\_function)
- [gen\_function\_OLD](#gen\_function\_old)
- [gen\_method](#gen\_method)
- [gen\_node\_as\_property](#gen\_node\_as\_property)
- [gen\_node\_class](#gen\_node\_class)
- [gen\_socket\_property](#gen\_socket\_property)
- [get\_output\_unames](#get\_output\_unames)
- [get\_variation\_input\_unames](#get\_variation\_input\_unames)
- [node\_name](#node\_name)
- [out\_index](#out\_index)
- [out\_name](#out\_name)
- [read\_arguments](#read\_arguments)
- [set\_parameters](#set\_parameters)
- [split](#split)

## Methods




### \_\_init\_\_


<sub>go to  [Node](#class-node)</sub>


```python
def __init__(self, bnode):
```



### bl\_idname


<sub>go to  [Node](#class-node)</sub>


```python
@property
def bl_idname(self):
```



### build\_arguments


<sub>go to  [Node](#class-node)</sub>


```python
def build_arguments(self, only_enabled=False, variation={}, self_name=None, attribute=False, domain=None, data_type=None, hooks={}):
```



### class\_out


<sub>go to  [Node](#class-node)</sub>


```python
@property
def class_out(self):
```


### function\_name


<sub>go to  [Node](#class-node)</sub>


```python
def function_name(self, func_type='METHOD'):
```



### gen\_attribute


<sub>go to  [Node](#class-node)</sub>


```python
def gen_attribute(self, base_name, domains=None):
```


> Generate an attribute

class_name is either the str for the actual class_name

### gen\_comments


<sub>go to  [Node](#class-node)</sub>


```python
def gen_comments(self):
```



### gen\_field


<sub>go to  [Node](#class-node)</sub>


```python
def gen_field(self, func_name=None, return_class=None):
```



### gen\_function


<sub>go to  [Node](#class-node)</sub>


```python
def gen_function(self, func_name, variation={}, ret='NODE', socket_name=None):
```



### gen\_function\_OLD


<sub>go to  [Node](#class-node)</sub>


```python
def gen_function_OLD(self, func_type='METHOD', func_name=None, variation={}, return_class=None):
```



### gen\_method


<sub>go to  [Node](#class-node)</sub>


```python
def gen_method(self, meth_name, decorator=None, self_name=None, variation={}, ret='NODE', socket_name=None):
```



### gen\_node\_as\_property


<sub>go to  [Node](#class-node)</sub>


```python
def gen_node_as_property(self, prop_name, names=None, settable = False):
```


> A node can be considered as a property of a node socket:
NodeSeparateRGG is a property of Color
It is implemented in the following way

  @property
  def separate(self):
      if not hasattr(self, 'separate_'):
          self.separate_ = NodeSeparateRGB(self)
      return self.separate_

  @property
  def r(self):
      if not hasattr(self, 'r_'):
          self.r_ = self.separate.r
      return self.r_

  @r.setter
  def r(self, value):
      _ = self.separate
      self.r_ = value


### gen\_node\_class


<sub>go to  [Node](#class-node)</sub>


```python
def gen_node_class(self, is_attribute=False):
```



### gen\_socket\_property


<sub>go to  [Node](#class-node)</sub>


```python
def gen_socket_property(self):
```



### get\_output\_unames


<sub>go to  [Node](#class-node)</sub>


```python
def get_output_unames(self):
```



### get\_variation\_input\_unames


<sub>go to  [Node](#class-node)</sub>


```python
def get_variation_input_unames(self, variation={}):
```


> When a node is created, a parameter can be passed as argument or not
When passed as an argument, the use can change it
A change in parameter value can change the enablement of input sockets

### node\_name


<sub>go to  [Node](#class-node)</sub>


```python
@property
def node_name(self):
```



### out\_index


<sub>go to  [Node](#class-node)</sub>


```python
@property
def out_index(self):
```



### out\_name


<sub>go to  [Node](#class-node)</sub>


```python
@property
def out_name(self):
```


### read\_arguments


<sub>go to  [Node](#class-node)</sub>


```python
def read_arguments(self):
```


> Read the input arguments


- Only the enabled sockets
- Unique names
- With their indices

### set\_parameters


<sub>go to  [Node](#class-node)</sub>


```python
def set_parameters(self, variation):
```



### split


<sub>go to  [Node](#class-node)</sub>


```python
@staticmethod
def split(word, left=""):
```




