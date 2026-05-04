"""Tests for core/classdeco.py."""
import pytest
from core.classdeco import class_property, ClassPropertyDescriptor, ClassPropertyMetaClass


# ---------------------------------------------------------------------------
# class_property (getter seul)

class TestClassProperty:

    def test_returns_descriptor(self):
        @class_property
        def prop(cls):
            return 42
        assert isinstance(prop, ClassPropertyDescriptor)

    def test_getter_accessible_from_class(self):
        class A:
            @class_property
            def value(cls):
                return 99
        assert A.value == 99

    def test_getter_accessible_from_instance(self):
        class A:
            @class_property
            def value(cls):
                return 99
        assert A().value == 99

    def test_getter_receives_class(self):
        class A:
            @class_property
            def name(cls):
                return cls.__name__
        assert A.name == "A"

    def test_no_setter_raises_on_set(self):
        class A:
            @class_property
            def value(cls):
                return 1
        with pytest.raises(AttributeError, match="can't set attribute"):
            A().value = 2


# ---------------------------------------------------------------------------
# setter

class TestClassPropertySetter:

    def test_setter_via_decorator(self):
        class A:
            _x = 0

            @class_property
            def x(cls):
                return cls._x

            @x.setter
            def x(cls, value):
                cls._x = value

        A.x = 10
        assert A.x == 10

    def test_setter_wraps_plain_function_in_classmethod(self):
        def plain(cls, v):
            pass
        descriptor = ClassPropertyDescriptor(classmethod(plain))
        descriptor.setter(plain)
        assert descriptor.fset is not None


# ---------------------------------------------------------------------------
# ClassPropertyMetaClass

class TestClassPropertyMetaClass:

    def test_setattr_triggers_descriptor(self):
        class A(metaclass=ClassPropertyMetaClass):
            _v = 0

            @class_property
            def v(cls):
                return cls._v

            @v.setter
            def v(cls, value):
                cls._v = value

        A.v = 55
        assert A.v == 55

    def test_regular_attr_unaffected(self):
        class A(metaclass=ClassPropertyMetaClass):
            x = 1

        A.x = 2
        assert A.x == 2
