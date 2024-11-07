import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "libs"))

from .main import GlobalPlugin


__all__ = [
    "GlobalPlugin",
]
