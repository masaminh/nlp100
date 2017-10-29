import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', type=argparse.FileType('r'))
    parser.add_argument('count', type=int)
    args = parser.parse_args()

    count = 0
    for line in args.infile:
        print(line, end='')
        count += 1

        if args.count <= count:
            return


if __name__ == '__main__':
    main()
