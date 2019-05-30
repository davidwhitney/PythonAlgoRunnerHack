# Algorithm Runtime SDK

The Algorithm Runtime SDK is the data-science-user facing library that you can use to help override the `Algorithm Runtime Conventions` and author automatically executed `QPIs`

# Contents
* Using Annotations
    * Supported Annotations
* Authoring QPIs

# Using Annotations

The annotation API provides hints for data resoultion in your algorithms, they look like this example:

```python
import importlib
param = importlib.import_module("algoruntimesdk")

def invoke_with_annotation_support( 
            some_data_requirement: param.annotation_name("annotation param"),
        ):

    # Algorithm code here  

```

# Supported Annotations

## only_requires

    some_data_requirement: param.only_requires("field1", "field2")

Hints to the data sourcing code that you only require specific fields at runtime from a data source.

* This parameter will be filled with the suggested data.
* It **may** contain additional data.

---

## source_from

    another_data_requirement: param.source_from(lambda: 123)

Forces the data loader to invoke this function callback to source data.

* Useful for extending the runtime, or sourcing data from unsupported locations

---

## uses_data_key

    something_else_here: param.uses_data_key("some_other_key")

Overrides the naming convention detection, so in this example, instead of using the key `something_else_here`, the data sourcer will use `some_other_key` to source the value of the parameter.

---

## from_uri

    totally_random_thing: param.from_uri("http://some/s3/uri")

Not yet supported - placeholder.

---

## from_uri

    temp_test_algo: param.previous_periods(5)

Not yet supported - placeholder.

When an algorithm requires the results of it's own previous execution, it can request them using previous_periods

* Parameter is number of previous periods
* Data supplied as a list of dataframes + associated stored QPIs.


# Authoring QPIs

By convention, adding a file called `verify.py` with a function called `verify(results)` to your published package will result in the `Algorithm Runtime` executing your verify function after your code has run.

The `runtime` will pass in as a method parameter, the returned object from your algorithm, as the input parameter of your verify function.

An example `verify.py` file might look like this:

```python
import importlib
qpic = importlib.import_module("algoruntimesdk")

def verify(results):
    qpic.check(
        "Should have four arguments",
        lambda: results["__qpis"]["number_of_args"] == 4, 
        "FATAL"
    )

    for cell in results["dataframe1"]:
        if cell["something"] > 1: qpic.warn("Oh no, greater than 1!", cell)

    return qpic.results
```