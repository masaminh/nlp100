import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', type=argparse.FileType('r'))
    parser.add_argument('count', type=int)
    args = parser.parse_args()

    result = []
    for line in args.infile:
        result.append(line)

        if args.count < len(result):
            del result[0]

    for line in result:
        print(line, end='')


if __name__ == '__main__':
    main()
