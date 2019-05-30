def invoke( some_data_requirement, 
            another_data_requirement,
            something_else_here
        ):        
    if some_data_requirement is None:
        raise Exception("I need some_data_requirement to run!")

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