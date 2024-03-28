# rainbowprint - an example of a simple Python package

I built this repository as a template to show a simple installable Python package. The package can only do one (pretty useless) thing: apply a `matplotlib` color gradient to a string and print it to the screen. The default color map is `cool`:

<img src="docs/example1.png" width="500" />

It also works [inside a Jupyter notebook](docs/notebook1.ipynb).

The most basic structure for the package to be installable is:

	rainbowprint/
	├── pyproject.toml
	└── src/
	    └── rainbowprint/
	        ├── __init__.py
	        └── functions.py

With just the soure code and the **pyproject.toml** file, the repository is already installable as a Python package. It will be the bare minimum though. Further down I list many things that can make a package better.

## Installation:

  	pip install git+https://github.com/TristanCantatGaudin/rainbowprint.git

Or, to install it in a fresh environment:

   	conda create -n someNewEnvName
   	conda activate someNewEnvName
   	conda install pip

and then go for `pip install...`

To test in one line that it worked, you can type:

	python -c "from rainbowprint.functions import rainbowprint; rainbowprint('This is a rainbow')"

 **NB:** if we leave `__init__.py` empty then the above works, but the following doesnt:

	import rainbowprint
	rainbowprint.functions.rainbowprint('some string')

and crashes with the error message *AttributeError: module 'rainbowprint' has no attribute 'functions'*. We can add `from .functions import *` to the `__init__.py` file so that importing the package imports the `functions` module too. At also allows `from rainbowprint import functions` to work, because the module now exists in the namespace of the package.

## Necessary file: pyproject.toml

This file contains some basic information about the package (e.g. name, version) but importantly lists dependencies (in the present case `matplotlib`, it will be automatically installed when you install `rainbowprint`) and the installation package (called a *build backend*) that `pip` (the *build frontend* tool) will rely on for the installation (here we chose `setuptools` as a build backend).

# Improving the package

All the rest is "optional", but many extra features are useful. For instance, having a `README.md` file in the main directory of the repository (this file). GitHub creates one by default when you create a repo, unless you explicitly ask it not to. It can also automatically create a `LICENSE` file (see e.g. https://choosealicense.com).

## tests

In the main directory, create a `tests` dir. It can contain several .py files, each one possibly containing several functions. There are several packages to run test suites, I use `pytest` (which is pip installable). When in the main directory, running the command `pytest` will run all the tests inside the `tests` directory. If you are inside the `tests` directory you can also run a specific subset of tests, for instance `pytest test_import.py`.

## workflow to run tests

A workflow is a script that GitHub runs automatically on its servers. These scripts have to be placed in the directory `rainbowprint/.github/workflows/`, and are written in YAML (a very human-readable language). The script can be run on a schedule (every hour, every day at 9am, every Monday, etc see [cron scheduling](https://en.wikipedia.org/wiki/Cron)). It can also be triggered by a commit or a pull, or manually (on: `workflow_dispatch`).

A convenient set up is to use workflows to install the package and run tests after each commit. If the last commit breaks something, we then know it immediately. You can use multiple versions of Python, OS, etc and the jobs will be run in parallel inside multiple virtual machines. You can set up the workflow to only be triggered by commits to a certain branch (e.g. main), or only changes to certain files or directories. Here I have set it up to not be executed if changes are made to the README file.

**NB:** if the tests fail it doesn't necessarily mean the problem was caused by your update (the bug may come from external dependencies), so go check the complete log of the run.


## workflow to compile notebooks

in `Settings -> Actions -> General -> Workflow permissions` make sure that "Read and write permissions" is enabled, to allow the GitHub Actions bot to commit new files to the repository. 

I created a second workflow which installs the present package and Jupyter, then executes the notebook in `docs/notebook1.ipynb`, then converts the result to an HTML page and uploads (commits + pushes) both these files to the repository. This workflow can only be started manually. The resulting page is visible here: https://htmlpreview.github.io/?https://github.com/TristanCantatGaudin/rainbowprint/blob/main/docs/notebook1.html

**NB:** if the newly compiled notebook (and corresponding HTML) is unchanged, then "git add ..." will do nothing, and the GitHub Actions both will not upload any new file, which may cause the workflow to exit with an error. So for the sake of this example the notebook also prints the current date and time, just to make sure that the workflow creates new files every time.

## documentation with sphinx

Install `sphinx locally` (or `pip install sphinx-rtd-theme` etc to install other themes, see https://sphinx-themes.org/):

	pip install sphinx
 	cd docs
  	sphinx-quickstart

This will prompt a few basic questions (package name, author, version) and create new files. 

...

## workflow for linting

...

## pypi 

tags, versions, releases
