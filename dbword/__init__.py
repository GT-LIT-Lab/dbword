import os
import warnings

from .config import SUBTLEX_PATH, KUPERMAN_PATH
from .subtlex import Subtlex
from .kuperman import Kuperman

def check_subtlex() -> bool:
    """Check if database exists in root""" 
    return os.path.isfile(SUBTLEX_PATH)
    
if not check_subtlex():
    warnings.warn("Subtlex database not found \n Try running dbword.utils.download('subtlex')", UserWarning)

def check_kuperman() -> bool:
    """Check if database exists in root""" 
    return os.path.isfile(KUPERMAN_PATH)

if not check_kuperman():
    warnings.warn("Kuperman database not found \n Try running dbword.utils.download('kuperman')", UserWarning)
    
__all__ = ['Subtlex', 'Kuperman']