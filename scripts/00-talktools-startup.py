"""IPython startup script to make talktools module available.

This script runs automatically when IPython/Jupyter starts.
It adds the talktools module to the path so helper functions like
youtube(), callout(), columns(), etc. are available.

Note: CSS styling is loaded separately via ~/.jupyter/custom/custom.css
for instant styling on page load.
"""

import sys
from pathlib import Path

def _find_talktools_path():
    """Find the path containing talktools.py."""
    possible_paths = [
        Path.cwd() / "lectures",
        Path.cwd(),
        Path.cwd().parent,
    ]

    # Search up the directory tree
    cwd = Path.cwd()
    for _ in range(5):
        if (cwd / "lectures" / "talktools.py").exists():
            return cwd / "lectures"
        if (cwd / "talktools.py").exists():
            return cwd
        cwd = cwd.parent

    for path in possible_paths:
        if (path / "talktools.py").exists():
            return path

    return None

def _setup_talktools():
    """Add talktools to path so it can be imported."""
    path = _find_talktools_path()
    if path and str(path) not in sys.path:
        sys.path.insert(0, str(path))

# Only run in Jupyter notebooks, not regular IPython
try:
    ip = get_ipython()
    if 'zmqshell' in str(type(ip)):
        _setup_talktools()
except NameError:
    pass
