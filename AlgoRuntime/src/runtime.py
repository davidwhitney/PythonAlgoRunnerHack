import sys
import importlib
import inspect
import logging

datasourcer = importlib.import_module('datasourcer')
datapersister = importlib.import_module('datapersister')
algofactory = importlib.import_module('algofactory')

class Runtime:
    def __init__(self):
        self.factory = algofactory.AlgoFactory()
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
        algo_name = self.select_algo_to_execute()        
        algo = self.factory.create_algo_proxy(algo_name)   
        arg_values = self.sourcer.source_required_data(algo.entrypoint_arg_spec)
        
        result = algo.execute(arg_values)
        algo.verify(result)

        self.persister.store(result)

    def select_algo_to_execute(self) -> str:
        algo_name = "temp_test_algo"
        if len(sys.argv) > 1:
            algo_name = sys.argv[1]
        logging.info("Bootstrapping " + algo_name)
        return algo_name

if __name__ == '__main__':    
    logging.basicConfig(filename='runtime.log', level=logging.DEBUG)
    logging.getLogger().addHandler(logging.StreamHandler())
    Runtime().execute()