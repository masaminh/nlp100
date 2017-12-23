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


def get_filereferences(article):
    regex = re.compile(r'ファイル:(.+?)\|')
    return (m.group(1) for m
            in (regex.search(l) for l in article.splitlines()) if m)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile')
    args = parser.parse_args()

    article = get_article(args.infile, 'イギリス')
    filereferences = get_filereferences(article)

    print('\n'.join(filereferences))


if __name__ == '__main__':
    main()
