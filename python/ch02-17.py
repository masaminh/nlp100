import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', type=argparse.FileType('r'))
    args = parser.parse_args()

    print('\n'.join({x.split()[0] for x in args.infile}))


if __name__ == '__main__':
    main()
