import os

# Get the directory where this __init__.py file is located
PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))

# Subtlex
SUBTLEX_PATH = os.path.join(PACKAGE_DIR, "data", "subtlex-us.pkl")
SUBTLEX_HEAD = ["FREQcount","CDcount","FREQlow", "Cdlow", "SUBTLWF",	"Lg10WF", "SUBTLCD", "Lg10CD"]

# Kuperman
KUPERMAN_HEAD =["OccurTotal", "OccurNum", "Freq_pm", "Rating.Mean", "Rating.SD", "Dunno"]
KUPERMAN_PATH = os.path.join(PACKAGE_DIR, "data", "kuperman.pkl")