import unittest
import importlib
import AlgoRuntime.src.datasourcer as datasourcer

class DataSourcerTest(unittest.TestCase):
    def test_source_required_data_when_key_is_not_found(self):
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

    def test_source_required_data_when_source_is_registered_many_times_first_source_wins(self):
        ds = datasourcer.DataSourcer({
                datasourcer.HardCodedDataStrategy({ "abc": "foo" }),
                datasourcer.HardCodedDataStrategy({ "abc": "bar" }),
            }) 

        result = ds.source_required_data(["abc"])

        self.assertEqual(result, {'abc': 'foo'})

if __name__ == '__main__':
    unittest.main()