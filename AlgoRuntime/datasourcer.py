from typing import List
import logging
import importlib
param = importlib.import_module('sdk.param')

class DataSourcer:
    def __init__(self, data_providers):
        self.data_providers = data_providers

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

class HardCodedDataStrategy:
    def __init__(self, known_sources):
        self.registered_data_sources = known_sources

    def source_required_data(self, requirement):
        if requirement.search_key() in self.registered_data_sources:
            return self.registered_data_sources[requirement.search_key()]
        else:
            return None

class DataSourcedFromThisProcessStrategy:
    def source_required_data(self, requirement):
        return None

class DataSourcedFromS3Strategy:
    def source_required_data(self, requirement):
         raise Exception("S3 is not yet supported.")

class DataSourcedFromAnnotationStrategy:
    def source_required_data(self, requirement):
        if requirement.annotation is not None and isinstance(requirement.annotation, param.source_from):
            return requirement.annotation.callback()

        if requirement.annotation is not None and isinstance(requirement.annotation, param.from_uri):
            raise Exception("This attribute is not yet supported.")

        return None