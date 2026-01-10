# https://docs.python.org/3/glossary.html#term-decorator

import inspect

from plugin_discovery import discovered_plugins

def func_decorator(orig_name, orig_func):
    def decorator(*args, **kwargs):
         print(f"--> Decorating wrapper called on {orig_name} method {orig_func.__name__}")
         result = orig_func(*args, **kwargs)
         return result
    return decorator

def pluggable(cls):
    for name, method in inspect.getmembers(cls):
        if (not inspect.ismethod(method) and not inspect.isfunction(method)) or inspect.isbuiltin(method):
            continue
        print("Decorating function %s" % name)
        setattr(cls, name, func_decorator(cls.__name__, method))
    print("- Class %s has been decorated" % cls.__name__)
    return cls
