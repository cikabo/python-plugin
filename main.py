#!/usr/bin/env python3
"""
Main module for the application.
"""

import sys
from users import User
from plugin_discovery import discovered_plugins

def main():
    """
    Main entry point of the application.
    """

    print("Discovered plugins:", list(discovered_plugins.keys()))

    User_instance = User("john_doe", "john_doe@example.com")
    print(User_instance.get_info())
    return 0


if __name__ == "__main__":
    sys.exit(main())
