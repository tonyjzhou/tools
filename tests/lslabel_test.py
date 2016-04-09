import unittest

from src import lslabel


class TestLslabel(unittest.TestCase):
    def setUp(self):
        pass

    def test_read_file(self):
        content = lslabel.read_file("/Users/tzhou/workspace/ci-job-configs/.test/output/aurora-admin-7-release")
        self.assertTrue('assignedNode' in content)
        self.assertTrue('<project>' in content)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
