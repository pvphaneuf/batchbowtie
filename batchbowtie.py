#!/usr/bin/python
import csv
import subprocess


CSV_FILE = "to_qc.csv"
INDEX_BUILDER = "bowtie2-build"
REF_SEQ_INDEX = 0


def main():
    ref_seq_file_list = _get_ref_seq_file_list(CSV_FILE)
    index_builder_cmd_list = [INDEX_BUILDER]
    for ref_seq_file in ref_seq_file_list:
        index_builder_cmd_list.append(ref_seq_file)
        index_builder_cmd_list.append(_get_index_name(ref_seq_file))
        subprocess.run(index_builder_cmd_list)


def _get_ref_seq_file_list(csv_file_name):
    ref_seq_file_list = []
    with open(csv_file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            ref_seq_file = row[REF_SEQ_INDEX]
            if ref_seq_file not in ref_seq_file_list:
                ref_seq_file_list.append(ref_seq_file)
    return ref_seq_file_list


def _get_index_name(ref_seq_file):
    pos = ref_seq_file.find('.')
    if pos == -1: return ""
    return ref_seq_file[0:pos]


if __name__ == '__main__':
    main()