# /usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABCMeta
from numbers import Real
import functools


#Decorator class for setter methods independent of @property. Setter methods
#should use self.__dict__['variable'] = value rather than variable = value
#to avoid recursion
class setter():

    def __init__(self, func):
        self.func = func

    def __set__(self, obj, value):
        return self.func(obj, value)


class Identifier():

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return repr(self.name)


class WithBoundedAttr(metaclass = ABCMeta):

    def __setattr__(self, name, value):
        if hasattr(self, 'bounds'):
            if name in self.bounds and isinstance(value, Real):
                mini, maxi = (eval(x) if isinstance(x, str) else x
                              for x in self.bounds[name])
                if all([isinstance(m, Real) for m in (mini, maxi)]):
                    value = min(maxi, max(mini, value))
        self.__dict__[name] = value

    def bound(self, name, mini, maxi):
        if not hasattr(self, 'bounds'):
            self.bounds = {}
        self.bounds[name] = mini, maxi
        if hasattr(self, name):
            setattr(self, name, getattr(self, name))


# A property that caches the result to avoid querying the api more than needed.
def lazy_property(func):
    return property(functools.lru_cache()(func))