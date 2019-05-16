import sys
import importlib
import inspect
import logging

class AlgoProxy:
    def __init__(self, algo_name, entrypoint, entrypoint_arg_spec, verify_method):
        self.name = algo_name
        self.entrypoint = entrypoint
        self.entrypoint_arg_spec = entrypoint_arg_spec
        self.verify_method = verify_method
        self.parameters = None

    def prepare_parameters(self, values):
        self.parameters = values

    def execute(self, arg_values = None):
        if arg_values is None:
            arg_values = self.parameters

        self.last_execution_result = self.entrypoint(*arg_values.values())
        return self.last_execution_result

    def verify(self, result = None):
        if self.verify_method is None:
            return

        if(result is None):
            result = self.last_execution_result

        self.verify_method(result)