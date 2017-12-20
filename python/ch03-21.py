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


def get_categorylines(article):
    regex = re.compile(r'\[\[Category:.*\]\]')
    return [l for l in article.splitlines() if regex.search(l)]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile')
    args = parser.parse_args()

    article = get_article(args.infile, 'イギリス')
    categorylines = get_categorylines(article)
    print('\n'.join(categorylines))


if __name__ == '__main__':
    main()
