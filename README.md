# dbword
Interacting with word-statistic databases

Currently, `dbword` supports access to the [Subtlex-US](https://www.ugent.be/pp/experimentele-psychologie/en/research/documents/subtlexus) data and [Kuperman](https://link.springer.com/article/10.3758/s13428-012-0210-4#Sec4) AoA ratings. More to follow. 

# Installation

```bash
git clone https://github.com/GT-LIT-Lab/dbword.git
cd dbword
pip install .
```

# Usage

```python
from dbword import Subtlex

words = ["hello", "screen", "jog"]

S = Subtlex(words).extract()

S.to_pandas()
```
## Example output
|        |   FREQcount |   CDcount |   FREQlow |   Cdlow |   SUBTLWF |   Lg10WF |   SUBTLCD |   Lg10CD |
|:-------|------------:|----------:|----------:|--------:|----------:|---------:|----------:|---------:|
| hello  |       29857 |      6405 |      3228 |    2089 |    585.43 |   4.4751 |     76.36 |   3.8066 |
| screen |        1193 |       766 |      1152 |     749 |     23.39 |   3.077  |      9.13 |   2.8848 |
| jog    |         123 |        99 |       110 |      95 |      2.41 |   2.0934 |      1.18 |   2      |

## Domain general attributes
Both `Subtlex` and `Kuperman` contain the same attributes.

```
- words: list[str]
    List of words specified in the words parameter

- data: dict
    Collected word data for each word specified in the words parameter

- database: dict
    Database 
```

## Domain general methods
Both `Subtlex` and `Kuperman` contain the same methods.

```
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
S.to_pandas().to_csv(path='words.csv')
```

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
There shouldn't be any issues with the program downloading and accessing the databases. If there is an problem, an error will display at import with the necessary steps to be taken. Fortuntately, you can install these databases directly from the GitHub repo **[recommended]**:

```python
from dbword.utils import download

# specify the database you wish to install
download(db='kuperman', source='github')
```
Or you can download them directly from the source:

```python
from dbword.utils import download

# specify the database you wish to install
download(db='kuperman', source='origin')
```

>[!WARNING]
Installing from origin means that the original files and the format which they uploaded in are downloaded to the package directory from the location on the internet at which the original authors placed the data. These files are then automatically parsed and converted to `.pkl` format. This process is longer and riskier than installing from the GitHub repo, as file locations are subject to changes.