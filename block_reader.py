class BlockData:
    # 0 - path, 1 - format

    def __init__(self, path, new_block_symbol):
        self.path_format = path
        self.new_block_symbol = new_block_symbol

    def iter_block_objects(self, block_obj):
        yield from block_obj

    def iter_block_file(self):
        """
        Write here the correct doc string.
        """
        with open(self.path_format) as f_read:
            _i = 1
            block_obj = {0: f_read.readline()}
            for line in f_read:
                if line.startswith(self.new_block_symbol):
                    yield block_obj[0].strip(), ''.join(block_obj[j] for j in range(1, _i))  # header, generator
                    _i = 1
                    block_obj.clear()
                    block_obj[0] = line
                else:
                    block_obj[_i] = line.strip()
                    _i += 1
            else:
                yield block_obj[0].strip(), ''.join(block_obj[j] for j in range(1, _i))  # header, generator
            block_obj.clear()

    def iter_block_file2(self):
        """

        :param:
        :return: header:str, sequence:list
        """
        with open(self.path_format) as f_read:
            sequence = []
            header = f_read.readline().strip()
            for line in f_read:
                if line.startswith(self.new_block_symbol):
                    yield header[:-1], ''.join(sequence)
                    header = line
                    sequence = []
                else:
                    sequence.append(line.strip())
        del sequence


if __name__ == '__main__':
    a = BlockData(path="/Users/darji/itmo_local/edusummer2021/students/Abusagit/rosalind/output.fasta",
                  new_block_symbol='>')
    b = BlockData(path="/Users/darji/itmo_local/edusummer2021/students/Abusagit/rosalind/new.fasta",
                  new_block_symbol='>')
    #
    # for i in a.iter_block_file(new_block_symbol='>'):
    #     print(i, list(a.iter_block_objects(i[1])))

    # for i in a.iter_block_file(new_block_symbol='>'):
    #     print(list(i[1]))
    #
    for i in b.iter_block_file2():
        print(i)
    print(list(a.iter_block_file()),
          list(a.iter_block_file2()))
