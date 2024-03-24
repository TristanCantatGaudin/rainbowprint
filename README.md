# rainbowprint

The most basic structure for the package to be installable:

	rainbowprint/
	├── LICENSE
	├── pyproject.toml
	├── README.md
	├── src/
	│   └── rainbowprint/
	│       ├── __init__.py
	│       └── functions.py
	└── tests/

  ## Installation:

  	pip install git+https://github.com/TristanCantatGaudin/rainbowprint.git

Or, to install it in a fresh environment:

   	conda create -n someNewEnvName
    	conda activate someNewEnvName
    	conda install pip

and then go for `pip install...`

## pyproject.toml

This file contains some basic information about the package (e.g. name, version) but importantly lists dependencies (in the present case `matplotlib`, it will be automatically installed when you install `rainbowprint`) and the installation package that `pip` will rely on for the installation (here, `setuptools`).
