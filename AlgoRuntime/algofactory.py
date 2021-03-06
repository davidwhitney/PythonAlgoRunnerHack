import sys
import importlib
import inspect
import logging
import algoproxy as algoproxy

class AlgoFactory:
    def __init__(self, conventions = None):
        self.conventions = conventions or default_configuration()

    def create_algo_proxy(self, algo_name):
        logging.debug(f"Generating a proxy to module: '{algo_name}'.")

        algo_module = self.__import_algo(algo_name)

        entrypoint = self.__select_entrypoint(algo_module)        
        entrypoint_args = self.__generate_parameter_table(entrypoint)
        verify_method = self.__find_verification_function(algo_name)

        return algoproxy.AlgoProxy(algo_name, entrypoint, entrypoint_args, verify_method)
    
    def __select_entrypoint(self, algo_module):
        supported_entrypoints = self.conventions["supported_entrypoints"]
        discovered_entrypoints = list(filter(lambda name: hasattr(algo_module, name), supported_entrypoints))
        selected_entrypoint = next(iter(discovered_entrypoints), None)
        
        logging.debug(f"Found module entry point '{selected_entrypoint}'.")
        return getattr(algo_module, selected_entrypoint)

    def __import_algo(self, algo: str):
        try:
            return __import__(algo)
        except ImportError:
            logging.critical("Could not import algorithm " + algo)
            exit -1

    def __generate_parameter_table(self, entrypoint):
        entrypoint_args = {}
        for arg in inspect.getfullargspec(entrypoint).args:
            entrypoint_args[arg] = None

            if arg in entrypoint.__annotations__:
                logging.debug(f"Found annotation for {arg}")
                entrypoint_args[arg] = entrypoint.__annotations__[arg]
        
        return entrypoint_args
    
    def __find_verification_function(self, algo):
        try:      
            verify_filename = self.conventions["verify_filename"];
            import_path = f"{algo}.{verify_filename}"
            logging.debug(f"Attempting to import verification function: '{import_path}'...")
            return getattr(importlib.import_module(import_path), self.conventions["verify_function"])
        except ImportError:
            logging.info("Skipping verification. No verify.py file found in package.")
        except AttributeError:
            logging.info("Skipping verification. No 'def verify(algo_output)' function found in verify.py.")


def default_configuration():
    return {
        "supported_entrypoints": ["invoke", "run", "execute", "start", "main", "train"],
        "verify_filename": "verify",
        "verify_function": "verify"
    }