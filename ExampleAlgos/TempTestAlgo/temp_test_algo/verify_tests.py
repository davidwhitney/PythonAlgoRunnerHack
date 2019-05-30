import unittest
import importlib
verify = importlib.import_module("verify")

class VerifyTest(unittest.TestCase): 

    def my_qpi_works(self):
        results = verify.verify({
            "__qpis": {
                "number_of_args": 4
            }
        })

        self.assertIsNotNone(results)
    
if __name__ == '__main__':
    unittest.main()