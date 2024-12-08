# -*- coding: utf-8 -*-

"""Main module"""

import inspect
import typing

Self = typing.TypeVar("Self", bound="ClassPropertyDescriptor")

SetterReturnType = typing.TypeVar("SetterReturnType")  # Declare type
GetterReturnType = typing.TypeVar("GetterReturnType")  # Declare type variable
OwningClassType = typing.TypeVar(
    "OwningClassType", bound="object"
)  # Declare type variable


# AnyFuncType = typing.Union[classmethod, staticmethod, typing.Callable[[typing.Any], typing.Any]]
AnyFuncType = typing.Callable[[OwningClassType], GetterReturnType]


class ClassPropertyDescriptor(object):
    def __init__(
        self: Self,
        fget: typing.Union[classmethod, staticmethod],
        fset: typing.Optional[typing.Union[classmethod, staticmethod]] = None,
    ) -> None:
        self.fget = fget
        self.fset = fset

    def __get__(
        self: Self,
        obj: OwningClassType,
        klass: typing.Optional[typing.Type[OwningClassType]] = None,
    ) -> GetterReturnType:
        if klass is None:
            klass = type(obj)
        return self.fget.__get__(obj, klass)()

    def __set__(self: Self, obj: typing.Any, value: typing.Any) -> None:
        if not self.fset:
            raise AttributeError("can't set attribute")
        if inspect.isclass(obj):
            type_ = obj
            obj = None
        else:
            type_ = type(obj)
        return self.fset.__get__(obj, type_)(value)

    def setter(
        self: Self, func: typing.Callable[[OwningClassType, GetterReturnType], None]
    ) -> Self:
        if isinstance(func, (classmethod, staticmethod)):
            cm = func
        else:
            cm = classmethod(func)
        self.fset = cm
        return self


def class_property(
    func: typing.Callable[[OwningClassType], GetterReturnType]
) -> ClassPropertyDescriptor:
    if isinstance(func, (classmethod, staticmethod)):
        cm = func
    else:
        cm = classmethod(func)

    return ClassPropertyDescriptor(cm)


class ClassPropertyMetaClass(type):
    def __setattr__(self, key: typing.Any, value: typing.Any) -> typing.Any:
        if key in self.__dict__:
            obj = self.__dict__.get(key)
            if obj and type(obj) is ClassPropertyDescriptor:
                return obj.__set__(self, value)

        return super(ClassPropertyMetaClass, self).__setattr__(key, value)
    
    
class Foo:
    @class_property
    def bar(cls):
        return 123
    
    
print(Foo.bar)