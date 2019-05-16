from typing import List
import logging

class DataSourcer:
    def __init__(self, data_providers):
        self.data_providers = data_providers

    def source_required_data(self, registered_data_sources: List[str]):
        if not type(registered_data_sources) is list:
            raise Exception("Parameter 'registered_data_sources' was expected to be a list of strings.")

        requested_data = {}

        for key in registered_data_sources:
            print("Searching for '" + key + "' in data providers.")

            for provider in self.data_providers:
                any_data = provider.source_required_data(key)
                if any_data is not None:
                    logging.info("Sourced data for '" + key + "' from " + provider.__class__.__name__)
                    requested_data[key] = any_data
                    break

            if requested_data[key] is None:
                raise Exception("No registered data source that can provide '" + key + "' exists. This is either a typo or you're trying to get data we cannot source.")

        return requested_data        

class HardCodedDataStrategy:
    def __init__(self, known_sources):
        self.registered_data_sources = known_sources

    def source_required_data(self, key):
        if key in self.registered_data_sources:
            return self.registered_data_sources[key]
        else:
            return None

class DataSourcedFromThisProcessStrategy:
    def source_required_data(self, key):
        return None

class DataSourcedFromS3Strategy:
    def source_required_data(self, key):
        return None