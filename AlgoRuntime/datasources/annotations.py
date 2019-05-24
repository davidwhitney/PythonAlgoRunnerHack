class DataSourcedFromAnnotationStrategy:
    def source_required_data(self, requirement):
        if requirement.annotation is not None and isinstance(requirement.annotation, param.source_from):
            return requirement.annotation.callback()

        if requirement.annotation is not None and isinstance(requirement.annotation, param.from_uri):
            raise Exception("This attribute is not yet supported.")

        return None