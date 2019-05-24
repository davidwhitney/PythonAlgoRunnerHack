class HardCodedDataStrategy:
    def __init__(self, known_sources):
        self.registered_data_sources = known_sources

    def source_required_data(self, requirement):
        if requirement.search_key() in self.registered_data_sources:
            return self.registered_data_sources[requirement.search_key()]
        else:
            return None
