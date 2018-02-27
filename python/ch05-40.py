import argparse
import itertools


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile')
    args = parser.parse_args()

    with open(args.infile, mode='r') as f:
        sentences = read_sentences(f)
        for m in itertools.chain.from_iterable(
                itertools.islice(sentences, 2, 3)):
            print(m)


def read_sentences(lines):
    morphemes = []

    for line in lines:
        if line.rstrip() == 'EOS':
            yield morphemes

            morphemes = []
        elif line[0] != '*':
            morphemes.append(Morph(line))


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


if __name__ == '__main__':
    main()
