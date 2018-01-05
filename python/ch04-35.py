import argparse
from itertools import chain


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


def ngram(s, n):
    return [s[i:i + n] for i in range(len(s))]


def get_words(morphemes):
    words = []

    for line in morphemes:
        word = []

        for morpheme in line:
            if morpheme['pos'] == '名詞':
                word.append(morpheme['surface'])
            else:
                if len(word) > 1:
                    words.append(''.join(word))

                word = []

    if len(word) > 1:
        words.append(''.join(word))

    return words


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile')
    args = parser.parse_args()

    with open(args.infile, mode='r') as f:
        morphemes = read_morphemes(f)
        words = get_words(morphemes)

    for word in words:
        print(word)


if __name__ == '__main__':
    main()
