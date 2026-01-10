# https://docs.python.org/3/glossary.html#term-decorator

import inspect

def func_decorator(orig_func):
    def decorator(*args, **kwargs):
         print("Decorating wrapper called for method %s" % orig_func.__name__)
         result = orig_func(*args, **kwargs)
         return result
    return decorator

def pluggable(cls):
    for name, method in inspect.getmembers(cls):
        if (not inspect.ismethod(method) and not inspect.isfunction(method)) or inspect.isbuiltin(method):
            continue
        print("Decorating function %s" % name)
        setattr(cls, name, func_decorator(method))
    print("- Class %s has been decorated" % cls.__name__)
    return cls
