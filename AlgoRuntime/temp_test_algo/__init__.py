def invoke( some_data_requirement, 
            another_data_requirement,
            something_else_here
        ):        
    if some_data_requirement is None:
        raise Exception("Noo!")

    qpis = {}

    print("Inside the algo here")
    print(some_data_requirement)
    print(another_data_requirement)
    print(something_else_here)

    qpis["number_of_args"] = 4

    return {
        "__qpis": qpis,
        "first_dataframe": [ 1, 2, 3 ],
        "second_datafarme": None
    }


# Example of using attributes to support extra binding scenarios

import importlib
param = importlib.import_module('sdk.param', '../sdk/param.py')

def invoke_with_annotation_support( 
            some_data_requirement: param.only_requires("field1", "field2"), 
            another_data_requirement: param.source_from(lambda: 123),
            something_else_here: param.uses_data_key("some_other_key"),
            totally_random_thing: param.from_uri("http://some/s3/uri"),
            temp_test_algo: param.previous_periods(5)
        ):

    print("Inside the algo here")
    print(some_data_requirement)
    print(another_data_requirement)
    print(something_else_here)    
