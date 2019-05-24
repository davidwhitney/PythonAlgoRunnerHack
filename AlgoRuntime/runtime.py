import sys
import importlib
import inspect
import logging

import datasourcer as datasourcer
import datapersister as datapersister
import algofactory as algofactory
import pipeline as pipeline

class Runtime:
    def __init__(self):
        self.factory = algofactory.AlgoFactory()
        self.sourcer = datasourcer.DataSourcer()
        self.persister = datapersister.DataPersister()

    def execute(self):
        algo_name = self.select_algo_to_execute()        
        algo = self.factory.create_algo_proxy(algo_name)

        pipeline.Pipeline({
            "Prepare": lambda ctx: [ algo.prepare_parameters(self.sourcer.source_required_data(algo.entrypoint_arg_spec)) ],
            "Execute": lambda ctx: [ algo.execute() ],
            "Verify" : lambda ctx: [ algo.verify() ],
            "Save"   : lambda ctx: [ self.persister.store(algo.last_execution_result, ctx) ]
        }).execute()
        
        logging.info("Pipeline completed.")

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