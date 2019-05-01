from typing import List

class DataSourcer:
    def __init__(self, known_sources, fallback_data_source = None):
        self.registered_data_sources = known_sources
        self.fallback = fallback_data_source or self.throw_error

    def source_required_data(self, registered_data_sources: List[str]):
        if not type(registered_data_sources) is list:
            raise Exception("Parameter 'registered_data_sources' was expected to be a list of strings.")

        requested_data = {}

        for key in registered_data_sources:
            print("Sourcing data for " + key)

            if key in self.registered_data_sources:
                data_for = self.registered_data_sources[key]
            else:
                data_for = self.fallback      

            requested_data[key] = data_for(key)

        return requested_data

    def throw_error(self, key):
        raise Exception("No registered data source for " + key + " exists. This is either a typo or you're trying to get data we cannot source.")

class HardCodedDataStrategy:
    def __init__(self, known_sources):
        self.registered_data_sources = known_sources
        self.fallback = self.throw_error

    def source_required_data(self, key):
        print("Sourcing data for " + key)
        if key in self.registered_data_sources:
            data_for = self.registered_data_sources[key]
        else:
            data_for = self.fallback 

        return data_for(key)
        
    def throw_error(self, key):
        raise Exception("No registered data source for " + key + " exists. This is either a typo or you're trying to get data we cannot source.")


class DataSourcedFromThisProcessStrategy:
    def source_required_data(self, key):
        return None

class DataSourcedFromS3Strategy:
    def source_required_data(self, key):
        return None      
