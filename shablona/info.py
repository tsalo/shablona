import importlib.util
import json
import os.path as op

spec = importlib.util.spec_from_file_location(
    "_version", op.join(op.dirname(__file__), "shablona/_version.py")
)
_version = importlib.util.module_from_spec(spec)
spec.loader.exec_module(_version)

VERSION = _version.get_versions()["version"]
del _version

# Get list of authors from Zenodo file
with open(op.join(op.dirname(__file__), ".zenodo.json"), "r") as fo:
    zenodo_info = json.load(fo)
authors = [author["name"] for author in zenodo_info["creators"]]
authors = [author.split(", ")[1] + " " + author.split(", ")[0] for author in authors]

CLASSIFIERS = ["Development Status :: 3 - Alpha",
               "Environment :: Console",
               "Intended Audience :: Science/Research",
               "License :: OSI Approved :: MIT License",
               "Operating System :: OS Independent",
               "Programming Language :: Python",
               "Topic :: Scientific/Engineering"]

NAME = "shablona"
MAINTAINER = "Ariel Rokem"
MAINTAINER_EMAIL = "arokem@gmail.com"
DESCRIPTION = "shablona: a template for small scientific Python projects"
LONG_DESCRIPTION = """

Shablona
========
Shablona is a template project for small scientific Python projects.

It contains software implementations of an analysis of some simple data, but
more importantly, it contains infrastructure for testing, documentation,
continuous integration and deployment, which can be easily adapted
to use in other projects.

To get started using these components in your own software, please go to the
repository README_.

.. _README: https://github.com/uwescience/shablona/blob/master/README.md

License
=======
``shablona`` is licensed under the terms of the MIT license. See the file
"LICENSE" for information on the history of this software, terms & conditions
for usage, and a DISCLAIMER OF ALL WARRANTIES.

All trademarks referenced herein are property of their respective holders.

Copyright (c) 2015--, Ariel Rokem, The University of Washington
eScience Institute.
"""
URL = "http://github.com/uwescience/shablona"
DOWNLOAD_URL = ""
LICENSE = "MIT"
AUTHOR = "Ariel Rokem"
AUTHOR_EMAIL = "arokem@gmail.com"
PLATFORMS = "OS Independent"
PACKAGE_DATA = {'shablona': [op.join('data', '*')]}
REQUIRES = [
    "numpy",
    "scipy",
    "matplotlib",
    "pandas",
]
EXTRA_REQUIRES = {
    "dev": [
        "pytest==4.6.3",
        "coveralls",
        "pytest-cov",
        "flake8",
    ],
    "doc": [
        "sphinx>=3.1.1",
    ]
}
PYTHON_REQUIRES = ">= 3.5"
