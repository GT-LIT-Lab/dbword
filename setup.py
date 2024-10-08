from setuptools import setup, find_packages

setup(
    name="dbword",
    version="1.0.1",
    author="Will Decker",
    author_email="will.decker@gatech.edu",
    description="Accessing word statistics databases",
    url="https://github.com/GT-LIT-Lab/dbword",
    packages=find_packages(),
    package_data={
        'dbword': ['data/subtlex-us.pkl'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering"
    ]

)