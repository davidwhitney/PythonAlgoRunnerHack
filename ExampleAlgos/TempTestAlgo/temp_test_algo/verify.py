import importlib
from algoruntimesdk import qpi

def verify(results):
    
    qpi.check(
        "Should have four arguments",
        lambda: results["__qpis"]["number_of_args"] == 4, 
        "FATAL"
    )

    for cell in results["first_dataframe"]:
        qpi.check_cell(cell, "Something must be >= 1", lambda c: c["something"] >= 1)

    return qpi.results


if __name__ == '__main__':
    verify(None)