import importlib
import sdk.param as param

class DataRequirement:
    def __init__(self, key, annotation):
        self.key = key
        self.annotation = annotation

    def search_key(self):
        if self.annotation is not None and isinstance(self.annotation, param.uses_data_key):            
            return self.annotation.lookup_key
        return self.key