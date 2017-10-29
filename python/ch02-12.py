import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', type=argparse.FileType('r'))
    parser.add_argument('outfile1', type=argparse.FileType('w'))
    parser.add_argument('outfile2', type=argparse.FileType('w'))
    args = parser.parse_args()

    for line in args.infile:
        t = line.split()
        args.outfile1.write(t[0] + '\n')
        args.outfile2.write(t[1] + '\n')


if __name__ == '__main__':
    main()
