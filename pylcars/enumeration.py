# -*- coding: utf-8 -*-
print "sfdsdf"
class Enumeration(set):
    
    def __getattr__(self, name):
        if name in self:
            return name
        raise AttributeError
    def __setattr__(self, name, value):
        raise RuntimeError("Cannot override values")
    def __delattr__(self, name):
        raise RuntimeError("Cannot delete values")
    class __metaclass__(type):
        def __iter__(self):
            for item in self.__dict__:
                if item == self.__dict__[item]:
                    yield item    
