#!/usr/bin/python
import csv
import subprocess


CSV_FILE = "to_qc.csv"
INDEX_BUILDER = "bowtie2-build"


def main():
    ref_seq_file_list = []
    with open(CSV_FILE) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            ref_seq_file_list.append(row[0])
    index_builder_cmd_list = [INDEX_BUILDER]
    for ref_seq_file in ref_seq_file_list:
        index_builder_cmd_list.append(ref_seq_file)
        index_builder_cmd_list.append(_get_index_name(ref_seq_file))
        subprocess.run(index_builder_cmd_list)


def _get_index_name(ref_seq_file):
    pos = ref_seq_file.find('.')
    if pos == -1: return ""
    return ref_seq_file[0:pos]


if __name__ == '__main__':
    main()