from dataclasses import dataclass, field
import pickle
from .datasets import KUPERMAN_PATH, SUBTLEX_PATH, KUPERMAN_HEAD, SUBTLEX_HEAD
import pandas as pd

@dataclass
class Database(object):
    """Database class"""

    # load database
    dataset: str
    database: dict = field(init=False, default=None)

    # other attributes
    words: list[str]
    data: dict = field(init=False, default=None)
    
    def __post_init__(self):
        if self.dataset == "subtlex":
            self.dataset = SUBTLEX_PATH
            self.headers = SUBTLEX_HEAD
        elif self.dataset == "kuperman":
            self.dataset = KUPERMAN_PATH
            self.headers = KUPERMAN_HEAD

        with open(self.dataset, 'rb') as f:
            self.database = pickle.load(f)

    def __add__(self, other):
        if isinstance(other, list):
            self.words += other
        elif isinstance(other, str):
            self.words.append(other)
        return self

    def __sub__(self, other):
        if isinstance(other, list):
            [self.words.remove(word) for word in other]
        elif isinstance(other, str):
            self.words.remove(other)
        return self

    def extract(self):
        """Extract word data"""

        # what is each value in the output mean?
        headers = self.headers

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