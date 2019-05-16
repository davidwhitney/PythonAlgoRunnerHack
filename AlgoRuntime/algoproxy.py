import sys
import importlib
import inspect

class AlgoProxy:
    def __init__(self, algo_name, entrypoint, entrypoint_arg_spec, verify_method):
        self.name = algo_name
        self.entrypoint = entrypoint
        self.entrypoint_arg_spec = entrypoint_arg_spec
        self.verify_method = verify_method

    def execute(self, arg_values):
        self.entrypoint(*arg_values.values())

    def verify(self, result):
        if self.verify_method is None:
            return        
        self.verify_method(result)