# Creating a Python Algorithm Package

Our algos should be packaged as standard python pip packages.

## Pre-Requirements

To create a package, you need to install `setuptools` and `wheel`.

    > python -m pip install --user --upgrade setuptools wheel

## Creating your package

* Copy the contents of `PythonAlgoTemplate` and modify the setup.py file.
* Open a terminal / prompt inside your new directory

	> python setup.py sdist bdist_wheel

An archive will be created in dist/*.tar.gz - this is your pip archive.

The runtime will pull, install, and execute your code from this package.