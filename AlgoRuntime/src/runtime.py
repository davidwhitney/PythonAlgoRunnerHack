import sys
import importlib
import inspect
datasourcer = importlib.import_module('datasourcer')

class Runtime:
    def execute(self):
        algo = self.select_algo_to_execute()
        print("Bootstrapping " + algo)

        algo_module = self.import_algo(algo)
        entrypoint = self.select_entrypoint(algo_module)
        arg_spec = inspect.getfullargspec(entrypoint).args

        sourcer = self.configure_datasourcer()
        arg_values = sourcer.source_required_data(arg_spec)

        result = entrypoint(*arg_values.values())

    def select_algo_to_execute(self) -> str:
        if len(sys.argv) > 1:
            return sys.argv[1]
        return "temp_test_algo"

    def select_entrypoint(self, algo_module):
        supported_entrypoints = ["invoke", "run", "execute", "start", "main", "train"]
        discovered_entrypoints = list(filter(lambda name: hasattr(algo_module, name), supported_entrypoints))
        selected_entrypoint = next(iter(discovered_entrypoints), None)
        return getattr(algo_module, selected_entrypoint)

    def configure_datasourcer(self):
        return datasourcer.DataSourcer({
            datasourcer.HardCodedDataStrategy({
                "some_data_requirement": "foo",
                "another_data_requirement": "bar",
                "something_else_here": "baz",
            }),
            datasourcer.DataSourcedFromThisProcessStrategy(),
            datasourcer.DataSourcedFromS3Strategy()
        })
        
    def import_algo(self, algo: str):
        try:
            return __import__(algo)
        except ImportError:
            print("Could not import algorithm " + algo)
            exit -1

if __name__ == '__main__':
    Runtime().execute()