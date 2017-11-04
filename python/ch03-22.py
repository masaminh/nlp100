import argparse
import re


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', type=argparse.FileType('r'))
    args = parser.parse_args()

    regex = re.compile('\[\[Category:(?P<category>[^|]+)(\|.*)?\]\]')
    for line in args.infile:
        match = regex.search(line)
        if match:
            print(match.group('category'))


if __name__ == '__main__':
    main()
