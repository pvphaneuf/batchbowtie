#!/usr/bin/python
import csv
import subprocess


CSV_FILE = "to_qc.csv"
INDEX_BUILDER = "bowtie2-build"
ALIGNER = "bowtie2"
REF_SEQ_INDEX = 0
READ_1_INDEX = 1
READ_2_INDEX = 2
REF_SEQ_FLAG = "-x"
READ_1_FLAG = "-1"
READ_2_FLAG = "-2"
OUTPUT_FILE_FLAG = "-S"
OUTPUT_FILE_PREFIX = "output"
OUTPUT_FILE_EXT = ".sam"


def main():
    _build_indexes()
    _align_reads()
    #_clean_up()


def _align_reads():
    with open(CSV_FILE) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        output_file_count = 0
        for row in csv_reader:
            index_name = _get_substr_before('.', row[REF_SEQ_INDEX])
            bowtie_cmd_list = [ALIGNER, REF_SEQ_FLAG, index_name,
                               READ_1_FLAG, row[READ_1_INDEX],
                               READ_2_FLAG, row[READ_2_INDEX],
                               OUTPUT_FILE_FLAG, OUTPUT_FILE_PREFIX+str(output_file_count)+OUTPUT_FILE_EXT]
            subprocess.run(bowtie_cmd_list)
            output_file_count += 1


def _build_indexes():
    ref_seq_file_list = _get_ref_seq_file_list(CSV_FILE)
    index_builder_cmd_list = [INDEX_BUILDER]
    for ref_seq_file in ref_seq_file_list:
        index_builder_cmd_list.append(ref_seq_file)
        index_builder_cmd_list.append(_get_substr_before('.', ref_seq_file))
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


def _get_substr_before(delimiter, file_name):
    pos = file_name.find(delimiter)
    if pos == -1: return file_name
    return file_name[0:pos]


if __name__ == '__main__':
    main()