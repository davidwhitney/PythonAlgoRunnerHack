class source_from:
    def __init__(self, lambda_function):
        self.callback = lambda_function

    def execute(self):
        return self.callback()