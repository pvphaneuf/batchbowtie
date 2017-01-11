import unittest
import os
from batchbowtie import _get_ref_seq_file_list
from batchbowtie import _get_index_name

class Tests(unittest.TestCase):

    def test_get_ref_seq_file_list_duplicate_entry(self):
        curr_path = os.path.dirname(__file__)
        ref_seq_file_list = _get_ref_seq_file_list(curr_path + "/test_to_qc.csv")
        expected = ["1.fa", "2.fa"]
        self.assertEquals(ref_seq_file_list, expected)

    def test_get_index_name(self):
        ref_seq_file = "nc000913.fa"
        returned = _get_index_name(ref_seq_file)
        expected = "nc000913"
        self.assertEquals(returned, expected)