import sys
import importlib
import inspect
algoproxy = importlib.import_module('algoproxy')

class AlgoFactory:
    def create_algo_proxy(self, algo_name):        
        algo_module = self.__import_algo(algo_name)

        entrypoint = self.__select_entrypoint(algo_module)
        entrypoint_arg_spec = inspect.getfullargspec(entrypoint).args

        verify_method = self.__find_verification_function(algo_name)
        return algoproxy.AlgoProxy(algo_name, entrypoint, entrypoint_arg_spec, verify_method)
    
    def __select_entrypoint(self, algo_module):
        supported_entrypoints = ["invoke", "run", "execute", "start", "main", "train"]
        discovered_entrypoints = list(filter(lambda name: hasattr(algo_module, name), supported_entrypoints))
        selected_entrypoint = next(iter(discovered_entrypoints), None)
        return getattr(algo_module, selected_entrypoint)

    def __import_algo(self, algo: str):
        try:
            return __import__(algo)
        except ImportError:
            print("Could not import algorithm " + algo)
            exit -1
    
    def __find_verification_function(self, algo):
        try:        
            return self.import_from(algo + ".verify", "verify")            
        except ImportError:
            print("Skipping verification. No verify.py file found in package.")
        except AttributeError:
            print("Skipping verification. No 'def verifly(algo_output)' function found in verify.py.")

    def __import_from(self, module, name):
        module = __import__(module, fromlist=[name])
        return getattr(module, name)

