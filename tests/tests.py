import unittest
import os
from batchbowtie import get_ref_seq_file_list

class Tests(unittest.TestCase):

    def test_get_ref_seq_file_list_duplicate_entry(self):
        curr_path = os.path.dirname(__file__)
        ref_seq_file_list = get_ref_seq_file_list(curr_path+"/test_to_qc.csv")
        expected = ["1.fa", "2.fa"]
        self.assertEquals(ref_seq_file_list, expected)