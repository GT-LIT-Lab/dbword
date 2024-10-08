import os
import warnings

from .config import SUBTLEX_PATH
from .subtlex import Subtlex

def check() -> bool:
    """Check if database exists in root""" 
    return os.path.isfile(SUBTLEX_PATH)
    
if not check():
    warnings.warn("Database not found \n Try running dbword.utils.download(<database>)", UserWarning)
    
__all__ = ['subtlex']