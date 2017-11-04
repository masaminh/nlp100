import argparse
import re


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', type=argparse.FileType('r'))
    args = parser.parse_args()

    regex = re.compile(r'(={2,6})\s*(?P<name>.+?)\s*\1')
    for line in args.infile:
        match = regex.search(line)
        if match:
            print(match.group('name') + '\t' + str(len(match.group(1)) - 1))


if __name__ == '__main__':
    main()
