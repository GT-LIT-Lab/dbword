"""Downloading databases

The following code handles database reinstallation if the import process fails
"""

import requests
import zipfile
from .config import PACKAGE_DIR
import pickle
import pandas as pd
import os

def download(db:str, source:str, verbose:bool=True):
    """Download database to root directory
    
    Parameters
    ----------
    db: str

    source: str, 'origin' or 'github'
    
    verbose: bool
    """

    if db == 'subtlex':
        _subtlex_us(source, verbose)

        if source == 'origin':
            _unzip(db, verbose)
            _ = convert_to_pickle(path=os.path.join(PACKAGE_DIR, "data", "SUBTLEXus74286wordstextversion.txt"),
                            fname="subtlex-us", verbose=verbose)

    if db == 'kuperman':
        _kuperman(source, verbose)

        if source == "origin":
            _ = convert_to_pickle(path=os.path.join(PACKAGE_DIR, "data", "kuperman.txt"),
                            fname='kuperman', verbose=verbose)

    if source.lower() == 'origin':
        # clean up unnecessary files
        _clear_extra(db)

def _subtlex_us(source:str, verbose:bool):

    if source.lower() == 'origin':
        url = "https://www.ugent.be/pp/experimentele-psychologie/en/research/documents/subtlexus/subtlexus2.zip"
        file_path = os.path.join(PACKAGE_DIR, "data", "subtlexus2.zip")
    
    elif source.lower() == 'github':
        url = "https://github.com/GT-LIT-Lab/dbword/blob/main/dbword/data/subtlex-us.pkl"
        file_path = os.path.join(PACKAGE_DIR, "data", "subtlex-us.pkl")
    
    # Check if file already exists
    if not os.path.exists(file_path):
        response = requests.get(url)
        response.raise_for_status()

        # Write the content to a file
        with open(file_path, "wb") as file:
            file.write(response.content)

        if verbose:
            print(f"File downloaded and saved as {file_path}")
    else:
        if verbose:
            print(f"File already exists: {file_path}")

def _unzip(db:str, verbose:bool):

    if db == "subtlex":
        file = os.path.join(PACKAGE_DIR, "data", "subtlexus2.zip")

    with zipfile.ZipFile(file, 'r') as zip_ref:
        zip_ref.extractall(os.path.join(PACKAGE_DIR, "data"))

    if verbose:
        print(f"File downloaded, unzipped and saved as data/SUBTLEXus74286wordstextversion.txt")

def _kuperman(source:str, verbose:bool):

    if source.lower() == "origin":
        url = "https://static-content.springer.com/esm/art%3A10.3758%2Fs13428-013-0348-8/MediaObjects/13428_2013_348_MOESM1_ESM.xlsx"
        file_path = os.path.join(PACKAGE_DIR, "data", "13428_2013_348_MOESM1_ESM.xlsx")

    elif source.lower() == "github":
        url = "https://github.com/GT-LIT-Lab/dbword/blob/main/dbword/data/kuperman.pkl"
        file_path = os.path.join(PACKAGE_DIR, "data", "kuperman.pkl")
    
    # Check if file already exists
    if not os.path.exists(file_path):
        response = requests.get(url)
        response.raise_for_status()

        with open(file_path, "wb") as file:
            file.write(response.content)

    if source.lower() == "origin":

        new_file_path = os.path.join(PACKAGE_DIR, "data", "kuperman.xlsx")

        # go ahead and rename file here
        os.rename(file_path, new_file_path)

        # convert to txt
        df = pd.read_excel(new_file_path)
        txt_file_path = os.path.join(PACKAGE_DIR, "data", "kuperman.txt")
        df.to_csv(txt_file_path, sep='\t', index=False)

        if verbose:
            print(f"File downloaded and saved as {txt_file_path}")       

def convert_to_pickle(path:str, fname:str, verbose:bool=False):
    """Convert database into pickle
    
    Parameters
    ----------
    path: str
        Path to .txt file

    fname: str
        What you want to name you pkl file
        
    Returns
    -------
    database: dict
        Dictionary of Subtlex database
    """

    assert path.endswith('.txt')

    # store data
    data = {} 

    with open(path, 'r') as file:
    
        # skip the headers
        header = file.readline().strip().split('\t')
        
        # create the dict
        data = {
            line.split('\t')[0]: [value for value in line.split('\t')[1:]]
            for line in file
        }

    # Save as .pkl 
    with open(os.path.join(PACKAGE_DIR, "data", f'{fname}.pkl'), 'wb') as pkl_file:
        pickle.dump(data, pkl_file)

    if verbose:
        print(f"Database converted to pickle: '{fname}.pkl'")

def _clear_extra(db:str):
    """Remove extra files"""

    if db == "kuperman":
        os.remove(os.path.join(PACKAGE_DIR, "data", "kuperman.txt"))
        os.remove(os.path.join(PACKAGE_DIR, "data", "kuperman.xlsx"))
    elif db == "subtlex":
        os.remove(os.path.join(PACKAGE_DIR, "data", "SUBTLEXus74286wordstextversion.txt"))
        os.remove(os.path.join(PACKAGE_DIR, "data", "subtlexus2.zip"))