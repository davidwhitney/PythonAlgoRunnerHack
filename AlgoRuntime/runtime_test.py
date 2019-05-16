import unittest
import importlib
import runtime as runtime

class RuntimeTest(unittest.TestCase):
    def test_can_init(self):
        rt = runtime.Runtime()
        self.assertIsNotNone(rt)

if __name__ == '__main__':
    unittest.main()