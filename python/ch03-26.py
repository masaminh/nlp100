import argparse
import re


def remove_markup(s):
    return re.sub(r"('{2,3})|('{5})", '', s)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', type=argparse.FileType('r'))
    args = parser.parse_args()

    regex = re.compile(r'^{{基礎情報 国$(.+?)^}}$',
                       flags=(re.MULTILINE | re.DOTALL))
    alltext = args.infile.read()
    match = regex.search(alltext)

    if match:
        content = match.group(1)
        regex2 = re.compile(r'^\|(.+?) = (.+?)(?:(?=\n\|)|(?=\n$))',
                            flags=(re.MULTILINE | re.DOTALL))
        result = {m.group(1): remove_markup(m.group(2))
                  for m in regex2.finditer(content)}

        for k, v in result.items():
            print('{0}\t{1}'.format(k, v))


if __name__ == '__main__':
    main()
