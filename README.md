# rainbowprint

I built this repository as a template showing a simple installable Python package. The package can only do one (pretty useless) thing: apply a `matplotlib` color gradient to a string and print it to the screen. The default color map is `cool`. Example:

<img src="docs/example1.png" width="500" />

The most basic structure for the package to be installable is:

	rainbowprint/
	├── pyproject.toml
	└── src/
	    └── rainbowprint/
	        ├── __init__.py
	        └── functions.py

With just the soure code and a pyproject.toml file, the repository is already installable as a Python package. It will be the bare minimum though. Further down I list many things that can make a package better.

## Installation:

  	pip install git+https://github.com/TristanCantatGaudin/rainbowprint.git

Or, to install it in a fresh environment:

   	conda create -n someNewEnvName
   	conda activate someNewEnvName
   	conda install pip

and then go for `pip install...`

To test in one line that it worked, you can type:

	python -c "from rainbowprint.functions import rainbowprint; rainbowprint('This is a rainbow')"

## Necessary file: pyproject.toml

This file contains some basic information about the package (e.g. name, version) but importantly lists dependencies (in the present case `matplotlib`, it will be automatically installed when you install `rainbowprint`) and the installation package (called a *build backend*) that `pip` (the *build frontend* tool) will rely on for the installation (here we chose `setuptools` as a build backend).

# Improving the package

All the rest is "optional", but many extra features are useful. For instance, having a `README.md` file in the main directory of the repository (this file). GitHub creates one by default when you create a repo, unless you explicitly ask it not to. It can also automatically create a `LICENSE` file (see e.g. https://choosealicense.com).

## tests

In the main directory, create a `tests` dir. It can contain several .py files, each one possibly containing several functions. There are several packages to run test suites, I use `pytest` (which is pip installable). When in the main directory, running the command `pytest` will run all the tests inside the `tests` directory. If you are inside the `tests` directory you can also run a specific subset of tests, for instance `pytest test_import.py`.

# Better
* tests (at least import), pytest + workflow
* notebook example + compile workflow
* documentation (sphynx in repo, or readthedocs)
* pypi
