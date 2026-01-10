#!/usr/bin/env python3
"""
Main module for the application.
"""

# https://packaging.python.org/en/latest/guides/creating-and-discovering-plugins/

import sys
import importlib
import pkgutil

import plugins
from users import User


def iter_namespace(ns_pkg):
    # Specifying the second argument (prefix) to iter_modules makes the
    # returned name an absolute name instead of a relative one. This allows
    # import_module to work without having to do additional modification to
    # the name.
    return pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + ".")

discovered_plugins = {
    name: importlib.import_module(name)
    for finder, name, ispkg
    in iter_namespace(plugins)
}

def main():
    """
    Main entry point of the application.
    """
    print("Hello, World!")
    print("Discovered plugins:", list(discovered_plugins.keys()))

    User_instance = User("john_doe", "john_doe@example.com")
    print(User_instance.get_info())
    return 0


if __name__ == "__main__":
    sys.exit(main())
