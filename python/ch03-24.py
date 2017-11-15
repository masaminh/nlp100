import argparse
import re


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', type=argparse.FileType('r'))
    args = parser.parse_args()

    regex = re.compile(r'ファイル:(?P<name>.+?)\|')
    for line in args.infile:
        match = regex.search(line)
        if match:
            print(match.group('name'))


if __name__ == '__main__':
    main()
