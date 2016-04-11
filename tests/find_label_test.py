import unittest

from src.find_label import extract_label
from src.find_label import read_file


class TestFindLabel(unittest.TestCase):
    def setUp(self):
        pass

    def test_read_file(self):
        content = read_file("/Users/tzhou/workspace/ci-job-configs/.test/output/aurora-admin-7-release")
        self.assertTrue('assignedNode' in content)
        self.assertTrue('<project>' in content)

    def test_extract_label_whenNormal_returnLabelBetweenAssignedNodeTag(self):
        label = extract_label("<assignedNode>abc</assignedNode>")
        self.assertEqual('abc', label)

    def test_extract_label_whenNormal_returnLabelBetweenAssignedNodeTag2(self):
        label = extract_label("<assignedNode>abc2</assignedNode>")
        self.assertEqual('abc2', label)

    def test_extract_label_whenNormal_returnLabelBetweenAssignedNodeTag3(self):
        label = extract_label("<project><assignedNode>abc</assignedNode></project>")
        self.assertEqual('abc', label)

    def test_extract_label_whenEmpty_returnEmptyString(self):
        label = extract_label("<project><assignedNode></assignedNode></project>")
        self.assertEqual('', label)

    def test_extract_label_whenNoAssignedNodeTags_returnEmptyString(self):
        label = extract_label("<project></project>")
        self.assertEqual('', label)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
