import importlib
qpic = importlib.import_module('sdk.assert', '../sdk/assert.py')

def verify(results):
    qpic.check(
        "Should have four arguments",
        lambda: results["__qpis"]["number_of_args"] == 4, 
        "FATAL"
    )

    for cell in results["dataframe1"]:
        if cell["something"] > 1: qpic.warn("Oh no, greater than 1!", cell)

    return qpic.results