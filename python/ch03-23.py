import argparse
import gzip
import json
import re


def get_article(file, name):
    with gzip.open(file, 'rt') as f:
        for line in f:
            dic = json.loads(line)

            if dic["title"] == name:
                return dic["text"]


def get_sections(article):
    regex = re.compile(r'(={2,6})\s*(.+?)\s*\1')
    return ((m.group(2), len(m.group(1)) - 1) for m
            in (regex.search(l) for l in article.splitlines()) if m)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile')
    args = parser.parse_args()

    article = get_article(args.infile, 'イギリス')
    sections = get_sections(article)

    print('\n'.join(['{0[0]}\t{0[1]}'.format(x) for x in sections]))


if __name__ == '__main__':
    main()
