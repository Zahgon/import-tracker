"""
This module implements utilities that enable tracking of third party deps
through import statements
"""
# Standard
from types import ModuleType
from typing import Any, Dict, Iterable, List, Optional, Set, Tuple, Union
import dis
import importlib
import os
import re
import sys

# Local
from . import constants
from .log import log

## Public ######################################################################


def track_module(
    module_name: str,
    package_name: Optional[str] = None,
    submodules: Union[List[str], bool] = False,
    track_import_stack: bool = False,
    full_depth: bool = False,
    detect_transitive: bool = False,
    show_optional: bool = False,
) -> Union[Dict[str, List[str]], Dict[str, Dict[str, Any]]]:
    """Track the dependencies of a single python module

    Args:
        module_name:  str
            The name of the module to track (may be relative if package_name
            provided)
        package_name:  Optional[str]
            The parent package name of the module if the module name is relative
        submodules:  Union[List[str], bool]
            If True, all submodules of the given module will also be tracked. If
            given as a list of strings, only those submodules will be tracked.
            If False, only the named module will be tracked.
        track_import_stack:  bool
            Store the stacks of modules causing each dependency of each tracked
            module for debugging purposes.
        full_depth:  bool
            Include transitive dependencies of the third party dependencies that
            are direct dependencies of modules within the target module's parent
            library.
        detect_transitive:  bool
            Detect whether each dependency is 'direct' or 'transitive'
        show_optional:  bool
            Show whether each requirement is optional (behind a try/except) or
            not

    Returns:
        import_mapping:  Union[Dict[str, List[str]], Dict[str, Dict[str, Any]]]
            The mapping from fully-qualified module name to the set of imports
            needed by the given module. If tracking import stacks or detecting
            direct vs transitive dependencies, the output schema is
            Dict[str, Dict[str, Any]] where the nested dicts hold "stack" and/or
            "type" keys respectively. If neither feature is enabled, the schema
            is Dict[str, List[str]].
    """
    pass


## Private #####################################################################


def _get_dylib_dir():
    """Different versions/builds of python manage different builtin libraries as
    "builtins" versus extensions. As such, we need some heuristics to try to
    find the base directory that holds shared objects from the standard library.
    """
    is_dylib = lambda x: x is not None and (x.endswith(".so") or x.endswith(".dylib"))
    all_mod_paths = list(
        filter(is_dylib, (getattr(mod, "__file__", "") for mod in sys.modules.values()))
    )
    # If there's any dylib found, return the parent directory
    sample_dylib = None
    if all_mod_paths:
        sample_dylib = all_mod_paths[0]
    else:  # pragma: no cover
        # If not found with the above, look through libraries that are known to
        # sometimes be packaged as compiled extensions
        #
        # NOTE: This code may be unnecessary, but it is intended to catch future
        #   cases where the above does not yield results
        #
        # More names can be added here as needed
        for lib_name in ["cmath"]:
            lib = importlib.import_module(lib_name)
            fname = getattr(lib, "__file__", None)
            if is_dylib(fname):
                sample_dylib = fname
                break

    # If all else fails, we'll just return a sentinel string. This will fail to
    # match in the below check for builtin modules
    return (
        os.path.realpath(os.path.dirname(sample_dylib))
        if sample_dylib is not None
        else "BADPATH"
    )


# The path where global modules are found
_std_lib_dir = os.path.realpath(os.path.dirname(os.__file__))
_std_dylib_dir = _get_dylib_dir()
_known_std_pkgs = [
    "collections",
]


# Regex for matching lines in the exception table
_exception_table_expr = re.compile(r"  ([0-9]+) to ([0-9]+) -> [0-9]+ \[([0-9]+)\].*")


def _mod_defined_in_init_file(mod: ModuleType) -> bool:
    """Determine if the given module is defined in an __init__.py[c]"""
    pass


def _get_import_parent_path(mod_name: str) -> str:
    """Get the parent directory of the given module"""
    pass


def _is_third_party(mod_name: str) -> bool:
    """Detect whether the given module is a third party (non-standard and not
    import_tracker)"""
    pass


def _get_non_std_modules(mod_names: Iterable[str]) -> Set[str]:
    """Take a snapshot of the non-standard modules currently imported"""
    pass


def _get_value_col(dis_line: str) -> str:
    """Parse the string value from a `dis` output line"""
    pass


def _get_op_number(dis_line: str) -> Optional[int]:
    """Get the opcode number out of the line of `dis` output"""
    pass


def _get_try_end_number(
    dis_line: str,
    op_num: Optional[int],
    exception_table: Dict[int, int],
) -> Optional[int]:
    """If the line contains a known indicator for a try block, get the
    corresponding end number

    NOTE: This contains compatibility code for changes between 3.10 and 3.11
    """
    pass


def _get_exception_table(dis_lines: List[str]) -> Dict[int, int]:
    """For 3.11+ exception handling, parse the Exception Table"""
    pass


def _figure_out_import(
    mod: ModuleType,
    dots: Optional[int],
    import_name: Optional[str],
    import_from: Optional[str],
) -> ModuleType:
    """This function takes the set of information about an individual import
    statement parsed out of the `dis` output and attempts to find the in-memory
    module object it refers to.
    """
    pass


def _get_imports(mod: ModuleType) -> Tuple[Set[ModuleType], Set[ModuleType]]:
    """Get the sets of required and optional imports for the given module by
    parsing its bytecode
    """
    pass


def _find_parent_direct_deps(
    module_deps_map: Dict[str, List[str]]
) -> Dict[str, Dict[str, List[str]]]:
    """Construct a mapping for each module (e.g. foo.bar.baz) to a mapping of
    parent modules (e.g. [foo, foo.bar]) and the sets of imports that are
    directly imported in those modules. This mapping is used to augment the sets
    of required imports for each target module in the final flattening.
    """
    pass


def _flatten_deps(
    module_name: str,
    module_deps_map: Dict[str, List[str]],
    parent_direct_deps: Dict[str, Dict[str, List[str]]],
) -> Tuple[Dict[str, List[str]], Dict[str, bool]]:
    """Flatten the names of all modules that the target module depends on"""
    pass
