import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', type=argparse.FileType('r'))
    args = parser.parse_args()

    for line in args.infile:
        print(line.replace('\t', ' '), end='')


if __name__ == '__main__':
    main()
