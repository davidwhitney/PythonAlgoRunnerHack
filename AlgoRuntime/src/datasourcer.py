class DataSourcer:
    def __init__(self):
        self.registered_data_sources = {
              "some_data_requirement": self.load_some_data_requirement,
              "another_data_requirement": self.load_some_data_requirement,
              "something_else_here": self.load_some_data_requirement,
          }

    def source_required_data(self, arg_spec):
        requested_data = {}

        # This is not a real implementation - I imagine we'd look-up S3 buckets or table keys or something here
        # Ideally something that we can run a list operation on, so when people request things that aren't
        # in our data sources, we can throw an error with a list of *actual* data sources available.

        for key in arg_spec:
            print("Sourcing data for " + key)

            if key not in self.registered_data_sources:
                raise Exception("No registered data source for " + key + " exists. This is either a typo or you're trying to get data we cannot source.")

            factory = self.registered_data_sources[key]
            value = factory()
            requested_data[key] = value

        return requested_data

    def load_some_data_requirement(self):
        return "1234"