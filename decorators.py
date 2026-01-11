# https://docs.python.org/3/glossary.html#term-decorator

import inspect

from plugin_discovery import discovered_plugins

def func_decorator(orig_name, orig_func):
    def decorator(*args, **kwargs):
        print(f"-> Decorator wrapper called on {orig_name} method {orig_func.__name__}")
        for plugin_name, plugin_module in discovered_plugins.items():
            plugin_class = getattr(plugin_module, orig_name, None)
            if plugin_class is None:
                continue
            plugin_method = getattr(plugin_class(args[0]), orig_func.__name__, None)
            if plugin_method is None:
                continue
            print(f"---> Calling plugin {plugin_name} method {plugin_method.__name__}")
            if orig_func.__name__ == "__init__":
                plugin_method(args[0])
            else:
                result = plugin_method(*args, **kwargs)
        if not 'result' in locals():
            print(f"---> Calling original method {orig_func.__name__}")
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
