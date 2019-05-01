import unittest
import importlib
import AlgoRuntime.src.datasourcer as datasourcer

class DataSourcerTest(unittest.TestCase):
    def test_source_required_data_when_param_provided_is_not_a_list_throws(self):
        ds = datasourcer.DataSourcer({
                datasourcer.HardCodedDataStrategy({})
            })

        with self.assertRaises(Exception):
            ds.source_required_data("abc")

    def test_source_required_data_when_source_is_registered_sources_data_correctly(self):
        ds = datasourcer.DataSourcer({
                datasourcer.HardCodedDataStrategy({ "abc": "foo" }),
                datasourcer.DataSourcedFromThisProcessStrategy(),
                datasourcer.DataSourcedFromS3Strategy(),
            }) 

        result = ds.source_required_data(["abc"])

        self.assertEqual(result, {'abc': 'foo'})

if __name__ == '__main__':
    unittest.main()