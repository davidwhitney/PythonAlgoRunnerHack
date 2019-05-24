import unittest
import importlib
import algofactory as algofactory

class AlgoFactoryTest(unittest.TestCase):
    def setUp(self):
        self.test_algo = "temp_test_algo"
        self.sut = algofactory.AlgoFactory({
            "supported_entrypoints": ["invoke", "run", "execute", "start", "main", "train"],
            "verify_filename": "verify",
            "verify_function": "verify"
        })

    def test_create_algo_proxy_algo_doesnt_exist_throws(self):        
        with self.assertRaises(Exception):
            self.sut.create_algo_proxy("garbage here")

    def test_create_algo_proxy_algo_exists_returns_proxy(self):
        proxy = self.sut.create_algo_proxy(self.test_algo)
        
        self.assertIsNotNone(proxy)

    def test_create_algo_proxy_algo_exists_creates_reference_to_entry_point(self):
        proxy = self.sut.create_algo_proxy(self.test_algo)
        
        self.assertIsNotNone(proxy.entrypoint)
        self.assertIsNotNone(proxy.entrypoint_arg_spec)

    def test_create_algo_proxy_verify_file_exists_contains_reference_to_verify(self):
        proxy = self.sut.create_algo_proxy(self.test_algo)
        
        self.assertIsNotNone(proxy.verify_method)

if __name__ == '__main__':
    unittest.main()