import sys
import argparse


class Parser:
    pass  # TODO command linethrough argparse


class Reader:
    def __init__(self, scaffolds_file, kmers_file):
        self.scaffolds = self.read_scaffolds(scaffolds_file)
        self.kmers = self.read_kmers(kmers_file)
        self.kmer_size = ...

    @staticmethod
    def read_scaffolds(scaffolds) -> dict:
        with open(scaffolds) as f_read:
            scaffolds_dict = {}

            sequence_name = f_read.readline().strip()
            current_sequence = []

            for line in f_read:
                if line.startswith('>'):
                    current_sequence = ''.join(current_sequence)
                    scaffolds_dict[sequence_name] = current_sequence
                    sequence_name = line.strip()
                    current_sequence = []
                else:
                    current_sequence.append(line.strip())
        return scaffolds_dict

    @staticmethod
    def read_kmers(kmers) -> set:
        with open(kmers) as f_read:
            kmers_set = set()
            for line in f_read:
                kmers_set.add(line.split()[0])
        return kmers_set

    def _sort_scaffolds_by_length(self):
        """
        sort in descending order
        """
        return sorted(self.scaffolds.items(), key=lambda x: -len(x[1]))

    def filter_nonunique_reads(self):
        kmers_copied = self.kmers.copy()
        filtered_scaffolds = set()

        for scaffold_name, scaffold_sequence in self._sort_scaffolds_by_length():
            if kmers_copied:
                # TODO make proper index for kmers