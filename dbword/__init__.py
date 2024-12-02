import os
import warnings

from .config import SUBTLEX_PATH, KUPERMAN_PATH, PACKAGE_DIR
from .subtlex import Subtlex
from .kuperman import Kuperman
from .preprocess import preprocess, consolidate, rm_punct, listify, rm_invalid

def check_subtlex() -> bool:
    """Check if database exists in root""" 
    return os.path.isfile(SUBTLEX_PATH)
    
def check_kuperman() -> bool:
    """Check if database exists in root""" 
    return os.path.isfile(KUPERMAN_PATH)

def __getattr__(name):
    if name == 'Kuperman':
        if not check_kuperman():
            warnings.warn(f"Kuperman database not found \n Try running dbword.utils.download('kuperman')", UserWarning)
        return Kuperman
    
    elif name == 'Subtlex':
        if not check_subtlex():
            warnings.warn(f"Subtlex database not found \n Try running dbword.utils.download('subtlex')", UserWarning)
        return Subtlex
    
    raise AttributeError(f"module {__name__} has no attribute {name}")
    
__all__ = ['Subtlex', 'Kuperman']