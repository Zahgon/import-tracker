"""
This module holds tools for libraries to use when definint requirements and
extras_require sets in a setup.py
"""

# Standard
from functools import reduce
from typing import Dict, Iterable, List, Optional, Tuple, Union
import os
import re
import sys

# Local
from .constants import INFO_OPTIONAL
from .import_tracker import track_module
from .log import log

## Public ######################################################################


def parse_requirements(
    requirements: Union[List[str], str],
    library_name: str,
    extras_modules: Optional[List[str]] = None,
    full_depth: bool = True,
    keep_optional: Union[bool, Dict[str, List[str]]] = False,
    **kwargs,
) -> Tuple[List[str], Dict[str, List[str]]]:
    """This helper uses the lists of required modules and parameters for the
    given library to produce requirements and the extras_require dict.

    Args:
        requirements:  Union[List[str], str]
            The list of requirements entries, or a file path pointing to a
            requirements file
        library_name:  str
            The top-level name of the library package
        extras_modules:  Optional[List[str]]
            List of module names that should be used to generate extras_require
            sets
        full_depth:  bool
            Passthrough to track_module. The default here is switched to True so
            that modules which are both direct and transitive dependencies of
            the library are correctly allocated.
        keep_optional:  Union[bool, Dict[str, List[str]]]
            Indicate which optional dependencies should be kept when computing
            the extras sets. If True, all optional dependencies will be kept. If
            False, none will be kept. Otherwise, the argument should be a dict
            mapping known optional dependencies of specific modules that should
            be kept and all optional dependencies not represented in the dict
            will be dropped.
        **kwargs:
            Additional keyword arguments to pass through to track_module

    Returns:
        requirements:  List[str]
            The list of requirements to pass to setup()
        extras_require:  Dict[str, List[str]]
            The extras_require dict to pass to setup()
    """
    pass


## Implementation Details ######################################################

# Regex for parsing requirements
_REQ_SPLIT_EXPR = re.compile(r"[=><!~\[]")

# Exprs for finding module names
_PKG_VERSION_EXPR = re.compile("-[0-9]")
_PKG_NAME_EXPR = re.compile("^Name: ([^ \t\n]+)")

# Extras require group name for the union of all dependencies
_ALL_GROUP = "all"

# Lazily created global mapping from module name to package name
_MODULE_TO_PKG = None


def _map_requirements(declared_dependencies, dependency_set):
    """Given the declared dependencies from requirements.txt and the given
    programmatic dependency set, return the subset of declared dependencies that
    matches the dependency set
    """
    pass


def _map_modules_to_package_names():
    """Look for any information we can get to map from the name of the imported
    module to the name of the package that installed that module.

    WARNING: This is a best-effort function! It attempts to look for common
        conventions from pip, but it's very possible to break this function by
        non-standard installation topology.
    """
    pass


def _standardize_package_name(raw_package_name):
    """Helper to convert the arbitrary ways packages can be represented to a
    common (matchable) representation
    """
    pass


def _get_required_packages_for_imports(imports: Iterable[str]) -> List[str]:
    """Get the set of installable packages required by this list of imports"""
    pass
