class DataSourcer:        
    def source_required_data(self, arg_spec):
        requested_data = {}
        requested_data["some_data_requirement"] = "123"
        requested_data["another_data_requirement"] = "456"
        requested_data["something_else_here"] = "789"

        return requested_data