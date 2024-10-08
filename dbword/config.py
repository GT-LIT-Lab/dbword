import os

# Get the directory where this __init__.py file is located
PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))
SUBTLEX_PATH = os.path.join(PACKAGE_DIR, "data", "subtlex-us.pkl")