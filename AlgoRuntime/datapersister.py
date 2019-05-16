import logging

class DataPersister:
    def store(self, results, pipeline_execution_context):
        logging.info("Storing data...")