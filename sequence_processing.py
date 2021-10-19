#!usr/bin/python
# -*- coding: utf-8 -*-
#
#@created: 14.10.2021
#@author: Fyodor Velikonivtsev
#@contact: mirotvorez00@gmail.com
import sys



def get_reverse_complement(strand, dna=True):
    rev_comp_dict = {
        "A": "T" if dna else "U",
        "T": "A",
        "U": "A",
        "G": "C",
        "C": "G",
    }
    
    return ''.join(rev_comp_dict[strand[index]] for index in range(len(strand)-1, -1, -1))


if __name__ == "__main__":
    strand = sys.argv[1]
    print(f"Reverse complement for {strand}:\n{get_reverse_complement(strand)}", file=sys.stdout)

