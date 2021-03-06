if __name__ == '__main__':
    import block_reader
else:
    from . import block_reader

"""
Implements reading .fasta file format
"""


def stupid_fasta_reader(fasta_file_name):

    """
    fasta_file_name: fasta file localisation
    """
    with open(rf"{fasta_file_name}.fasta") as f_read:
        iterator = iter(f_read.readlines())
    sequence = {0: next(iterator)}
    _i = 1
    for line in iterator:
        if line.startswith('>'):
            yield sequence[0], ''.join(sequence[j] for j in range(1, _i))
            _i = 1
            sequence.clear()
            sequence[0] = line
        else:
            sequence[_i] = line.strip()
            _i += 1
    else:
        yield sequence[0], ''.join(sequence[j] for j in range(1, _i))


def iter_fasta_reader(fasta_file_name):
    with open(rf"{fasta_file_name}.fasta") as f_read:
        # print(f_read.readlines())
        iterator = iter(f_read.readlines())
    sequence = {0: next(iterator)}
    _i = 1
    for line in iterator:
        if line.startswith('>'):
            yield sequence[0], ''.join(sequence[j] for j in range(1, _i))
            _i = 1
            sequence.clear()
            sequence[0] = line
        else:
            sequence[_i] = line.strip()
            _i += 1
    else:
        yield sequence[0], ''.join(sequence[j] for j in range(1, _i))


class FastaData(block_reader.BlockData):
    def __init__(self, path):
        super().__init__(path, new_block_symbol='>')

    def iter_block_file(self, new_block_symbol='>'):
        yield from super(FastaData, self).iter_block_file()

    def iter_block_objects(self, block_obj):
        yield from super(FastaData, self).iter_block_objects(block_obj)


if __name__ == '__main__':
    import os
    print(os.getcwd())
    # for h, s in iter_fasta_reader(r"/Users/darji/edusummer2021/students/Abusagit/rosalind/output.fasta"):
    #     print(h, repr(s))
    #     print(len(s))

    a = FastaData(path=r"/Users/darji/itmo_local/edusummer2021/students/Abusagit/rosalind/new.fasta")
    for i in a.iter_block_file(new_block_symbol='>'):
        print(i)
        print(list(a.iter_block_objects(i[1])))
