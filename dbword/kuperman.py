from dataclasses import dataclass, field
import pickle
from .config import KUPERMAN_PATH
import pandas as pd

@dataclass
class Kuperman(object):
    """Access Subtlex-US database"""

    # load database
    database: dict = field(init=False, default=None)

    # other attributes
    words: list[str]
    data: dict = field(init=False, default=None)
    
    def __post_init__(self):
        # Load the .pkl file after the dataclass fields are initialized
        with open(KUPERMAN_PATH, 'rb') as f:
            self.database = pickle.load(f)

    def extract(self):
        """Extract word data"""

        # what is each value in the output mean?
        headers = ["OccurTotal", "OccurNum", "Freq_pm", "Rating.Mean", "Rating.SD", "Dunno"]

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

    @property
    def to_panda(self):
        """Convert to pandas dataframe"""
        return pd.DataFrame(self.data).transpose()