results = {}

def check(description: str, verification_lambda, error_level = Result.FAIL):
    print("Executing check: " + description)
    result = verification_lambda()
    results[description] = result

    if not result:
        print(f"{description} failed.")