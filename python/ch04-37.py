import argparse
from collections import Counter
from itertools import chain
import matplotlib as mpl
import matplotlib.pyplot as plt


def read_morphemes(lines):
    morphemes = []

    for line in lines:
        if line.rstrip() == 'EOS':
            if len(morphemes) > 0:
                yield morphemes

            morphemes = []
        else:
            t1 = line.split('\t')
            t2 = t1[1].split(',')
            m = {'surface': t1[0], 'base': t2[6], 'pos': t2[0], 'pos1': t2[1]}
            morphemes.append(m)


def get_freq(morphemes):
    c = Counter(x['surface'] for x in chain.from_iterable(morphemes))
    return c.most_common(10)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile')
    args = parser.parse_args()

    with open(args.infile, mode='r') as f:
        morphemes = read_morphemes(f)
        freq = get_freq(morphemes)

    x = list(range(1, 11))
    y = [f[1] for f in freq]
    lbl = [f[0] for f in freq]
    mpl.rcParams['font.family'] = 'AppleGothic'
    plt.bar(x, y, tick_label=lbl)
    plt.show()


if __name__ == '__main__':
    main()
