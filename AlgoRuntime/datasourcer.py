from typing import List
import logging
import importlib
param = importlib.import_module('sdk.param')

import datasources.annotations as annotations
import datasources.hardcoded as hardcoded
import datasources.s3bucket as s3bucket
import datasources.thisprocess as thisprocess

class DataSourcer:
    def __init__(self, data_providers = None):
        self.data_providers = data_providers or default_configuration()

    def source_required_data(self, data_requirements):
        if not type(data_requirements) is dict:
            raise Exception("Parameter 'data_requirements' was expected to be a list of strings.")

        requested_data = {}

        for key, annotation in data_requirements.items():
            logging.debug(f"Searching for '{key}' in data providers.")
            requirement = DataRequirement(key, annotation)
                                    
            for provider in self.data_providers:
                any_data = provider.source_required_data(requirement)
                if any_data is not None:
                    logging.info(f"Sourced data for '{key}' from {provider.__class__.__name__}")
                    requested_data[key] = any_data
                    break

            if requested_data[key] is None:
                raise Exception(f"No registered data source that can provide '{key}' exists. This is either a typo or you're trying to get data we cannot source.")

        return requested_data        

class DataRequirement:
    def __init__(self, key, annotation):
        self.key = key
        self.annotation = annotation

    def search_key(self):
        if self.annotation is not None and isinstance(self.annotation, param.uses_data_key):            
            return self.annotation.lookup_key
        return self.key



def default_configuration():
    return [
        thisprocess.DataSourcedFromThisProcessStrategy(),
        annotations.DataSourcedFromAnnotationStrategy(),
        hardcoded.HardCodedDataStrategy({
            "some_data_requirement": "foo",
            "another_data_requirement": "bar",
            "something_else_here": "baz",
        }),
        s3bucket.DataSourcedFromS3Strategy()
    ]
