import unittest

from src import lslabel


class TestLslabel(unittest.TestCase):
    def setUp(self):
        pass

    def test_read_file(self):
        content = lslabel.read_file("filename")
        self.assertEqual('assignedNode' in content)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
