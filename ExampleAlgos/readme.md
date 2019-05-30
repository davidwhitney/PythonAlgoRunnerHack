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

## Anatomy of a package

Our packages require a few mandatory things to make them work.

'''
    /setup.py
    /README.md
    /algo_name
    /algo_name/__init__.py
    /algo_name/requirements.txt
    /algo_name/verify.py
'''

* __init__.py - The package entrypoint
* requirements.txt - List of requirements to be restored by pip during build process
* verify.py - Support for verification / QPIs

See the README.md for the Algorithm Runtime for more detailed explainations of how our supported conventions.