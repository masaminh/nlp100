import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', type=argparse.FileType('r'))
    args = parser.parse_args()

    prefdict = dict()

    for line in args.infile:
        pref = line.split()[0]

        if pref in prefdict:
            prefdict[pref] += 1
        else:
            prefdict[pref] = 1

    result = sorted(prefdict.items(), key=lambda x: x[1], reverse=True)

    print('\n'.join([str(freq) + ' ' + pref for pref, freq in result]))


if __name__ == '__main__':
    main()
