import sys
import inspect
import datasourcer

class Runtime:
    def execute(self):
        print("Python AlgoRuntime")

        algo = self.select_algo_to_execute()
        print("Bootstrapping " + algo)

        algo_module = self.import_algo(algo)

        arg_spec = inspect.getfullargspec(algo_module.invoke).args
        sourcer = datasourcer.DataSourcer()
        arg_values = sourcer.source_required_data(arg_spec)

        algo_module.invoke(*arg_values.values())


    def select_algo_to_execute(self):
        if len(sys.argv) > 1:
            return sys.argv[1]
        return "temp_test_algo"
        
    def import_algo(self, algo):
        try:
            return __import__(algo)
        except ImportError:
            print("Could not import algorithm " + algo)
            exit -1

if __name__ == '__main__':
    Runtime().execute()