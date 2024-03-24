# rainbowprint

The most basic structure with the absolute minimum for the package to be installable:

	rainbowprint/
	├── pyproject.toml
	└── src/
	    └── rainbowprint/
	        ├── __init__.py
	        └── functions.py

Here we also have a README.md and a LICENSE file. We can also have a directories containing tests.

  ## Installation:

  	pip install git+https://github.com/TristanCantatGaudin/rainbowprint.git

Or, to install it in a fresh environment:

   	conda create -n someNewEnvName
    	conda activate someNewEnvName
    	conda install pip

and then go for `pip install...`

## pyproject.toml

This file contains some basic information about the package (e.g. name, version) but importantly lists dependencies (in the present case `matplotlib`, it will be automatically installed when you install `rainbowprint`) and the installation package (called a *build backend*) that `pip` will rely on for the installation (here, `setuptools`).
