import CaboCha
from graphviz import Digraph


def main():
    g = Digraph(format='png')

    cabocha = CaboCha.Parser()
    cabochastr = cabocha.parse(input()).toString(CaboCha.FORMAT_LATTICE)
    lines = cabochastr.splitlines()

    s = list(read_sentences(lines))[0]
    for i, c in enumerate(s):
        if c.nomark():
            g.node(str(i), label=c.get_surface_nomark())

            if c.dst >= 0 and s[c.dst].nomark():
                g.edge(str(i), str(c.dst))

    g.render('ch05-44')


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

    def get_surface(self):
        return ''.join([m.surface for m in self.morphs])

    def nomark(self):
        return [m for m in self.morphs if m.pos != '記号']

    def get_surface_nomark(self):
        return ''.join([m.surface for m in self.nomark()])


if __name__ == '__main__':
    main()
