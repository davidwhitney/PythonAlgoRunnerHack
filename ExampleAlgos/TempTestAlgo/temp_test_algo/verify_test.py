import unittest
import importlib
import verify as verify

class VerifyTest(unittest.TestCase): 

    def test_can_check_a_qpi_value(self):
        algo_result = {
            "__qpis": {
                "number_of_args": 4
            },
            "first_dataframe": []
        }
        
        results = verify.verify(algo_result)

        self.assertIsNotNone(results)

    def test_something_is_less_than_one_fails(self):
        algo_result = {
            "__qpis": {
                "number_of_args": 4
            },
            "first_dataframe": [
                { "something": 0 }
            ]
        }
        
        results = verify.verify(algo_result)

        self.assertIsNotNone(results)
    
if __name__ == '__main__':
    unittest.main()