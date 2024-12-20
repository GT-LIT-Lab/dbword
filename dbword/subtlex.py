from dataclasses import dataclass, field
import pickle
from .config import SUBTLEX_PATH
import pandas as pd

@dataclass
class Subtlex(object):
    """Access Subtlex-US database"""

    # load database
    database: dict = field(init=False, default=None)

    # other attributes
    words: list[str]
    data: dict = field(init=False, default=None)
    
    def __post_init__(self):
        # Load the .pkl file after the dataclass fields are initialized
        with open(SUBTLEX_PATH, 'rb') as f:
            self.database = pickle.load(f)

    def extract(self):
        """Extract word data"""

        # what is each value in the output mean?
        headers = ["FREQcount","CDcount","FREQlow", "Cdlow", "SUBTLWF",	"Lg10WF", "SUBTLCD", "Lg10CD"]

        data = {}

        # go through selected words
        for _, word in enumerate(self.words):

            # account for capitalization issues
            try:
                _data = self.database[word]
            except KeyError:
                _data = self.database[word.capitalize()]

            # get data
            data[word] = {header: value for header, value in zip(headers, _data)}

        self.data = data

        return self

    def to_pandas(self):
        """Convert to pandas dataframe"""
        return pd.DataFrame(self.data).transpose()