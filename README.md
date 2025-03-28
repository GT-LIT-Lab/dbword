# dbword
Interacting with word-statistic databases

Currently, `dbword` supports access to the [Subtlex-US](https://www.ugent.be/pp/experimentele-psychologie/en/research/documents/subtlexus) data and [Kuperman](https://link.springer.com/article/10.3758/s13428-012-0210-4#Sec4) AoA ratings. More to follow. 

# Installation

```bash
pip install git+https://github.com/GT-LIT-LAB/dbword.git
```

# Usage

```python
from dbword import Database

words = ["hello", "screen", "jog"]

D = Database(dataset="subtlex", words=words).extract()

D.to_pandas()
```
## Example output
|        |   FREQcount |   CDcount |   FREQlow |   Cdlow |   SUBTLWF |   Lg10WF |   SUBTLCD |   Lg10CD |
|:-------|------------:|----------:|----------:|--------:|----------:|---------:|----------:|---------:|
| hello  |       29857 |      6405 |      3228 |    2089 |    585.43 |   4.4751 |     76.36 |   3.8066 |
| screen |        1193 |       766 |      1152 |     749 |     23.39 |   3.077  |      9.13 |   2.8848 |
| jog    |         123 |        99 |       110 |      95 |      2.41 |   2.0934 |      1.18 |   2      |

## Attributes
`Database` contains the following attributes. 

```
- words: list[str]
    List of words specified in the words parameter

- data: dict
    Collected word data for each word specified in the words parameter

- database: dict
    Database 
```

## Methods
`Database` contains the following methods.

```
- __add__()
    Add another word to self.words

- __sub__()
    Remove a word from self.words

- extract()
    Extract data for each word specified in the words parameter

    returns: dict

- to_pandas()
    Convert data to pandas.DataFrame()

    returns: pandas.DataFrame(self.data).transpose()
```

## Why `pandas`?
You can use `pandas` to convert the dataframe to whatever necessary format you wish. For example, I can save the output as a `.csv` file with just an additional method call:

```python
D.to_pandas().to_csv(path='words.csv')
```

## Preprocessing large text

`dbword` also allows you to parse a large string should you need to extract word-level statistics from a paragraph or more of text. 

```python
from dbword.preprocess import preprocess

text = """
Louisiana is a state in the southeastern region of the United States. It is the 19th-smallest by area and the 25th most populous of the 50 U.S. states. Louisiana is bordered by the state of Texas to the west, Arkansas to the north, Mississippi to the east, and the Gulf of Mexico to the south. A large part of its eastern boundary is demarcated by the Mississippi River. Louisiana is the only U.S. state with political subdivisions termed parishes, which are equivalent to counties. The state's capital is Baton Rouge, and its largest city is New Orleans.
"""

words = preprocess(text)
```

This function returns a list of strings, which is the data type required by `dbword`. But `preprocess()` does more than this. In total, `preprocess()`:

1. Parses a piece of text into a list of strings (`list[str]`). This is carried out with an internal function called `listify()`.
2. Removes punctuation. This is carried out with an internal function call `rm_punct()`. 
3. Removes invalid elements like hyphenated words and numbers. This is carried out with an internal function called `rm_invalid()`. 
4. Removes duplicate elements. This is carried out with an internal function called `consolidate()`.

> [!NOTE] 
> All internal functions mentioned above are located within the `preprocessing` module. You can import these individually to support specific preprocessing needs. 

> [!CAUTION]  
> `preprocess()` is intended to serve as a quick work-around for handling text data. As such it may remove important tokens from a given text. If this is an issue, it is recommended that alternative methods be taken to parse your text. Additionally, `preprocess()` may _not_ remove _all_ invalid tokens, in turn causing an error during data extraction. Edge cases like these should be [submitted as an issue](https://github.com/GT-LIT-Lab/dbword/issues/new) to the GitHub repository. 

# Database information
Each database is automatically installed in the package directory as a `.pkl` file. Run the following code to see each database's file.

```python
from dbword.config import PACKAGE_DIR
import os

os.listdir(os.path.join(PACKAGE_DIR, "data"))
```
```
>>> ['kuperman.pkl', 'subtlex-us.pkl']
```
Each database is type `dict`. This makes indexing (what the program is doing under the hood) very easy and generally not explosive. Based on internal tests, extracting data from 15 words takes approximately **0.02 seconds**. Extracting data from 100 words takes approximately **0.05 seconds**. Extracting data from 10,000 words takes approximately **0.09 seconds**.

## Install failures
There shouldn't be any issues with the program downloading and accessing the databases. If there is a problem, an error will display at import with the necessary steps to be taken. Fortuntately, you can install these databases directly from the GitHub repo **[recommended]**:

```python
from dbword.utils import download

# specify the database you wish to install
download(dataset='kuperman', source='github')
```
Or you can download them directly from the source:

```python
from dbword.utils import download

# specify the database you wish to install
download(dataset='kuperman', source='origin')
```

>[!WARNING]
Installing from origin means that the original files and the format which they uploaded in are downloaded to the package directory from the location on the internet at which the original authors placed the data. These files are then automatically parsed and converted to `.pkl` format. This process is longer and riskier than installing from the GitHub repo, as file locations are subject to changes.
