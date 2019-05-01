import sys
import importlib
import inspect
datasourcer = importlib.import_module('datasourcer')

class Runtime:
    def execute(self):
        algo = self.select_algo_to_execute()
        print("Bootstrapping " + algo)

        algo_module = self.import_algo(algo)
        arg_spec = inspect.getfullargspec(algo_module.invoke).args

        sourcer = datasourcer.DataSourcer({
            datasourcer.HardCodedDataStrategy({
                "some_data_requirement": "foo",
                "another_data_requirement": "bar",
                "something_else_here": "baz",
            }),
            datasourcer.DataSourcedFromThisProcessStrategy(),
            datasourcer.DataSourcedFromS3Strategy()
        })

        arg_values = sourcer.source_required_data(arg_spec)
        algo_module.invoke(*arg_values.values())

    def select_algo_to_execute(self) -> str:
        if len(sys.argv) > 1:
            return sys.argv[1]
        return "temp_test_algo"

    def source_unregistered_data(self, key):
        return "nothing here for " + key
        
    def import_algo(self, algo: str):
        try:
            return __import__(algo)
        except ImportError:
            print("Could not import algorithm " + algo)
            exit -1

if __name__ == '__main__':
    Runtime().execute()