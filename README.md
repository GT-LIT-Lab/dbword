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