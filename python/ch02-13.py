import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile1', type=argparse.FileType('r'))
    parser.add_argument('infile2', type=argparse.FileType('r'))
    parser.add_argument('outfile', type=argparse.FileType('w'))
    args = parser.parse_args()

    for c1, c2 in zip(args.infile1, args.infile2):
        args.outfile.write(c1.rstrip('\r\n') + '\t' + c2.rstrip('\r\n') + '\n')


if __name__ == '__main__':
    main()
