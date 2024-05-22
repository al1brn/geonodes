#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Blender Python Geometry module

Created on Fri Nov 10 11:15:36 2023

@author: alain.bernard
@email: alain@ligloo.net

-----

Geometry domains are the core of geometry behavior. A domain manages dynamic attributes suc as position or radius.
Mesh, Curve, Instances and Cloud then manage the relationshp between the domains.

"""

import bpy

import numpy as np
from geonodes import Rotation, KDTree

from geonodes.maths.transformations import Transformations, axis_vector, axis_index
from geonodes.maths import splinesmaths

from geonodes.core import blender
from geonodes.core.attributes import Attributes

# =============================================================================================================================
# reduce indices
#
# selection is a list of indices to be renumeroted from 0 to max
# [7, 9, 9, 2, 5, 7] -> [2, 3, 3, 0, 1, 2]

def reduce_indices(indices, return_map=False):

    uniq = sorted(list(set(indices)))

    new_indices = np.zeros(np.max(uniq) + 1, int)
    new_indices[uniq] = np.arange(len(uniq))

    if return_map:
        return new_indices
    else:
        return np.array(new_indices[indices])


# =============================================================================================================================
# A domain can own its attributes or be a selection of a True domain

class Domain:

    # ====================================================================================================
    # Constructors

    def __init__(self, domain_name=None, owner=None, selector=None):
        """ A Domain can be initialized in two ways:
            - as a whole domain = domain_name is not None, owner is None
            - as a selection on a true domain : domain_name is None, owner is not None

        A whole domain owns its attributes when a selection get the attributes from its owner.

        The initialization is made by the following methods:
            - __init__ :
                - called for whole domains and selections
                - calls init_domain for initialization of common parameters
                - calls owner.init_selection for the owner to link its selection
            _ New (classmethod) :
                - calls __init__
                - initializes parameters proper to the whole domains
            - init_domain
                - initializes parameters common to selections and whole domains such as auto attributes
            - init_selection
                - allows an owner to complete the initialization of a selection

        The __init__ method is not supposed to be overriden. Use New, init_domain and init_selection in
        inherited classes. However __init__ can be overriden for initialization of 'intermediary' domains
        such as FaceSplineDomain.

        A whole domain is created with domain = Domain.New(*args).
        A selection is created with dom_sel = domain.selection(selector)

        Here after is simplified code for Face domain

        New(corners):
            __init__(domain_name='FACE')
            set corners attributes
            create and initializes attributes
            create attributes loop_start and loop_total

        init_domain
            create auto attributes such as material_index

        init_selection
            link the selection to corners
        """

        # ----- Create the attributes if whole domain

        if domain_name is None:
            assert(owner is not None)
            self._attributes = None
        else:
            assert(owner is None)
            assert(isinstance(domain_name, str))
            self._attributes = Attributes(domain=domain_name)

        # ----- Ownership

        self._owner    = owner
        self._selector = selector

        # ----- Auto attrbutes

        self.auto_attrs = {}

        # ----- Initialization common to whole domains and selections

        self.init_domain()

        # ----- Initialization of selections from its owner

        if self._owner is not None:
            self._owner.init_selection(self)

    # ====================================================================================================
    # Iteration

    def __iter__(self):
        self._iter_current = 0
        return self

    def __next__(self):
        if self._iter_current < len(self):
            self._iter_current += 1
            return self[self._iter_current - 1]
        raise StopIteration

    # ====================================================================================================
    # Selection : common methods

    # ----- Flag property

    @property
    def is_selection(self):
        """ The domain is a selection or not.

        Returns
        -------
            - bool : True if the domain instance is a selectionn False otherwise
        """

        return self._owner is not None

    # ----- Error message

    def no_selection(self, context="No conext"):
        """ Raises an error if the domain is a selection.

        Arguments
        ---------
            - Context (str="No context") : the string to use in the error message
        """

        if self.is_selection:
            raise RuntimeError(f"Domain {self.domain_name} error: the operation {context} is not possible for selections.")

    # ----- Build a selection from a selector

    def selection(self, selector):
        """ Select part of the domain items.

        The 'selector' argument must be a valid selection on the domain.
        The method return a sub domain pointing on itself (or the owner if the domain is already a selection)

        ``` python
        # Initialize POINT domain with 10 vectors
        points = domain.PointDomain.New()
        points.add(10, position = np.reshape(range(30), (10, 3)))

        print(f"My points : {points.shape=}")
        print(points.position)
        print()

        # Get a selection

        sub = points[points.position[:, 1] % 2 == 0]
        print((f"My selection : {sub.shape}="))
        print(sub.position)

        # Set the selection to -1

        sub.position = -1

        print("Modified points")
        print(points.position)
        ```

        Arguments
        ---------
            - selector (int, array of ints or array of bools) : a selection on the domain

        Returns
        -------
            - domain of the same type
        """

        if True:
            if self._owner is None:
                return type(self)(owner=self, selector=selector)
            elif isinstance(self._selector, slice):
                return type(self)(owner=self._owner, selector=np.arange(self.size)[self._selector][selector])
            else:
                return type(self)(owner=self._owner, selector=self._selector[selector])

        # OLD OLD OLD OLD OLD OLD OLD OLD


        sel = np.reshape(np.arange(self.size), self.shape)[selector]

        if np.shape(sel) == ():
            sel = np.reshape(sel, (1,))

        if self._owner is None:
            return type(self)(owner=self, selector=sel)
        else:
            return type(self)(owner=self._owner, selector=self._selector[sel])

    # ----------------------------------------------------------------------------------------------------
    # Can be overriden

    # ----- Init domain (common to owner and selection)

    def init_domain(self):
        """ Initialization for whole domain and selections
        """

        self.add_auto_attribute('ID', 'INT', 0, transfer=False)

    # ----- Init selection

    def init_selection(self, selection):
        """ Init a domain selection.

        Used to link a selection to its owner properties.
        For example, a selection of Corner must be linked to the points attribute of its owner.

        Don't call this method directly. It is called in the initialization process.

        Arguments
        ---------
            - selection (Domain) : a domain of the same type
        """

        pass

    # ====================================================================================================
    # Serialization

    def as_dict(self):
        return self.attributes.as_dict()

    @classmethod
    def FromDict(cls, domain_name, d):
        domain = cls(domain_name)
        domain._attributes = Attributes.FromDict(d)

        return domain

    # ====================================================================================================
    # Auto attributes

    def add_auto_attribute(self, name, data_type, default, transfer=True):
        """ Auto attributes are optional attributes which can be automatically created when used tries to read or write them.

        For instance, the Cloud domains declares the auto attribute 'radius' withe default value 1. It is created
        only if the user read or write this property.

        ``` python
        points = domain.PointDomain.New()
        points.add(10, position=(0, 0, 0))

        print("Current attributes")
        print(points)

        points.radius = 1.
        print("Radius was automatically created.")
        print(points)
        ```

        Arguments
        ----------
            - name (str) : attribute name
            - data_type (str) : attribute type
            - default (any) : default value
            - transfer (bool=True) : transfer as geometry attribute into Blender
        """

        self.auto_attrs[name] = {'data_type': data_type, 'default': default, 'transfer': transfer}

    def attribute_exists(self, name, create_if_auto=True):
        """ Check if an attribute name exists.

        Arguments
        ---------
            - name (str) : attribute name

        Returns
        -------
            - bool : True if the attribute exists, False otherwise
        """

        owner      = self.__dict__.get('_owner')
        attributes = self.__dict__.get('_attributes') if owner is None else owner.attributes

        if attributes is None:
            return False

        if attributes.exists(name):
            return True

        auto_attrs = self.__dict__.get('auto_attrs')
        if auto_attrs is None:
            return False

        #print('attribute_exists', self.domain_name, name, name in auto_attrs)

        if name in auto_attrs:
            if create_if_auto:
                attributes.new(name, **auto_attrs[name])
                return True
            else:
                return False

        return False

    def check_attributes(self, **attrs):
        """ Utility filtering the attributes existing in the domain.

        When updating an geometry with several domains, the attribute must be selected per domain.

        Arguments
        ---------
            - attrs (dict) : dictionnary of attribute names, attribute values

        Returns
        -------
            - dict : the key, values for existing attrubutes
        """

        return {name: value for name, value in attrs.items() if self.attribute_exists(name)}

    # ====================================================================================================
    # Main properties

    @property
    def attributes(self):
        """ Acces to the domain attributes.

        If the domain is a selection access to the attributes of its owner, otherwise access to
        its own attributes.

        Returns
        -------
            - Attributes : domain attributes
        """

        return self._attributes if self._owner is None else self._owner.attributes

    @property
    def domain_name(self):
        """ Doamin name

        Returns
        --------
            - str : domain name
        """

        return self.attributes.domain

    def __str__(self):
        if self._selector is None:
            return f"<Domain {self.domain_name:8s} ({len(self):5d}), attributes: {list(self.attributes.infos.keys())}>"
        else:
            return f"<Domain {self.domain_name:8s} ({len(self):5d}), attributes: {list(self.attributes.infos.keys())}, selection on {self._owner}>"


    # ====================================================================================================
    # Attributes access as property names

    def get_attribute(self, name):
        if self._selector is None:
            return self._attributes[name]
        else:
            return self._owner.attributes[name][self._selector]

    def set_attribute(self, name, value):

        if self._selector is None:

            a = self._attributes[name]
            target_size = np.size(a)
            in_size     = np.size(value)

            # ----- If shapes have same length, value can be the value of one instance among n
            # a = n * value

            if len(np.shape(a)) == len(np.shape(value)):

                # Sizes are equal : no broadcast

                if in_size == target_size:
                    a[:] = value

                # Size of a is multiple of size of value

                elif target_size % in_size == 0:
                    np.reshape(a, (in_size, target_size//in_size))[:] = np.reshape(value, (in_size, 1))

                # Error

                else:
                    raise AttributeError(f"Domain.set_attribute: Impossible to set value of shape {np.shape(value)} to attribute of shape {np.shape(a)}.")

            # ----- Standard broadcast

            else:
                a[:] = value

        else:
            self._owner.attributes[name][self._selector] = value

    def __getattr__(self, name):
        if self.attribute_exists(name):
            return self.get_attribute(name)
        else:
            raise AttributeError(f"Domain '{self.domain_name}' doesn't have '{name}' attribute.")

    def __setattr__(self, name, value):
        if self.attribute_exists(name):
            self.set_attribute(name, value)
            return

        super().__setattr__(name, value)

    def set_attributes(self, **attributes):
        for name, value in attributes.items():
            setattr(self, name, value)

    # ----------------------------------------------------------------------------------------------------
    # Add attributes

    def new_attribute(self, name, data_type, default, transfer=True):
        """ Add a new domain attribute.

        Use preferrably user friendly methods 'new_float_attribute', 'new_vector_attribute', ...

        Arguments
        ----------
            - name (str) : attribute name
            - data_type (str) : attribute type
            - default (any) : default value
            - transfer (bool=True) : transfer as geometry attribute into Blender

        """
        self.attributes.new(name, data_type, default, transfer=transfer)


    def new_float_attribute(self, name, default=0., transfer=True):
        """ Create a new attribute of type FLOAT -> float.

        Arguments
        ---------
            - name (str) : attribute name
            - default (float=0) : default value
            - transfer (bool=True) : transfer the attribute to the Blender mesh
        """

        self.new_attribute(name, 'FLOAT', default, transfer=transfer)

    def new_vector_attribute(self, name, default=(0., 0., 0.), transfer=True):
        """ Create a new attribute of type FLOAT_VECTOR -> array of 3 floats.

        Arguments
        ---------
            - name (str) : attribute name
            - default (tuple=(0, 0, 0)) : default value
            - transfer (bool=True) : transfer the attribute to the Blender mesh
        """

        self.new_attribute(name, 'FLOAT_VECTOR', default, transfer=transfer)

    def new_int_attribute(self, name, default=0, transfer=True):
        """ Create a new attribute of type INT -> int.

        Arguments
        ---------
            - name (str) : attribute name
            - default (int=0) : default value
            - transfer (bool=True) : transfer the attribute to the Blender mesh
        """

        self.new_attribute(name, 'INT', default, transfer=transfer)

    def new_bool_attribute(self, name, default=False, transfer=True):
        """ Create a new attribute of type BOOLEAN -> bool.

        Arguments
        ---------
            - name (str) : attribute name
            - default (bool=False) : default value
            - transfer (bool=True) : transfer the attribute to the Blender mesh
        """

        self.new_attribute(name, 'BOOLEAN', default, transfer=transfer)

    def new_color_attribute(self, name, default=(0.5, 0.5, 0.5, 1.), transfer=True):
        """ Create a new attribute of type FLOAT_COLOR -> array of 4 floats.

        Arguments
        ---------
            - name (str) : attribute name
            - default (tuple=(0, 0, 0, 1)) : default value
            - transfer (bool=True) : transfer the attribute to the Blender mesh
        """

        self.new_attribute(name, 'FLOAT_COLOR', default, transfer=transfer)

    def new_vector2_attribute(self, name, default=(0., 0.), transfer=True):
        """ Create a new attribute of type FLOAT2 -> array of 2 floats.

        Arguments
        ---------
            - name (str) : attribute name
            - default tuple=(0, 0)) : default value
            - transfer (bool=True) : transfer the attribute to the Blender mesh
        """

        self.new_attribute(name, 'FLOAT2', default, transfer=transfer)


    # ----------------------------------------------------------------------------------------------------
    # Items

    def __len__(self):
        if self._selector is None:
            return len(self.attributes)
        elif np.shape(self._selector) == ():
            return 1
        else:
            return len(self._selector)

    def __getitem__(self, index):
        return self.selection(index)

        if self._owner is None:
            return self.domain_selection(self, index)
        else:
            return self.domain_selection(self._owner, self._selector[index])

    def shaped(self, *shape):
        """ Return a shaped selection of the domain.

        Offers a numpy-like interface for multi dimensional domains

        ''' python
        grid = Mesh.Grid(10, 10, vertices_x=100, vertices_y=100)

        points = grid.points.shaped(100, 100)
        points[range(100), range(100)].position += (0, 0, 1)

        points[12, 67].position += (0, 0, 1)

        grid.to_object("Grid")
        ```

        Arguments
        ---------
            - *shape : the shape compatible with the current size

        Returns
        -------
            - domain selection
        """

        self.no_selection("Shaped")

        if len(shape) == 1:
            shape = shape[0]
            if not hasattr(shape, '__len__'):
                shape = (shape,)

        shape = tuple(shape)

        """
        print("SHAPE", shape)

        try:
            sel = np.reshape(range(self.size), self.shape)[shape]
            print("SEL", np.shape(sel))
        except:
            raise RuntimeError(f"Domain Error: Impossible to reshape domain '{self.domain_name}' of size {self.size} into shape {shape}.")

        return self.selection(sel)

        #return self.selection(np.reshape(range(self.size), shape))
        """

        size = 1
        i_empty = None
        for i, v in enumerate(shape):
            if v is None:
                if i_empty is not None:
                    raise RuntimeError(f"Domain Error: domain shape {shape} is not valid: only one 'None' dimension is accepted")
                i_empty = i
            else:
                size *= v

        if i_empty is not None:
            missing_size = len(self)//size
            shape = tuple([missing_size if i==i_empty else v for i, v in enumerate(shape)])

        #shape = np.broadcast_shapes(shape)

        if np.prod(shape, dtype=int) != len(self):
            raise RuntimeError(f"Domain Error: Impossible to reshape domain '{self.domain_name}' of length {len(self)} into shape {shape}.")

        return self[np.reshape(np.arange(len(self)), shape)]

    # ====================================================================================================
    # Add / delete items

    @property
    def size(self):
        """ Domain size

        Returns
        -------
            - int : number of items in the domain
        """

        if self._selector is None:
            return len(self)
        else:
            return np.size(self._selector)

    @property
    def shape(self):
        """ Domain shape.

        Returns
        -------
            - tuple : domain shape
        """

        if self._selector is None:
            return (len(self),)
        else:
            return np.shape(self._selector)

    def add(self, count, **attrs):
        """ Create new domain items.

        Arguments
        ---------
            - count (int) : number of items to create
            - attrs : attribute names, attribute values of the new items
        """

        if self._owner is None:
            inds = self.attributes.add(count, **self.check_attributes(**attrs))
        else:
            inds = self._owner.attributes.add(count, **self.check_attributes(**attrs))

        return inds

    def add_from_domain(self, domain):
        """ Create new items by copying the items of another domain.

        Arguments
        ---------
            - domain (Domain) : other domain
        """

        self.attributes.copy_definitions(domain.attributes)
        return self.add(len(domain), **{name: getattr(domain, name) for name in domain.attributes.names})

    def delete(self, selection):
        """ Delete a selection of items.

        Arguments
        ---------
            - selection (int or array of ints or array of bools) : items to delete
        """

        self.no_selection("Delete")

        if self._owner is None:
            self.attributes.delete(selection)
        else:
            self._owner.attributes.delete(selection)

    # ====================================================================================================
    # Dump

    def dump(self, title="Dump", attributes=None, target='SCREEN'):
        """ Dump the content for an Excel sheet or to be displayed at the screen.
        """

        # ---------------------------------------------------------------------------
        # Formatting a value

        def sv(v):
            if target == 'SCREEN':
                if isinstance(v, (float, np.float64)):
                    return f"{v:.1f}"
                else:
                    return str(v)
            else:
                return str(v)

        # ---------------------------------------------------------------------------
        # Colum width

        def build_col(values):
            col = [sv(v) for v in values]
            col_len = max([len(s) for s in col])
            return col, col_len

        # ---------------------------------------------------------------------------
        # Main

        # ----- Selected attributes

        if attributes is None:
            attributes = list(self.attributes.infos.keys())

        # ---- Columns

        sizes   = []
        cols    = []
        for name in attributes:
            size = self.attributes.attribute_size(name)
            sizes.append(size)
            cols.append([] for _ in range(size))

        # ----- Data lines

        cols     = []
        col_lens = []
        for i_attr, name in enumerate(attributes):

            values = self.attributes[name]

            size = sizes[i_attr]
            if size == 1:
                new_col, l = build_col(values)
                cols.append(new_col)
                col_lens.append(l)

            else:
                cols.append([])

                new_col, l0 = build_col(values[:, 0])
                cols[-1].append(new_col)

                new_col, l1 = build_col(values[:, 1])
                cols[-1].append(new_col)

                new_col, l2 = build_col(values[:, 2])
                cols[-1].append(new_col)

                col_lens.append(max(l0, l1, l2))

        for i, name in enumerate(attributes):
            if sizes[i] == 3:
                continue

            col_lens[i] = max(col_lens[i], len(name))

        # ----- Excel formatting

        data  = '-'*50 + f"\n{title}\nDOMAIN {self.domain_name} DUMP: {len(self)} items\n"
        if target == 'EXCEL':

            # Header

            for name, size in zip(attributes, sizes):
                if size == 1:
                    data += f"{name}; "
                else:
                    data += f"{name}_x; {name}_y; {name}_z; "

            data += "\n"

            # Data lines

            for i in range(len(selection)):
                for size, col in zip(sizes, cols):
                    if size == 1:
                        data += f"{col[i]}; "
                    else:
                        data += f"{col[0][i]}; {col[1][i]}; {col[2][i]}; "
                data += "\n"

        # ----- Screen formatting

        else:

            # Header line

            header_line = "num  | "
            for name, size, col_len in zip(attributes, sizes, col_lens):
                n = col_len if size == 1 else col_len*3 + 4
                header_line += f"{name:{n}s} | "
            header_line += "\n"

            # Data lines

            for i in range(len(self)):
                if i % 50 == 0:
                    data += header_line

                data += f"{i:4d} | "
                for size, col_len, col in zip(sizes, col_lens, cols):
                    if size == 1:
                        data += f"{col[i]:>{col_len}s} | "
                    else:
                        data += f"{col[0][i]:>{col_len}s}  {col[1][i]:>{col_len}s}  {col[2][i]:>{col_len}s} | "
                data += "\n"

        return data

    # =============================================================================================================================
    # Transformations

    # -----------------------------------------------------------------------------------------------------------------------------
    # Utility for transformations

    def block_size(self, other_shape):
        size = np.prod(other_shape, dtype=int)
        rem = self.size % size
        if rem != 0:
            raise RuntimeError(f"Domain error: impossible to combine domain of size {self.size} {self.shape} with array of size {size} {other_shape}.")
        return self.size // size

    # -----------------------------------------------------------------------------------------------------------------------------
    # Transform : locations, scales and eulers

    def transform(self, transf, pivot=None):
        """ Apply a transformation to the position.

        Note that if the size of the transformation doesn't match the size of the domain, the method trys to apply
        the transformation on blocks. This allow to operate transformation on arrays of geometries.

        If it is not possible to have blocks of the same size, an error is raised.

        ``` python
        # ----- An array of count cubes

        count = 10
        mesh = Mesh.Cube()*10

        # ----- Prepare the transformations

        ags = np.linspace(0, 2*np.pi, count, endpoint=False)
        locs = 10*np.stack((np.cos(ags), np.sin(ags), np.zeros(count, float)), axis=-1)

        transf = Transformations(position=locs)
        transf.rz = ags
        transf.sy = 2

        # ----- Apply to the mesh

        mesh.points.transform(transf)

        # ----- Transformations can be applied directly on the mesh

        mesh.points.scale((.5, 1, 1), pivot=locs)
        mesh.points.translate((0, 4, 0))
        mesh.points.rotate_x(np.linspace(0, 2, count))

        # ----- The domain can be shaped as an array of 8 points

        points = mesh.points.shaped((10, 8))
        for i in range(len(points)):
            points[i].translate((0, 0, i*3))
            points[i].translate((0, 0, 10))

        # ----- Let's view the result

        mesh.to_object("Cubes")
        ```

        Arguments
        ---------
            - transf (Transformations) : the transformation to apply
            - pivot (vector or array of vectors = None) : pivot around which the transformation must be performed

        Returns
        -------
            - self
        """

        # ----------------------------------------------------------------------------------------------------
        # Pivot

        if pivot is not None:
            translations = Transformations(position=pivot)
            translations.position *= -1
            self.transform(translations)

        # ----------------------------------------------------------------------------------------------------
        # Position

        if self.size == transf.size or transf.size == 1:
            self.position = transf @ self.position

        else:
            block_size = self.block_size(transf.shape)
            self.position = np.reshape(
                    transf[..., None] @ np.reshape(self.position, transf.shape + (block_size, 3)),
                    (len(self), 3))

        # ----------------------------------------------------------------------------------------------------
        # Bezier specific

        if self.attribute_exists('handle_left'):
            if self.size == transf.size or transf.size == 1:
                self.handle_left = transf @ self.handle_left
            else:
                self.handle_left = np.reshape(
                        transf[..., None] @ np.reshape(self.handle_left, transf.shape + (block_size, 3)),
                        (len(self), 3))

        if self.attribute_exists('handle_right'):
            if self.size == transf.size or transf.size == 1:
                self.handle_right = transf @ self.handle_right
            else:
                self.handle_right = np.reshape(
                        transf[..., None] @ np.reshape(self.handle_right, transf.shape + (block_size, 3)),
                        (len(self), 3))

        # ----------------------------------------------------------------------------------------------------
        # Position

        if pivot is not None:
            translations.position *= -1
            self.transform(translations)

        return self

    # -----------------------------------------------------------------------------------------------------------------------------
    # Translate

    def translate(self, vectors):
        """ Apply a translation on the positions.

        See Domain.Transform

        Arguments
        ---------
            - vectors (vectors) : translation
        Returns
        -------
            - self
        """

        if np.shape(vectors) == ():
            vectors = (vectors, vectors, vectors)

        return self.transform(Transformations(position=vectors))

    # -----------------------------------------------------------------------------------------------------------------------------
    # Change the position

    def locate(self, vectors):
        """ Change the positions.

        See Domain.Transform

        Arguments
        ---------
            - vectors (vectors) : the locations
        Returns
        -------
            - self
        """

        raise Exception(f"Not yet implemented")

        if np.shape(vectors) == ():
            vectors = (vectors, vectors, vectors)

        if self.size == np.size(vectors)//3 or np.size(vectors) == 1:
            self.position = vectors

        else:
            vshape = np.shape(vectors)[:-1]
            block_size = self.block_size(vshape)

            self.position = np.reshape(np.reshape(vectors, vshape + (1, 3)), (len(self), 3))

        return self

    # -----------------------------------------------------------------------------------------------------------------------------
    # Apply a scale factor

    def scale(self, scales, pivot=None):
        """ Apply a scale.

        See Domain.Transform

        Arguments
        ---------
            - vectors (vectors) : the locations
            - pivot (vector = None) : scale pivot
        Returns
        -------
            - self
        """

        if np.shape(scales) == ():
            scales = (scales, scales, scales)

        return self.transform(Transformations(scale=scales), pivot=pivot)

    # -----------------------------------------------------------------------------------------------------------------------------
    # Rotate the positions

    def rotate(self, rotations, pivot=None):
        """ Apply a rotation.

        See Domain.Transform

        Arguments
        ---------
            - vectors (vectors) : the locations
            - pivot (vector = None) : scale pivot
        Returns
        -------
            - self
        """

        return self.transform(Transformations(rotation=rotations), pivot=pivot)

    # -----------------------------------------------------------------------------------------------------------------------------
    # Rotate around the x axis

    def rotate_x(self, angle=0, pivot=(0, 0, 0)):
        """ Rotate the vertices around the x axis.

        Arguments
        ---------
            - angle (float=0) : rotation angle
            - pivot (array[3] of floats = (0, 0, 0)) : rotation pivot

        Returns
        -------
            - self
        """

        eulers = np.zeros(np.shape(angle) + (3,), float)
        eulers[..., 0] = angle
        return self.rotate(eulers, pivot=pivot)

    # -----------------------------------------------------------------------------------------------------------------------------
    # Rotate around the y axis

    def rotate_y(self, angle=0, pivot=(0, 0, 0)):
        """ Rotate the vertices around the y axis.

        Arguments
        ---------
            - angle (float=0) : rotation angle
            - pivot (array[3] of floats = (0, 0, 0)) : rotation pivot

        Returns
        -------
            - self
        """

        eulers = np.zeros(np.shape(angle) + (3,), float)
        eulers[..., 1] = angle
        return self.rotate(eulers, pivot=pivot)

    # -----------------------------------------------------------------------------------------------------------------------------
    # Rotate around the y axis

    def rotate_z(self, angle=0, pivot=(0, 0, 0)):
        """ Rotate the vertices around the z axis.

        Arguments
        ---------
            - angle (float=0) : rotation angle
            - pivot (array[3] of floats = (0, 0, 0)) : rotation pivot

        Returns
        -------
            - self
        """

        eulers = np.zeros(np.shape(angle) + (3,), float)
        eulers[..., 2] = angle
        return self.rotate(eulers, pivot=pivot)

    # -----------------------------------------------------------------------------------------------------------------------------
    # Rotate around

    def rotate_around(self, axis='Z', angle=0., pivot=None):
        """ Apply a rotation around an axis.

        Arguments
        ---------
            - axis (vectors=(0, 0, 1)) : the axis
            - angle (float=0) : the rotation angle
            - pivot (vector = None) : scale pivot
        Returns
        -------
            - self
        """

        axis = axis_vector(axis)
        if np.shape(angle) == ():
            axis *= angle
        else:
            axis = axis * angle[:, None]

        return self.transform(Transformations(rotation=Rotation.from_rotvec(axis)), pivot=pivot)

    # =============================================================================================================================
    # KDTree

    def kd_tree(self):
        return KDTree(self.position)

    def nearest(self, count=1, kd_tree=None):

        kdt = self.kd_tree() if kd_tree is None else kd_tree

        dist, inds = kdt.query(kdt.data, count+1)
        if count == 1:
            return dist[:, 1], inds[:, 1]
        else:
            return dist[:, 1:], inds[:, 1:]

    def ball_point(self, r=1., remove_self=False, kd_tree=None):

        kdt = self.kd_tree() if kd_tree is None else kd_tree

        a = kdt.query_ball_point(self.position, r=r, return_sorted=False)
        if remove_self:
            for i, l in enumerate(a):
                l.remove(i)

        return a





# ====================================================================================================
# Point Domain

class PointDomain(Domain):
    """ Point domain.

    This domain is common to all geometries:
        - Mesh : vertices
        - Curve : control points
        - Cloud : points
        - Instances : instance locations

    Attributes
    ----------
        - position (vector) : point position
        - radius (float, optional) : point radius
    """

    @classmethod
    def New(cls):
        point = cls(domain_name='POINT')
        point.attributes.new_vector('position', transfer=True)

        return point

    def init_domain(self):
        super().init_domain()

        self.add_auto_attribute('radius', 'FLOAT', 1., transfer=True)

    @classmethod
    def FromDict(cls, d):
        domain = cls.New()
        domain._attributes = Attributes.FromDict(d)

        return domain

    # =============================================================================================================================
    # Add vertices

    def add_points(self, position, **attributes):
        """ Add points to the domain.

        Arguments
        ---------
            - position (vector or array of vectors) : the position of the new points
            - attributes (attribute names, attribute values) : value of the point attributes
        """

        return self.add(np.size(position)//3, position=np.reshape(position, (np.size(position)//3, 3)), **attributes)


    # =============================================================================================================================
    # Properties

    @property
    def x(self):
        """ x coordinate.

        Shortcut for position[:, 0]
        """

        return self.position[..., 0]

    @x.setter
    def x(self, value):
        self.position[..., 0] = value

    @property
    def y(self):
        """ y coordinate.

        Shortcut for position[:, 1]
        """
        return self.position[..., 1]

    @y.setter
    def y(self, value):
        self.position[..., 1] = value

    @property
    def z(self):
        """ x coordinate.

        Shortcut for position[:, 2]
        """

        return self.position[..., 2]

    @z.setter
    def z(self, value):
        self.position[..., 2] = value


    @property
    def bounding_box(self):
        if len(self):
            return np.min(self.position, axis=0), np.max(self.position, axis=0)
        else:
            return np.zeros(3, float), np.zeros(3, float)

    # =============================================================================================================================
    # Simple transformations

    # ----------------------------------------------------------------------------------------------------
    # Twist

    def twist(self, angle=np.pi/4, origin=(0, 0, 0), direction='X', angle_per_unit=False):
        """ Twist around a line.

        ``` python
        # Build a squared cylinder along x
        cyl = Mesh.Cylinder(vertices=4, depth=10, side_segments=100, transformation=Transformations(rotation=(0, np.pi/2, 0)))

        # Twist along x axis
        cyl.points.twist(2*np.pi, direction='X', angle_per_unit=False)

        # To object
        cyl.to_object("Twist", shade_smooth=False)
        ```

        Arguments
        ---------
            - angle (float=pi/4) : rotation par unit
            - origin (array[3] of floats) : a point on the line to twist around
            - direction (str = 'X') : axis name
            - angle_per_unit (bool=False) : angle is interpretad as a rotation per unit rather than the total twist angle

        Returns
        -------
            - self
        """

        # Unary vector for the direction

        u = axis_vector(direction)

        # Project the vertices on the line
        # The projected points are the centers of the rotations
        # The distance gives the angle to rotate

        d = np.dot(self.position, u)
        cs = u*d[:, None] + origin

        if angle_per_unit:
            ags = d*angle

        else:
            d0  = np.min(d)
            d1  = np.max(d)
            ags = (d - d0)/(d1 - d0)*angle - angle/2

        u_i = axis_index(u, False)

        eulers = np.zeros((len(ags), 3), float)
        eulers[:, u_i] = ags

        transf = Transformations(rotation=eulers)
        self.transform(transf, pivot=cs)


        return self

    # ----------------------------------------------------------------------------------------------------
    # Bend

    def bend(self, angle=np.pi/2, axis='Z', direction='X', pivot=(0, 0, 0)):
        """ Bend.

        ``` python
        # Build a squared cylinder along x
        cyl = Mesh.Cylinder(vertices=4, depth=10, side_segments=100, transformation=Transformations(rotation=(0, np.pi/2, 0)))
        cyl.to_object("Base", shade_smooth=False)

        # Twist along x axis
        cyl.points.bend(angle=np.pi, axis='Z', direction='X')

        # To object
        cyl.to_object("Bend", shade_smooth=False)
        ```

        Arguments
        ---------
            - angle (float=pi/4) : bend angle
            - axis (axis = 'Z') : rotation axis
            - direction (axis='X') : to direction of the line to bend
            - pivot (axis='X') : The invariant point in the line

        Returns
        -------
            - self
        """
        angle = np.clip(angle, -np.pi*2, np.pi*2)
        if abs(angle) < 0.0001:
            return self

        # ----------------------------------------------------------------------------------------------------
        # Rotate such as
        # - the rotation is around the z axis
        # - the bent line is along the x axis
        # - crossing the y axis at location r

        k = axis_vector(axis)
        i = axis_vector(direction) # Not necessarily normal to k
        j = np.cross(k, i)
        j /= np.linalg.norm(j)

        M = np.array((np.cross(j, k), j, k))

        verts = np.einsum('...ij, ...j', M, self.position - pivot)

        # ----------------------------------------------------------------------------------------------------
        # We take a radius such as 2pi makes a circle

        x0 = np.min(verts[:, 0])
        x1 = np.max(verts[:, 0])
        length = x1 - x0

        radius = length/angle

        # ----------------------------------------------------------------------------------------------------
        # x gives the angles

        ags  = -verts[:, 0]*(angle/length)

        # ----------------------------------------------------------------------------------------------------
        # y is the "altitude" from the radius

        rs = verts[:, 1] - radius
        verts[:, 0] = rs*np.sin(ags)
        verts[:, 1] = rs*np.cos(ags) + radius

        # ----------------------------------------------------------------------------------------------------
        # Back to initial space

        self.position = np.einsum('...ij, ...j', M.T, verts) + pivot

        return self

    # ----------------------------------------------------------------------------------------------------
    # Shear

    def shear(self, ratio=1., axis='X', plane='Y', pivot=(0, 0, 0), selection=None):
        """ Shear the selection.

        ``` python
        # ----- Build a frame

        cube = MeshBuilder.Cube()
        cube.scale((2, .3, .3))

        # ----- Select left and right faces in two ways

        left_face = cube.sel_faces_from_verts(np.argwhere(cube.verts[:, 0] < -.5).flatten())[0]
        right_face = cube.sel_faces_where(lambda faces: cube.normals(faces)[:, 0] > .5)[0]

        # ----- Left and right shear

        cube.shear(1, axis='X', plane='Y', selection=cube.sel_faces_verts(left_face))
        cube.shear(-1, axis='X', plane='Y', selection=cube.sel_faces_verts(right_face))

        # ----- Extrusion downwards

        cube.extrude([left_face, right_face], offset=3, direction='-Z')

        # ----- Inverse the shear

        cube.shear(2, axis='Z', plane='Y', pivot=cube.centers(left_face), selection=cube.sel_faces_verts(left_face))
        cube.shear(-2, axis='Z', plane='Y', pivot=cube.centers(right_face), selection=cube.sel_faces_verts(right_face))

        # ----- Bridge the two last faces

        cube.bridge_faces(left_face, right_face)

        cube.to_object("Shear", shade_smooth=False)
        ```

        Arguments
        ---------
            - ratio (float=1.) : multiply the distance to the axis to get the translation
            - axis (axis='X') : shear direction
            - plane (axis='Z') : shear plane defined by a perpendicular vector
            - pivot (vector=(0, 0, 0)) : pivot
            - selection (vertice selection=None) : vertex indices which must be sheared

        Returns
        -------
            - self
        """

        if True:
            verts = self.position - pivot

            # ----- Axis and plane

            axis  = axis_vector(axis)
            plane = axis_vector(plane)
            perp = np.cross(plane, axis)

            # ----- Signed distance to the shear axis

            d = np.einsum('...i, ...i', verts, perp)

            self.position += (d[:, None]*ratio)*axis


        else:
            selection = self.get_verts_selector(selection)
            sel_verts = self._verts[selection] - pivot

            # ----- Axis and plane

            axis  = axis_vector(axis)
            plane = axis_vector(plane)
            perp = np.cross(plane, axis)

            # ----- Signed distance to the shear axis

            d = np.einsum('...i, ...i', sel_verts, perp)

            self._verts[selection] += (d[:, None]*ratio)*axis

        return self

# ====================================================================================================
# Corner Domain

class CornerDomain(Domain):
    """ Corner domain stores a vertex index for face descriptions.

    This domain is specific to Mesh geometry.
    It keeps a pointer to the Mesh POINT domain.

    Attributes
    ----------
        - vertex_index (int) : vertex index in the points array
        - UVMap (float2, optional) : UV Map coordinat
    """

    @classmethod
    def New(cls, points):
        corner = cls(domain_name='CORNER')

        corner.points = points
        corner.attributes.new_int('vertex_index', transfer=False)

        return corner

    def init_domain(self):
        super().init_domain()

        self.add_auto_attribute('UVMap', 'FLOAT2', (0, 0), transfer=True)

    def init_selection(self, selection):
        super().init_selection(selection)
        selection.points = self.points

    def check(self, halt=True):
        if np.max(self.vertex_index) > self.points.size:
            if halt:
                raise RuntimeError(f"CornerDomain check fail: {np.max(self.vertex_index)=}, {self.points.size=}")
            else:
                return False
        return True

    @classmethod
    def FromDict(cls, points, d):
        domain = cls.New(points)
        domain._attributes = Attributes.FromDict(d)

        return domain

    # =============================================================================================================================
    # Add corners

    def add_corners(self, corners, **attributes):
        """ Add corners.

        Arguments
        ---------
            - corners (array of ints) : valid indices on the array of points
            - attributes (attribute names, attribute values) : value of the corner attributes
        """

        if corners is None or np.size(corners) == 0:
            return

        if len(np.shape(corners)) > 1:
            corners = np.reshape(corners, np.size(corners))

        self.add(len(corners), vertex_index=corners, **attributes)

    # =============================================================================================================================
    # Properties

    @property
    def position(self):
        return self.points.position[self.vertex_index]

    @position.setter
    def position(self, value):
        self.points.position[self.vertex_index] = value

    # =============================================================================================================================
    # Methods

    def new_uvmap(self, name, value=None):
        self.attributes.new_vector2(name, value)


# ====================================================================================================
# Face Domain

# ----------------------------------------------------------------------------------------------------
# Common to Face and Spline domains

class FaceSplineDomain(Domain):

    def __init__(self, domain_name=None, owner=None, selector=None):
        super().__init__(domain_name=domain_name, owner=owner, selector=selector)

        self.attributes.new_int('loop_start', transfer=False)
        self.attributes.new_int('loop_total', transfer=False)

    def init_domain(self):
        super().init_domain()
        self.add_auto_attribute('material_index', 'INT', 0, transfer=True)

    # ----------------------------------------------------------------------------------------------------
    # Loop start management

    @property
    def loop_start_offset(self):
        """ Return the value of the loop_start offset for adding new items

        Returns
        -------
            - int : sum of the last loop_start and the last loop_total
        """

        self.no_selection("loop_start_offset")
        if len(self):
            return self.loop_start[-1] + self.loop_total[-1]
        else:
            return 0

    def loop_start_new(self, loop_total):
        """ Compute the loop_start value of new iems.

        Arguments
        ---------
            - loop_total (array of ints) : the sizes of the items to add

        Returns
            - array of ints : one loop_start value per loop_total starting from loop_start_offset
        """

        if len(loop_total):
            a = np.roll(np.cumsum(loop_total), 1)
            a[0] = 0
            return a + self.loop_start_offset
        else:
            return np.zeros(0, int)

    def true_loop_start(self):
        """ Compute the target loop_start to be compared with the stored one.

        Can be used to recompute the proper loop start after a reorganization

        Returns
        -------
            - array of ints : the loop_start of each item
        """

        self.no_selection("true_loop_start")

        if len(self):
            a = np.roll(np.cumsum(self.loop_total), 1)
            a[0] = 0
            return a
        else:
            return np.zeros(0, int)

    def update_loop_start(self):
        self.loop_start = self.true_loop_start()

    def add(self, count, **attrs):
        super().add(count, **attrs)

        self.update_loop_start()

    def delete(self, selection):
        super().delete(selection)

        self.update_loop_start()

    def check(self, halt=True):

        if np.any(self.loop_start - self.true_loop_start() != 0):
            if halt:
                print("Expected loop start")
                print(self.true_loop_start())
                print()
                print("Loop start")
                print(self.loop_start)
                print()
                raise Exception(f"Loop start is not consistent")
            return False

        return True

    # ====================================================================================================
    # Sort the item per size

    def sized_items(self):

        if len(self) == 0:
            return {}

        starts  = self.loop_start
        totals  = self.loop_total

        if np.shape(starts) == ():
            return {totals: {'index': [0], 'loop_index': np.reshape(np.arange(starts, starts + totals), (1, totals))}}

        sizes   = np.unique(totals)
        indices = np.arange(self.size)
        items   = {}

        #print(f"SIZED_ITEMS: {starts=}, {totals=}, {sizes=}, {indices=}")

        for size in sizes:
            inds = indices[totals == size]
            items[size] = {'index': inds, 'loop_index': starts[inds, None] + [[i for i in range(size)]]}

        return items

    # ====================================================================================================
    # Reversed indices

    @property
    def reversed_indices(self):

        total = np.sum(self.loop_total)
        rev = np.empty(total, int)

        for size, dct in self.sized_items().items():
            rev[dct['loop_index']] = dct['index'][:, None]

        return rev


# ----------------------------------------------------------------------------------------------------
# Face domain

class FaceDomain(FaceSplineDomain):
    """ Face domain.

    The Face domain is specific to Mesh geometry.
    A face is a loop of size loop_total of corner indices.

    It keeps a pointer to the Mesh CORNER domain.

    Attributes
    ----------
        - loop_start (int) : first index in corners array
        - loop_total (int) : number of corners
        - material_index (int, optional) : material index
    """

    @classmethod
    def New(cls, corners):
        face = cls(domain_name='FACE')
        face.corners = corners
        return face

    def init_selection(self, selection):
        super().init_selection(selection)
        selection.corners = self.corners

    def check(self, halt=True):

        if np.sum(self.loop_total) > self.corners.size:
            if halt:
                raise RuntimeError(f"FaceDomain check fail: {np.sum(self.loop_total)=}, {self.corners.size=}")
            else:
                return False

        return super().check(halt)

    @classmethod
    def FromDict(cls, corners, d):
        domain = cls.New(corners)
        domain._attributes = Attributes.FromDict(d)

        return domain

    # ====================================================================================================
    # Adding faces

    def add_faces(self, faces, **attributes):
        """ Add faces.

        Arguments
        ---------
            - faces (array of ints) : the sizes of the faces
            - attributes (attribute names, attribute values) : value of the corner attributes
        """

        if faces is None or np.size(faces) == 0:
            return

        faces = np.reshape(faces, np.size(faces))
        self.add(len(faces), loop_start=self.loop_start_new(faces), loop_total=faces, **attributes)


        # Waiting for code stabilization



        self.check()

    # ====================================================================================================
    # Delete faces

    def delete(self, selection):
        """ Delete faces.

        Arguments
        ---------
            - selection : faces to delete
        """

        self.no_selection("delete faces")

        self.corners.delete(self[selection].get_corner_indices())

        super().delete(selection)

        self.update_loop_start()



    # ====================================================================================================
    # Surfaces and normals

    # ---------------------------------------------------------------------------
    # Surface is computed by cross products of triangle. This also gives
    # the normal to the face. The vector normal the length of which is the surface
    # is called the "surface vector".

    @staticmethod
    def area_vect(vs, size, return_vector=True):
        if size == 3:
            sv = np.cross(
                    vs[..., 1, :] - vs[..., 0, :],
                    vs[..., 2, :] - vs[..., 0, :])

        elif size == 4:
            sv = (np.cross(
                        vs[..., 1, :] - vs[..., 0, :],
                        vs[..., 3, :] - vs[..., 0, :]
                    ) +
                    np.cross(
                        vs[..., 3, :] - vs[..., 2, :],
                        vs[..., 1, :] - vs[..., 2, :]
                    ))

        else:
            sv = np.zeros((len(vs), 3), float)
            for i in range(size-2):
                sv += FaceDomain.surf_vect(vs[..., [0, i+1, i+2], :], 3)

        if return_vector == 'AREA':
            return np.linalg.norm(sv, axis=-1)/2

        elif return_vector == 'NORMAL':
            return sv / np.linalg.norm(sv, axis=-1)[:, None]

        else:
            return sv

    def area_vectors(self):
        """ Compute the surfaces vectors

        The surfaces are computed by cross products of triangles.
        This also gives the normal to the face.
        The normal vector normal the length of which is the surface
        is called the *surface vector*.

        Arguments
        ---------
            - faces (int or array of ints = None) : the faces

        Returns
        -------
            - array of vectors of floats: The surfaces normals
        """

        # ---------------------------------------------------------------------------
        # Compute the surface for faces of the same size

        def surf_vect(vs, size):

            if size == 3:
                return np.cross(
                        vs[...,1,:] - vs[..., 0,:],
                        vs[...,2,:] - vs[..., 0,:])

            elif size == 4:
                return (np.cross(
                            vs[...,1,:] - vs[..., 0, :],
                            vs[...,3,:] - vs[..., 0, :]
                        ) +
                        np.cross(
                            vs[...,3,:] - vs[..., 2, :],
                            vs[...,1,:] - vs[..., 2, :]
                        ))

            else:
                sv = np.zeros((len(vs), 3), float)
                for i in range(size-2):
                    sv += surf_vect(vs[..., [0, i+1, i+2], :], 3)
                return sv

        # ---------------------------------------------------------------------------
        # The surfaces

        area_vectors = np.zeros((self.size, 3), float)
        for size, fcs in self.sized_items().items():

            f_ind = fcs['index']
            c_ind = fcs['loop_index']

            verts = self.corners.position[c_ind]

            area_vectors[f_ind] = surf_vect(verts, size)

        return area_vectors

    # ---------------------------------------------------------------------------
    # Surfaces : norm of the perpendicular vectors

    @property
    def area(self):
        """ Faces areas

        Args:
            verts (array (:, 3) of floats): The vertices

        Returns:
            array (len(self)) of floats: The surfaces
        """

        return np.linalg.norm(self.area_vectors(), axis=-1)/2

    # ---------------------------------------------------------------------------
    # Normals : normalized surface vectors

    @property
    def normal(self):
        """ Compute the normals

        Args:
            verts (array (:, 3) of floats): The vertices

        Returns:
            array (len(self), 3) of floats: The normals
        """

        sv = self.area_vectors()
        return sv / np.linalg.norm(sv, axis=-1)[:, None]

    # ---------------------------------------------------------------------------
    # Centers of the faces

    @property
    def position(self):
        """ Centers of the faces

        Args:
            verts (array (:, 3) of floats): The vertices

        Returns:
            array (len(self), 3) of floats: The centers
        """

        centers = np.zeros((self.size, 3), float)
        for size, fcs in self.sized_items().items():

            f_ind = fcs['index']
            c_ind = fcs['loop_index']

            verts = self.corners.position[c_ind]

            centers[f_ind] = np.average(verts, axis=1)

        return centers

    @position.setter
    def position(self, value):

        sized_faces = self.sized_items()

        centers = np.zeros((self.size, 3), float)
        for size, fcs in sized_faces.items():

            f_ind = fcs['index']
            c_ind = fcs['loop_index']

            verts = self.corners.position[c_ind]

            centers[f_ind] = np.average(verts, axis=1)

        diffs = value - centers

        for size, fcs in sized_faces.items():

            c_ind = fcs['loop_index']

            verts = self.corners.position[c_ind]
            verts += diffs[:, None, :]

            self.corners[np.reshape(c_ind, np.size(c_ind))].position = np.reshape(verts, (np.size(verts)//3, 3))

    # ====================================================================================================
    # Get surface as a dict

    # ----------------------------------------------------------------------------------------------------
    # The indices of the corners

    def get_corner_indices(self):
        if self.is_selection:
            inds = np.empty(0, int)
            for size, items in self.sized_items().items():
                inds = np.append(inds, items['loop_index'].flatten())

            return inds
        else:
            return np.arange(self.corners.size)

    def get_point_indices(self):

        return self.corners.vertex_index[self.get_corner_indices()]

        if self.is_selection:
            if len(self) == 1:
                return self.corners[self.loop_start:self.loop_start + self.loop_total].vertex_index

            else:
                corners = np.empty(np.sum(self.loop_total), int)
                vertex_index = self.corners.vertex_index
                offset = 0
                for loop_start, loop_total in zip(self.loop_start, self.loop_total):
                    corners[offset:offset+loop_total] = vertex_index[loop_start:loop_start + loop_total]
                    offset += loop_total

                return corners

        else:
            return self.corners.vertex_index

    def get_verts(self):
        return self.corners.points.position[self.get_point_indices()]

    # ====================================================================================================
    # Get surface as a dict

    def get_surface(self):

        svs = self.area_vectors()
        assert(len(svs) == len(self))

        areas2 = np.linalg.norm(svs, axis=-1)

        surf  = {'normals': svs/areas2[:, None], 'areas': areas2/2}
        surf['sizes'] = self.loop_total
        surf['verts'] = self.get_point_indices()

        return surf

    # ====================================================================================================
    # As a list of sequences

    def sequences(self):
        inds = list(self.corners.vertex_index)
        return [inds[lstart:lstart+ltotal] for (lstart, ltotal) in zip(self.loop_start, self.loop_total)]


# ====================================================================================================
# Edge Domain

class EdgeDomain(Domain):
    """ Edge domain.

    Attributes
    ----------
        - vertex0 (int) : index of the first vertex
        - vertex1 (int) : index of the second vertex
    """

    @classmethod
    def New(cls, points):
        edge = cls(domain_name='EDGE')

        edge.points = points
        edge.attributes.new_int('vertex0', transfer=False)
        edge.attributes.new_int('vertex1', transfer=False)

        return edge

    def init_selection(self, selection):
        super().init_selection(selection)
        selection.points = self.points

    def check(self, halt=True):
        if (np.max(self.vertex0) > self.points.size) or (np.max(self.vertex1) > self.points.size):
            if halt:
                raise RuntimeError(f"EdgeDomain check fail: {np.max(self.vertex0)=}, {np.max(self.vertex1)=}, {self.points.size=}")
            else:
                return False
        return True

    @classmethod
    def FromDict(cls, points, d):
        domain = cls.New(points)
        domain._attributes = Attributes.FromDict(d)

        return domain

# ====================================================================================================
# Control Point Domain

class ControlPointDomain(Domain):
    """ Curve Control Point Domain.

    The control points of curve splines.

    Attributes
    ----------
        - position (vector) : control point position
        - handle_left (vector, optional) : bezier splines left handles
        - handle_right (vector, optional) : bezier splines right handles
        - handle_type_left (int, optional) : bezier splines left handle types
        - handle_type_right (int, optional) : bezier splines right handle types
        - radius (float, optional) : point radius
        - tilt (float, optional) : point tilt
    """

    @classmethod
    def New(cls):
        point = cls(domain_name='POINT')

        # ----- Position + w make vector4 :

        point.attributes.new_vector('position', transfer=False)
        point.attributes.new_float('w', default=1., transfer=False)

        return point

    def init_domain(self):

        super().init_domain()

        self.add_auto_attribute('handle_left',       'FLOAT_VECTOR', (0, 0, 0), transfer=True)
        self.add_auto_attribute('handle_right',      'FLOAT_VECTOR', (0, 0, 0), transfer=True)
        self.add_auto_attribute('handle_type_left',  'INT',           0,        transfer=True)
        self.add_auto_attribute('handle_type_right', 'INT',           0,        transfer=True)
        self.add_auto_attribute('tilt',              'FLOAT',         0,        transfer=True)
        self.add_auto_attribute('radius',            'FLOAT',         1,        transfer=True)

    @classmethod
    def FromDict(cls, d):
        domain = cls.New()
        domain._attributes = Attributes.FromDict(d)

        return domain


    # ====================================================================================================
    # Properties

    @property
    def points4(self):
        points = self.position
        n = len(points)
        if n == 0:
            return np.zeros((0, 4), float)

        else:
            points4 = np.empty((n, 4), float)
            points4[:, :3] = points
            del points
            points4[:, 3] = self.w
            return points4

        #return self.attributes.over_get('position', 4, selection=self._selector)

    @points4.setter
    def points4(self, value):
        if not isinstance(value, np.ndarray):
            value = np.array(value)

        if np.shape(value)[-1] == 3:
            self.position = value
            self.w        = 1
        else:
            self.position = value[:, :3]
            self.w        = value[:, 3]

        return


        if np.shape(value)[-1] == 3:
            a = np.ones(np.shape(value)[:-1] + (4,))
            a[..., :3] = value
        else:
            a = value
        self.attributes.over_set('position', 4, a, selection=self._selector)


# ====================================================================================================
# Spline Domain

class SplineDomain(FaceSplineDomain):
    """ Spline domain.

    Spline domain is specific to Curve geometry. A spline is an array of control points.
    A Spline is similare to a Face but points directly to the control points and not indirectly
    as for the faces.

    Attributes
    ----------
        - loop_start (int) : first index in control points array
        - loop_total (int) : number of control points
        - material_index (int, optional) : material index
        - resolution (int, optional) : spline resolution
        - cyclic (bool, optional) : spline is cyclic or not
        - order (int, optional) : Nurbs spline order
        - bezierpoint (bool, optional) : Nurbs spline bezierpoint flag
        - endpoint (bool, optional) : Nurbs spline endpoint flag
    """

    @classmethod
    def New(cls, points):

        spline = cls(domain_name='SPLINE')

        spline.points = points
        spline.attributes.new_int('curve_type')

        return spline

    def init_domain(self):

        super().init_domain()

        self.add_auto_attribute('resolution', 'INT',     16,    transfer=True)
        self.add_auto_attribute('cyclic',     'BOOLEAN', False, transfer=True)

        # Nurbs
        self.add_auto_attribute('order',      'INT',      4,    transfer=True)
        self.add_auto_attribute('bezierpoint','BOOLEAN', False, transfer=True)
        self.add_auto_attribute('endpoint',   'BOOLEAN', False, transfer=True)

    def init_selection(self, selection):
        super().init_selection(selection)
        selection.points = self.points

    @classmethod
    def FromDict(cls, points, d):
        domain = cls.New(points)
        domain._attributes = Attributes.FromDict(d)

        return domain

    def check(self, halt=True):
        if np.sum(self.loop_total) != self.points.size:
            if halt:
                raise RuntimeError(f"SplineDomain check fail: {np.sum(self.loop_total)=} != {self.points.size=}")
            else:
                return False

        return super().check(halt=halt)

    @property
    def has_bezier(self):
        return np.sum(self.curve_type == blender.BEZIER) > 0

    # ----------------------------------------------------------------------------------------------------
    # Points indices

    def get_point_indices(self):
        if self.is_selection:
            if len(self) == 1:
                return np.arange(self.loop_start, self.loop_start + self.loop_total)

            else:
                indices = np.empty(np.sum(self.loop_total), int)
                offset = 0
                for loop_start, loop_total in zip(self.loop_start, self.loop_total):
                    indices[offset:offset+loop_total] = range(loop_start, loop_start + loop_total)
                    offset += loop_total

                return indices

        else:
            return np.arange(self.points.size)

    def get_points(self):
        return self.points[self.get_point_indices()]

    def get_verts(self):
        return self.points.position[self.get_point_indices()]

    def get_lefts(self):
        return self.points.handle_left[self.get_point_indices()]

    def get_rights(self):
        return self.points.handle_right[self.get_point_indices()]


    def sample_attribute(self, value):
        npoints = len(self.bspline.c)
        count = npoints*self.resolution if self.cyclic else (npoints - 1)*self.resolution + 1


    # ====================================================================================================
    # Adding splines

    def add_splines(self, splines, **attributes):
        """ Add splines.

        Arguments
        ---------
            - splines (array of ints) : the number of control points per spline
            - attributes (attribute names, attribute values) : value of the corner attributes
        """


        if splines is None or np.size(splines) == 0:
            return

        splines = np.reshape(splines, np.size(splines))
        self.add(len(splines), loop_start=self.loop_start_new(splines), loop_total=splines, **attributes)

    # ====================================================================================================
    # Delete faces

    def delete(self, selection):
        """ Delete splines.

        Arguments
        ---------
            - selection : splines to delete
        """

        self.no_selection("delete splines")

        self.points.delete(self[selection].get_point_indices())

        super().delete(selection)

        self.update_loop_start()

    # ====================================================================================================
    # Properties

    @property
    def position(self):
        if self.size == 0:
            return []

        centers = np.empty(self.size + (3,))
        for size, splines in self.sized_items().items():
            centers[splines['index']] = np.average(self.points.position[splines['loop_index']], axis=-1)

        return centers

    @position.setter
    def position(self, value):

        if self.size == 0:
            return

        sized_splines = self.sized_items()

        centers = np.zeros((self.size, 3), float)
        for size, fcs in sized_splines.items():
            centers[splines['index']] = np.average(self.points.position[splines['loop_index']], axis=-1)

        diffs = value - centers

        for size, fcs in sized_splines.items():

            pinds = fcs['loop_index']

            verts = self.points.position[pinds]
            verts += diffs[:, None, :]

            self.points[np.reshape(pinds, np.size(pinds))].position = np.reshape(verts, (np.size(verts)//3, 3))


        #for size, splines in self.sized_splines().items():
        #    positions = self.points.position[splines['point_index']]
        #    self.points.position[splines['point_index']] = position + (value - np.average(positions, axis=-1))

    # ====================================================================================================
    # Parameter

    @property
    def functions(self):
        """ Return the functions representing the splines.

        The functions are scipy BSplines initialized with the splines parameters.

        Returns
        -------
            - list of BSpline functions
        """

        funcs = splinesmaths.BSplines()

        for i, (curve_type, loop_start, loop_total, cyclic, resolution) in enumerate(zip(self.curve_type, self.loop_start, self.loop_total, self.cyclic, self.resolution)):

            if curve_type == blender.BEZIER:
                funcs.append(splinesmaths.Bezier(self.points.position[loop_start:loop_start + loop_total], cyclic=cyclic, resolution=resolution,
                                lefts  = self.points.handle_left[loop_start:loop_start + loop_total],
                                rights = self.points.handle_right[loop_start:loop_start + loop_total]
                                ))

            elif curve_type == blender.POLY:
                funcs.append(splinesmaths.Poly(self.points.position[loop_start:loop_start + loop_total], cyclic=cyclic))

            elif curve_type == blender.NURBS:
                funcs.append(splinesmaths.Nurbs(self.points.position[loop_start:loop_start + loop_total], cyclic=cyclic, resolution=resolution,
                                    w     = self.w[loop_start:loop_start + loop_total],
                                    order = self.order[loop_start:loop_start + loop_total],
                                    ))

            else:
                assert(False)

        return funcs

    @property
    def length(self):
        """ Length of the splines.

        Returns
        -------
            - List of spline lengths
        """

        return self.functions.length

    def tangent(self, t):
        """ Tangents of the splines at a given time.

        Arguments
        ---------
            - t (float) : spline parameter between 0 and 1

        Returns
        -------
            - list of spline tangents evaluated at time t.
        """
        return self.functions.tangent(t)

# ====================================================================================================
# Instance Domain

class InstanceDomain(PointDomain):
    """ Instance Domain.

    Instance domain directly inherits from Point domain.
    In addition to position attribute, it managed two more transformations : Scale and Rotation to
    be applied to the instances.

    Instances are randomly chosen in a list of models. The index is stored in the model_index attribute.

    The instances capture attributes from other domains.

    Note that Instances Geometry inherits from Instance domain, contrary to the other geometries which
    store domains as attributes:

    ``` python
    class Mesh(Geometry):
        def __init__(self, ...):
            self.points  = PointDomain.New(...)
            self.corners = CornerDomain.New(...)
            self.faces   = FaceDomain.New(...)

    class Instances(InstanceDomain, Geometry):
        def __init__(self, ...):
            super().__init__(...) # Instances domain initialization

    v = Mesh().position        # Invalid : raises an error
    v = Mesh().points.position # Valid
    v = Instances().position   # Valid
    '''

    Attributes
    ----------
        - position (vector) : instance position
        - model_index (int) : index in the list of models
        - Scale (vector, optional) : instance scale
        - Rotation (vector, optional) : instance rotation

    Arguments
    ---------
        - domain_name (str = None) : 'INSTANCE' or None
        - owner (Instance domain = None) : the selection owner if not None
        - selector (selection = None) : selection if initialized as domain selection
        - points (array of vectors = None) : a point domain
        - models (model spec of list of model specs) : the model to pick into
        - indices (array of ints = None) : model_index initialization
        - seed (int = None) : random seed if indices is None
    """

    def __init__(self, domain_name=None, owner=None, selector=None, points=None, models=None, indices=None, seed=0):

        from geopy.core.geometry import Geometry

        super().__init__(domain_name=domain_name, owner=owner, selector=selector)

        if domain_name is None:
            return

        self.new_vector_attribute('position',    transfer=True)
        self.new_int_attribute(   'model_index', default=0, transfer=False)

        if points is not None:
            self.add_from_domain(points)

        # ----- The list of models

        if isinstance(models, list):
            self.models = [Geometry.LoadModel(model) for model in models]

        elif isinstance(models, bpy.types.Collection):
            self.models = [Geometry.LoadModel(model) for model in models.objects]

        elif models is None:
            self.models = []

        else:
            self.models = [Geometry.LoadModel(models)]

        # ----- Model index

        if len(self.models) <= 1:
            self.model_index = 0

        elif indices is None:
            rng = np.random.default_rng(seed)
            self.model_index = rng.integers(0, len(self.models), len(self))

        else:
            if len(indices) != len(self):
                raise Exception(f"Instances init error: the len of indices {len(indices)} is different from the number of points {len(points)}")

    def init_domain(self):
        super().init_domain()

        self.add_auto_attribute('Rotation', 'FLOAT_VECTOR', (0, 0, 0), transfer=True)
        self.add_auto_attribute('Scale',    'FLOAT_VECTOR', (1, 1, 1), transfer=True)

    def init_selection(self, selection):
        super().init_selection(selection)

        selection.models  = self.models

    # ====================================================================================================
    # Add / delete instances

    def add_from_domain(self, domain):
        """ Add instances from another domain
        """

        n = len(self)

        self.attributes.copy_definitions(domain.attributes)
        self.add(len(domain), **{name: getattr(domain, name) for name in domain.attributes.names})

        if isinstance(domain, InstanceDomain):
            nmodels = len(self.models)

            self.models.extend(domain.models)
            self.model_index[n:] += nmodels
