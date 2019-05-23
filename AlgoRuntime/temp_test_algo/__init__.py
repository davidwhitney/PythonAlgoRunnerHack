def invoke( some_data_requirement, 
            another_data_requirement,
            something_else_here
        ):

    print("Inside the algo here")
    print(some_data_requirement)
    print(another_data_requirement)
    print(something_else_here)  


# Example of using attributes to support extra binding scenarios

import importlib
param = importlib.import_module('sdk.param', '../sdk/param.py')

def invoke_with_annotation_support( 
            some_data_requirement: param.only_requires("field1", "field2"), 
            another_data_requirement: param.source_from(lambda: 123),
            something_else_here: param.uses_data_key("some_other_key"),
            totally_random_thing: param.from_uri("http://some/s3/uri")
        ):

    print("Inside the algo here")
    print(some_data_requirement)
    print(another_data_requirement)
    print(something_else_here)    
