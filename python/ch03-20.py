import argparse
import gzip
import json


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile')
    args = parser.parse_args()

    with gzip.open(args.infile, 'rt') as f:
        for line in f:
            dic = json.loads(line)

            if dic["title"] == 'イギリス':
                print(dic["text"])
                return


if __name__ == '__main__':
    main()
