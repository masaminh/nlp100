import argparse
import gzip
import json
import re


def get_article(file, name):
    with gzip.open(file, 'rt') as f:
        for line in f:
            dic = json.loads(line)

            if dic["title"] == name:
                return dic["text"]


def remove_markup(s):
    '''
    >>> remove_markup('[[イングランド王国]]／[[スコットランド王国]]<br />（両国とも[[連合法 (1707年)|1707年連合法]]まで）')
    'イングランド王国／スコットランド王国<br />（両国とも1707年連合法まで）'
    >>> s = '[[ファイル:Royal Coat of Arms of the United Kingdom.svg|85px|イギリスの国章]]'
    >>> remove_markup(s)
    '[[ファイル:Royal Coat of Arms of the United Kingdom.svg|85px|イギリスの国章]]'
    '''
    s = re.sub(r"('{2,3})|('{5})", '', s)
    s = re.sub(r'\[\[(?:[^]|]+?\|)?([^|]+?)\]\]', r'\1', s)
    return s


def get_basicinfo(article):
    regex = re.compile(r'^{{基礎情報 国$(.+?)^}}$',
                       flags=(re.MULTILINE | re.DOTALL))
    match = regex.search(article)

    if match:
        content = match.group(1)
        regex2 = re.compile(r'^\|(.+?) = (.+?)(?:(?=\n\|)|(?=\n$))',
                            flags=(re.MULTILINE | re.DOTALL))
        result = {m.group(1): remove_markup(m.group(2))
                  for m in regex2.finditer(content)}
    else:
        result = dict()

    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile')
    args = parser.parse_args()

    article = get_article(args.infile, 'イギリス')
    basicinfo = get_basicinfo(article)

    for k, v in basicinfo.items():
        print('{0}\t{1}'.format(k, v))


if __name__ == '__main__':
    main()
