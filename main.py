#!/usr/bin/env python3
"""
Main module for the application.
"""

import sys
import importlib
import pkgutil

import plugins

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
    return 0


if __name__ == "__main__":
    sys.exit(main())
