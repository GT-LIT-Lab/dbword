import os
import warnings

from .config import SUBTLEX_PATH, KUPERMAN_PATH
from .subtlex import Subtlex
from .kuperman import Kuperman

def check_subtlex() -> bool:
    """Check if database exists in root""" 
    return os.path.isfile(SUBTLEX_PATH)
    
if not check_subtlex():
    warnings.warn("Database not found \n Try running dbword.utils.download(<database>)", UserWarning)

def check_kuperman() -> bool:
    """Check if database exists in root""" 
    return os.path.isfile(KUPERMAN_PATH)

if not check_kuperman():
    warnings.warn("Database not found \n Try running dbword.utils.download(<database>)", UserWarning)
    
__all__ = ['subtlex']