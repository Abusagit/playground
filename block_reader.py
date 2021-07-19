class BlockData:
    # 0 - path, 1 - format

    def __init__(self, path):
        self.path_format = path

    def iter_block_objects(self, block_obj):
        yield from block_obj

    def iter_block_file(self, new_block_symbol):
        """
        Write here the correct doc string.
        """
        with open(self.path_format) as f_read:
            _i = 1
            block_obj = {0: f_read.readline()}
            for line in f_read:
                if line.startswith(new_block_symbol):
                    yield block_obj[0].strip(), (block_obj[j] for j in range(1, _i))  # header, generator
                    _i = 1
                    block_obj.clear()
                    block_obj[0] = line
                else:
                    block_obj[_i] = line.strip()
                    _i += 1
            else:
                yield block_obj[0].strip(), (block_obj[j] for j in range(1, _i))  # header, generator
            block_obj.clear()

    def iter_block_file2(self, new_block_symbol):
        """

        :param new_block_symbol:
        :return: sequence
        """
        # with open(self.path_format) as f_read:
        #     sequence = []
        #     header =


if __name__ == '__main__':
    a = BlockData(path='/Users/darji/edusummer2021/students/Abusagit/rosalind/output.fasta')
    b = BlockData(path="/Users/darji/edusummer2021/students/Abusagit/rosalind/new.fasta")

    for i in a.iter_block_file(new_block_symbol='>'):
        print(i, list(a.iter_block_objects(i[1])))

    for i in b.iter_block_file(new_block_symbol='>'):
        print(i, list(a.iter_block_objects(i[1])))