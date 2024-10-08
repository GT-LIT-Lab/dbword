import requests
import zipfile
from dbword import SUBTLEX_PATH

def download(db:str, verbose:bool=True):
    """Download database to root directory
    
    Parameters
    ----------
    db: str
    
    verbose: bool
    """

    if db == 'subtlex':
        _subtlex_us(verbose)
        _unzip(db, verbose)
    
    def _subtlex_us(verbose:bool):
        url = "https://www.ugent.be/pp/experimentele-psychologie/en/research/documents/subtlexus/subtlexus2.zip"
        file_path = "data/subtlexus2.zip"
        response = requests.get(url)

        # Write the content to a file
        with open(file_path, "wb") as file:
            file.write(response.content)

        if verbose:
            print(f"File downloaded and saved as {file_path}")

    def _unzip(db:str, verbose:bool):

        if db == "subtlex":
            file = "data/subtlexus2.zip"

        with zipfile.ZipFile(file, 'r') as zip_ref:
            zip_ref.extractall(".")

        if verbose:
            print(f"File unzipped and saved as data/SUBTLEXus74286wordstextversion.txt")

            