"""
molecool
A Python package for analyzing and visualizing xyz files. For MolSSI Workshop Python Packag development workshop.
"""

# Add imports here
# we aren't using the * because this imports literalyl everything so we use the actual file names
# if you still want to use * you could say __all__ = ["calculate_distance", "calculate_angle"]
from .functions import *
from .measure import calculate_distance, calculate_angle
from .molecule import build_bond_list
from .visualize import draw_molecule, bond_histogram
from .io import open_pdb, open_xyz, write_xyz

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
