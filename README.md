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

and then go for `pip install git+https://github.com/TristanCantatGaudin/rainbowprint.git`

To test in one line that it worked, you can type:

	python -c "from rainbowprint.functions import rainbowprint; rainbowprint('This is a rainbow')"

 **NB:** if we leave `__init__.py` empty then the above works, but the following doesnt:

	import rainbowprint
	rainbowprint.functions.rainbowprint('some string')

and crashes with the error message *AttributeError: module 'rainbowprint' has no attribute 'functions'*. We can add `from .functions import *` to the `__init__.py` file so that importing the package imports the `functions` module too. It also allows `from rainbowprint import functions` to work, because the module now exists in the namespace of the package.

## Necessary file: pyproject.toml

This file contains some basic information about the package (e.g. name, version) but importantly lists dependencies (in the present case `matplotlib`, it will be automatically installed when you install `rainbowprint`) and the installation package (called a *build backend*) that `pip` (the *build frontend* tool) will rely on for the installation (here we chose `setuptools` as a build backend).

# Improvements

Everything beyond this point is "optional", but many extra features are useful. For instance, having a `README.md` file in the main directory of the repository (this file). GitHub creates one by default when you create a repo, unless you explicitly ask it not to. It can also automatically create a `LICENSE` file (see e.g. https://choosealicense.com).

## tests

In the main directory, create a `tests` dir. It can contain several .py files, each one possibly containing several functions. There are several packages to run test suites, I use `pytest` (which is pip installable). When in the main directory, running the command `pytest` will run all the tests inside the `tests` directory. If you are inside the `tests` directory you can also run a specific subset of tests, for instance `pytest test_import.py`.

## workflow to run tests

A workflow is a script that GitHub runs automatically on its servers. These scripts have to be placed in the directory `rainbowprint/.github/workflows/`, and are written in YAML (a very human-readable language). The script can be run on a schedule (every hour, every day at 9am, every Monday, etc see [cron scheduling](https://en.wikipedia.org/wiki/Cron)). It can also be triggered by a commit or a pull, or manually (on: `workflow_dispatch`).

A convenient set up is to use workflows to install the package and run tests after each commit. If the last commit breaks something, we then know it immediately. You can use multiple versions of Python, OS, etc and the jobs will be run in parallel inside multiple virtual machines. You can set up the workflow to only be triggered by commits to a certain branch (e.g. main), or only changes to certain files or directories. Here I have set it up to not be executed if changes are made to the README file.

**NB:** if the tests fail it doesn't necessarily mean the problem was caused by your update (the bug may come from external dependencies), so go check the complete log of the run.


## workflow to compile notebooks

in `Settings -> Actions -> General -> Workflow permissions` make sure that "Read and write permissions" is enabled, to allow the GitHub Actions bot to commit new files to the repository. 

I created a second workflow which installs the present package and Jupyter, then executes the notebook in `docs/notebook1.ipynb`, then converts the result to an HTML page and uploads (commits + pushes) both these files to the repository. This workflow can only be started manually. The resulting page is visible here: https://htmlpreview.github.io/?https://github.com/TristanCantatGaudin/rainbowprint/blob/main/docs/notebook1.html

**NB:** if the newly compiled notebook (and corresponding HTML) is unchanged, then "git add ..." will do nothing, and the GitHub Actions bot will not upload any new file, which may cause the workflow to exit with an error. So for the sake of this example the notebook also prints the current date and time, just to make sure that the workflow creates new files every time. **tip:** you can also do `git commit -m "Update documentation" -a || true` to allow the workflow to proceed even in case of error.

## local documentation with sphinx

Install `sphinx` locally (or `pip install sphinx-rtd-theme` etc to install other themes, see https://sphinx-themes.org/):

	pip install sphinx
	sphinx-quickstart docs
	sphinx-apidoc --output-dir docs src/rainbowprint --separate
	cd docs

This created a bunch of files, including several `.rst` files which we are later going to "compile" into HTML web pages. They can be edited manually, you can write any text you like, and in particular we want to open `index.rst` and add a reference to the `module.rst` file, like this:

	Welcome to rainbowprint's documentation!
	========================================
	
	.. toctree::
	   :maxdepth: 2
	   :caption: Contents:
	
	   modules
	
	Indices and tables
	==================
	
	* :ref:`genindex`
	* :ref:`modindex`
	* :ref:`search`

Then we open `conf.py` and replace `extensions = []` with `extensions = ['sphinx.ext.autodoc']`. This extension allows sphinx to read the docstrings from our source code and create the nice looking documentation.

Now build the HTML pages with:

	make html

The documentation index page is now at: `rainbowprint/docs/_build/html/index.html`

**Btw:** If you modify the docstrings in the `.py` files, all you need to re-run is `make html`.

**Publishing the documentation:** it is common to NOT have a `docs` directory on the main branch, and to INSTEAD upload the HTML pages to a separate branch of the repo, which doesn't contain any of the code. GitHub allows you to enable GitHub Pages for that one branch (if you create a branch name `gh-pages` it is even enabled by default). In the present case (since we activated GitHub Pages for a branch of this repo) the documentation is accessible at: https://tristancantatgaudin.github.io/rainbowprint 

**Tip 1:** on GitHub pages the directories starting with an underscore are sometimes ignored when rendering HTML pages, but Sphinx outputs directories with underscores. Add an empty file named `docs/.nojekyll` to your doc to solve this.

**Tip 2:** if you add `"nbsphinx"` to the extensions in `conf.py` (and add it to the list of dependencies!), your tables of content will support notebooks, but you also need `pandoc` for this, it takes a few more steps to get that to work through GitHub actions (but I think ReadTheDocs can handle it).

Building and publishing the documentation can even be automated with GitHub actions, to keep up to date with code changes.
Tutorial for how to change theme, host documentation pages etc: https://olgarithms.github.io/sphinx-tutorial/

## workflow for sphinx

If we upload the result of `sphinx-quickstart` and `sphinx-apidoc` to our main branch, we can use a workflow to perform the `make` and deployment. In `pyproject.toml` I have specified optional dependencies that are only installed by the documentation workflow, which then builds the HTML pages, and pushes the pages to the branch `gh-pages` (this branch needs to already exist).

## ReadTheDocs

Create an account and import your project. Follow instructions to create `.readthedocs.yaml` in the root directory with the content auto-generated by ReadTheDocs. Also create a `docs/requirements.txt` listing the packages needed to build the documentation. It actually lists the same packages as in the optional "docs" section of the requirements listed in `pyproject.toml`. In particular, my first attempt at building the documentation failed because ReadTheDocs doesn't have the **furo** theme by default. After that, we can find the documentation here: https://rainbowprint.readthedocs.io/en/latest/

It looks the same as the one we built ourselves at https://tristancantatgaudin.github.io/rainbowprint, but ReadTheDocs will build + deploy it every time we make changes to the code (simpler than setting it up yourself with GitHub workflows) and keep track of the versioning.

## workflow for linting

https://www.freecodecamp.org/news/github-super-linter/

https://github.com/marketplace/actions/lint-action

## ssh key

To clone the repo and be able to push changes to GitHub you need to set up a valid SSH key, and provide the public key to GitHub. (see e.g. https://gist.github.com/yinzara/bbedc35798df0495a4fdd27857bca2c1). You will create a new password associated with this SSH key, it will not affect your GitHub account, only how your machine authenticates to the account. Then:

	git clone git@github.com:TristanCantatGaudin/rainbowprint.git

will allow you to push your commits. If you have multiple ssh keys, once inside the directory corresponding to that repository, do:

	git config --add --local core.sshCommand 'ssh -i /Users/myUserName/.ssh/key1_rsa'

 (or wherever your private key is located) to set the key for this particular repo.

## pypi 

tags, releases
