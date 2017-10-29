import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', type=argparse.FileType('r'))
    args = parser.parse_args()

    result = sorted([x for x in args.infile],
                    key=lambda x: x.split()[2], reverse=True)
    print(''.join(result))


if __name__ == '__main__':
    main()
