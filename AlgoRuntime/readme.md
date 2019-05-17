# AlgoRuntime

This is the Aaas runtime wrapper that will invoke data science algorithms.
It's designed to run inside a container, or be submitted to a spark cluster.

It's responsible for sourcing requested data, executing and instrumenting algorithms, and persisting the outputs.

* Anatomy of a package
* Supported Entrypoint conventions
* Expected outputs
* Dependency management
* Verification and QPIs

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

## Supported Entrypoint conventions

By default, we'll install your package and attempt to find any of the following methods, in this order:

* "invoke"
* "run"
* "execute"
* "start"
* "main"
* "train"

Declare any dependencies on data as constructor parameters.

```python
def invoke( some_data_requirement, 
            another_data_requirement,
            something_else_here
        ):

    print("Inside the algo here")
    print(some_data_requirement)
    print(another_data_requirement)
    print(something_else_here)
```

We'll use the function parameter names to infer the location of dependant data by convention - as a result, your parameter names need to exactly match the dependent data names.
For example:

| Algo name    | Insight Name                    | parameter name       |
|--------------|---------------------------------|----------------------|
| my_cool_algo | Single returned Insight         | my_cool_algo         |
| my_cool_algo | Named returned Insight "foo"    | my_cool_algo__foo    |

Note the `double underscore` `_ _` in the named insight example.

We support the following additional injected components and properties:

* context - runtime context, including invocation parameters
* TBC

## Expected outputs

Your entrypoint should return one of two data structures, either:

* A single data frame
* A dictionary, with named data frames

In the case of a single data frame, we'll store this as the default output of your algorithm.
When you return a dictionary, we'll store each output distinctly, using the named key.

## Dependency management

Package dependencies should be listed in requirements.txt
Pip will be used to restore these dependencies into the runtime environment.

## Verification and QPIs

Providing a verify.py file with a single function

```python
def verify(algo_results):
    # Verification tests here
```

Is our hook for algorithm result verification.
We'll execute this function if we find it after your algorithm runs.