import unittest
import os
from batchbowtie import _get_ref_seq_file_list
from batchbowtie import _get_substr_before
from batchbowtie import _get_overall_alignment_rate

class Tests(unittest.TestCase):

    def test_get_ref_seq_file_list_duplicate_entry(self):
        curr_path = os.path.dirname(__file__)
        ref_seq_file_list = _get_ref_seq_file_list(curr_path + "/test_to_qc.csv")
        expected = ["1.fa", "2.fa"]
        self.assertEquals(ref_seq_file_list, expected)

    def test_get_index_name(self):
        ref_seq_file = "nc000913.fa"
        returned = _get_substr_before('.', ref_seq_file)
        expected = "nc000913"
        self.assertEquals(returned, expected)

    def test_get_overall_alignment_rate(self):
        stdout_str = "b'20 reads; of these:\\n  20 (100.00%) were paired; of these:\\n    3 (15.00%) aligned concordantly 0 times\\n    17 (85.00%) aligned concordantly exactly 1 time\\n    0 (0.00%) aligned concordantly >1 times\\n    ----\\n    3 pairs aligned concordantly 0 times; of these:\\n      0 (0.00%) aligned discordantly 1 time\\n    ----\\n    3 pairs aligned 0 times concordantly or discordantly; of these:\\n      6 mates make up the pairs; of these:\\n        6 (100.00%) aligned 0 times\\n        0 (0.00%) aligned exactly 1 time\\n        0 (0.00%) aligned >1 times\\n85.00% overall alignment rate\\n"
        returned = _get_overall_alignment_rate(stdout_str)
        expected = "85.00% overall alignment rate"
        self.assertEquals(returned, expected)