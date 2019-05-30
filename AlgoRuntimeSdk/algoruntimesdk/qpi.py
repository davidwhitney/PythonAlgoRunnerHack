results = {
        "cell_failures": []
}

def check(description: str, verification_lambda, error_level = "FAIL"):
    print("Executing check: " + description)
    result = verification_lambda()
    results[description] = result

    if not result:
        print(f"{description} failed.")


def check_cell(cell, description: str, verification_lambda, error_level = "FAIL"):
    print("Executing check: " + description)
    result = verification_lambda(cell)

    result_wrapper = {"cell": cell, "result": result}
    results["cell_failures"].append(result_wrapper)

    if not result:
        print(f"{description} failed for cell.")