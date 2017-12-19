import argparse
import gzip
import json


def get_article(file, name):
    with gzip.open(file, 'rt') as f:
        for line in f:
            dic = json.loads(line)

            if dic["title"] == name:
                return dic["text"]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile')
    args = parser.parse_args()

    print(get_article(args.infile, 'イギリス'))


if __name__ == '__main__':
    main()
