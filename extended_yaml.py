# /usr/bin/env python
# -*- coding: utf-8 -*-

from yaml import *
from abc import ABCMeta, ABC

class AbstractYAMLMeta(ABCMeta, YAMLObjectMetaclass):
    pass

class AbstractYAMLObject(ABC, YAMLObject, metaclass=AbstractYAMLMeta):
    pass