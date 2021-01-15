from simple_example import some_function
import unittest

class TestMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(some_function(True), True)


if __name__ == '__main__':
    unittest.main()