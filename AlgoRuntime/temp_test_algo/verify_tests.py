import unittest
import verify as verify

class VerifyTest(unittest.TestCase):    
    def my_qpi_works(self):
        results = verify.verify({
            "__qpis": {
                "number_of_args": 4
            }
        })

        self.assertNotNull(results)
    
if __name__ == '__main__':
    unittest.main()