import sys
import importlib
import inspect
datasourcer = importlib.import_module('datasourcer')
datapersister = importlib.import_module('datapersister')

class Runtime:
    def __init__(self):
        self.sourcer = datasourcer.DataSourcer({
            datasourcer.DataSourcedFromThisProcessStrategy(),
            datasourcer.HardCodedDataStrategy({
                "some_data_requirement": "foo",
                "another_data_requirement": "bar",
                "something_else_here": "baz",
            }),
            datasourcer.DataSourcedFromS3Strategy()
        })
        self.persister = datapersister.DataPersister()

    def execute(self):
        algo = self.select_algo_to_execute()
        algo_module = self.import_algo(algo)

        entrypoint = self.select_entrypoint(algo_module)
        arg_spec = inspect.getfullargspec(entrypoint).args
        arg_values = self.sourcer.source_required_data(arg_spec)

        result = entrypoint(*arg_values.values())
        self.persister.store(result)

    def select_algo_to_execute(self) -> str:
        algo = "temp_test_algo"
        if len(sys.argv) > 1:
            algo = sys.argv[1]
        print("Bootstrapping " + algo)
        return algo
        
    def select_entrypoint(self, algo_module):
        supported_entrypoints = ["invoke", "run", "execute", "start", "main", "train"]
        discovered_entrypoints = list(filter(lambda name: hasattr(algo_module, name), supported_entrypoints))
        selected_entrypoint = next(iter(discovered_entrypoints), None)
        return getattr(algo_module, selected_entrypoint)
        
    def import_algo(self, algo: str):
        try:
            return __import__(algo)
        except ImportError:
            print("Could not import algorithm " + algo)
            exit -1

if __name__ == '__main__':
    Runtime().execute()