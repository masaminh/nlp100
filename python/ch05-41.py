import argparse
import itertools


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile')
    args = parser.parse_args()

    with open(args.infile, mode='r') as f:
        for line_num, sentence in enumerate(read_sentences(f)):
            if line_num == 7:
                for i, c in enumerate(sentence):
                    print(
                        f'{i}\t{"".join([m.surface for m in c.morphs])}' +
                        f'\tdst:{c.dst}')
                break


def read_sentences(lines):
    chunks = []
    chunk_lines = []

    for line in lines:
        if line[0] == '*':
            if len(chunk_lines) > 0:
                chunks.append(Chunk(chunk_lines))

            chunk_lines = [line]
        elif line.rstrip() == 'EOS':
            if len(chunk_lines) > 0:
                chunks.append(Chunk(chunk_lines))

            for i, c in enumerate(chunks):
                if c.dst != -1:
                    chunks[c.dst].srcs.append(i)

            yield chunks

            chunks = []
            chunk_lines = []
        else:
            chunk_lines.append(line)


class Morph:
    def __init__(self, line):
        t1 = line.split('\t')
        t2 = t1[1].split(',')
        self.surface = t1[0]
        self.base = t2[6]
        self.pos = t2[0]
        self.pos1 = t2[1]

    def __repr__(self):
        return f"'{self.surface}'\t'{self.base}'\t{self.pos}\t{self.pos1}"


class Chunk:
    def __init__(self, lines):
        self.srcs = []
        t = lines[0].split()
        self.dst = int(t[2][0:-1])
        self.morphs = [Morph(l) for l in lines[1:]]

    def __repr__(self):
        return (f'{self.dst}\n' + str(self.srcs) + '\n' +
                '\n'.join([str(m) for m in self.morphs]) + '\n---\n')


if __name__ == '__main__':
    main()
