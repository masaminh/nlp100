import argparse
import json
import re
import urllib.request
import urllib.parse


def get_basicinfo(alltext):
    regex = re.compile(r'^{{基礎情報 国$(.+?)^}}$',
                       flags=(re.MULTILINE | re.DOTALL))
    match = regex.search(alltext)

    if match:
        content = match.group(1)
        regex2 = re.compile(r'^\|(.+?) = (.+?)(?:(?=\n\|)|(?=\n$))',
                            flags=(re.MULTILINE | re.DOTALL))
        result = {m.group(1): m.group(2) for m in regex2.finditer(content)}
    else:
        result = dict()

    return result


def get_url(filename):
    params = {'action': 'query', 'titles': 'File:' + filename,
              'prop': 'imageinfo', 'iiprop': 'url', 'format': 'json'}
    encoded_params = urllib.parse.urlencode(params)

    with urllib.request.urlopen('http://ja.wikipedia.org/w/api.php?' +
                                encoded_params) as res:
        url = json.loads(res.read().decode('utf-8')
                         )['query']['pages']['-1']['imageinfo'][0]['url']
        return url


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', type=argparse.FileType('r'))
    args = parser.parse_args()

    basicinfo = get_basicinfo(args.infile.read())
    flagimage = basicinfo['国旗画像']
    url = get_url(flagimage)

    print(url)


if __name__ == '__main__':
    main()
