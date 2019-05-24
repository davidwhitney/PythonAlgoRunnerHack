import unittest
import importlib
import datasourcedfromannotationstrategy as annotations
import datarequirement as datarequirement

class DataSourcedFromAnnotationStrategyTest(unittest.TestCase):
    def setUp(self):
        self.sut = annotations.DataSourcedFromAnnotationStrategy()

    def test_source_required_data_no_annotation_present_returns_none(self):        
        value = self.sut.source_required_data(datarequirement.DataRequirement("something", None))
        
        self.assertIsNone(value)

if __name__ == '__main__':
    unittest.main()