#!/home/fvelikonivcev/miniconda3/envs/bioconda/bin/python


import bisect
import io
import os
import sys
import pandas as pd
from collections import defaultdict
import sys


pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


def read_vcf(path):
    with open(path, 'r') as f:
        lines = tuple(l for l in f if not l.startswith('##'))
    
    return pd.read_csv(io.StringIO(''.join(lines)), dtype={'#CHROM': str, 'POS': int, 'ID': str, 'REF': str, 'ALT': str, 'QUAL': str, 'FILTER': str, 'INFO': str}, sep='\t').rename(columns={'#CHROM': 'CHROM'})



def read_annotation(annotation_path):
    gencode = pd.read_table(annotation_path, comment='#', sep='\t', names=['seqname', 'source', 'feature', 'start', 'end', 'score', 'strand', 'frame', 'attribute'])
    gencode_genes = gencode[gencode['feature'] == 'gene'][['seqname', 'start', 'end', 'attribute']].copy().reset_index()
    gencode_genes.drop('index', axis='columns', inplace=True)

    return gencode_genes


def get_mutations(gff_file, vcf_file):
    genes_starts = tuple(gff_file.loc[:, 'start'])
    mutated = [bisect.bisect_left(genes_starts, mutation_index) - 1 for mutation_index in vcf_file['POS']]
    mutated_genes = gff_file.iloc[mutated].reset_index()


    columns = {key: [] for key in ['ID', 'Dbxref', 'Name', 'gbkey', 'gene', 'gene_biotype', 'gene_synonym', 'locus_tag']}
    genes_info = [gene.split(';') for gene in tuple(mutated_genes['attribute'])]
    
    for gene in genes_info:
        for attr in gene:
            key, value = attr.split("=")
            columns[key].append(value)
    frame = pd.DataFrame.from_dict(columns).set_index('Name')
    return frame


if __name__ == "__main__":
    vcf_path, annotation_path = sys.argv[1:]
    separator = f"{''.join('*' for _ in range(110))}"
    print(separator, file=sys.stderr)
    vcf_file = read_vcf(vcf_path)
    print("Read .vcf file\nStarted reading .gff file...\n\n\n", file=sys.stderr)
    gff_file = read_annotation(annotation_path)
    print("Done!\nStarted building mutations dataframe...\n\n\n", file=sys.stderr)
    print(get_mutations(gff_file, vcf_file), file=sys.stdout)
    print(f"Done!\n{separator}", file=sys.stderr)

    
