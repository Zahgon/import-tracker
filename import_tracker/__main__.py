"""
This main entrypoint allows import_tracker to run as an independent script to
track the imports for a given module.

Example Usage:

# Track a single module
python -m import_tracker --name my_library

# Track a module and all of the sub-modules it contains
python -m import_tracker --name my_library --recursive --num_jobs 2

# Track a module with relative import syntax
python -m import_tracker --name .my_sub_module --package my_library
"""

# Standard
import argparse
import json
import logging
import os

# Local
from .import_tracker import track_module

## Main ########################################################################


def main():
    """Main entrypoint as a function"""
    pass


if __name__ == "__main__":  # pragma: no cover
    main()
