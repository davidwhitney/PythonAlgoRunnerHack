class only_requires:
    def __init__(self, *args):
        self.dependencies = args

class source_from:
    def __init__(self, lambda_function):
        self.callback = lambda_function

    def execute(self):
        return self.callback()

class uses_data_key:
    def __init__(self, lookup_key):
        self.lookup_key = lookup_key

class from_uri:
    def __init__(self, uri):
        self.uri = uri

class previous_periods:
    def __init__(self, number_of_periods):
        self.number_of_periods = number_of_periods

def check():
    print("Checking!")