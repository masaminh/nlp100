import argparse
import re


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
        regex3 = re.compile(r"('{2,3})|('{5})")
        result = {m.group(1): regex3.sub('', m.group(2))
                  for m in regex2.finditer(content)}
        print(result)


if __name__ == '__main__':
    main()
