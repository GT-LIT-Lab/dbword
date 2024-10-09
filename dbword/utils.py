import requests
import zipfile
from dbword import SUBTLEX_PATH
import pickle
import os

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

def convert_to_pickle(path:str, fname:str, verbose:bool=False):
    """Convert downloaded Subtlex file into pickle
    
    Parameters
    ----------
    path: str
        Path to .txt file

    fname: str
        What you want to name you pkl file
        
    Returns
    -------
    subtlex: dict
        Dictionary of Subtlex database
    """

    assert path.endswith('.txt')

    # store data
    data = {} 

    with open(path, 'r') as file:
       
        # this will skip the headers
        header = file.readline().strip().split('\t')
        
        # create the dict
        data = {
            line.split('\t')[0]: [value for value in line.split('\t')[1:]]
            for line in file
        }

    # Save as .pkl 
    with open(f'{fname}.pkl', 'wb') as pkl_file:
        pickle.dump(data, pkl_file)

    if verbose:
        print(f"Data has been saved as '{fname}.pkl'")

