import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('n', type=int)
    parser.add_argument('infile', type=argparse.FileType('r'))
    parser.add_argument('prefix')
    args = parser.parse_args()

    lines = args.infile.readlines()
    lines_len = len(lines)
    c = lines_len // args.n
    adj = lines_len % args.n

    lines_list = [c + 1] * adj + [c] * (args.n - adj)

    for i, line_count in enumerate(lines_list):
        filename = args.prefix + 'a' + chr(ord('a') + i)

        with open(filename, 'w') as f:
            f.writelines(lines[0:line_count])

        del lines[0:line_count]


if __name__ == '__main__':
    main()
