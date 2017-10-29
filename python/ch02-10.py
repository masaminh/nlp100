import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', type=argparse.FileType('r'))
    args = parser.parse_args()

    count = 0
    for line in args.infile:
        count += 1

    print(count)


if __name__ == '__main__':
    main()
