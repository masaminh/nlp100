import random


def func00(source):
    """
    >>> func00('stressed')
    'desserts'
    """
    return source[::-1]


def func01(source):
    """
    >>> func01('パタトクカシーー')
    'パトカー'
    """
    return source[::2]


def func02(source1, source2):
    """
    >>> func02('パトカー', 'タクシー')
    'パタトクカシーー'
    """
    return ''.join([x + y for x, y in zip(source1, source2)])


def func03(source):
    """
    >>> func03('One, two, three.')
    [3, 3, 5]
    """
    return [len([c for c in x if str.isalpha(c)]) for x in source.split()]


def func04(source, pos):
    """
    >>> func04('One Two Three.', [1, 3])
    {'O': 1, 'Tw': 2, 'T': 3}
    """
    t = source.split()
    return {x[:1 if i + 1 in pos else 2]: i + 1 for i, x in list(enumerate(t))}


def func05(s, n):
    """
    >>> func05('ABCD', 2)
    ['AB', 'BC', 'CD', 'D']
    >>> func05(['ABC', 'DEF', 'GHI', 'JKL'], 2)
    [['ABC', 'DEF'], ['DEF', 'GHI'], ['GHI', 'JKL'], ['JKL']]
    """
    return [s[i:i + n] for i in range(len(s))]


def func07(x, y, z):
    """
    >>> func07(12, '気温', 22.4)
    '12時の気温は22.4'
    """
    return '{0}時の{1}は{2}'.format(x, y, z)


def cipher(s):
    """
    >>> cipher('AaBbCc')
    'AzByCx'
    """
    return ''.join([chr(219 - ord(x)) if str.islower(x) else x for x in s])


def func09_shuffle(s):
    if (len(s) <= 4):
        r = s
    else:
        m = list(s[1:-1])
        random.shuffle(m)
        r = s[0] + ''.join(m) + s[-1]

    return r


def func09(s):
    return ' '.join([func09_shuffle(x) for x in s.split()])


def main():
    print('00:' + func00('stressed'))

    print('01:' + func01('パタトクカシーー'))

    print('02:' + func02('パトカー', 'タクシー'))

    s03 = 'Now I need a drink, alcoholic of course, '
    s03 += 'after the heavy lectures involving quantum mechanics.'
    print('03:' + str(func03(s03)))

    s04 = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. '
    s04 += 'New Nations Might Also Sign Peace Security Clause. '
    s04 += 'Arthur King Can.'
    print('04:' + str(func04(s04, [1, 5, 6, 7, 8, 9, 15, 16, 19])))

    s05 = 'I am an NLPer'
    print('05: 単語bi-gram: ' + str(func05(s05.split(), 2)))
    print('05: 文字bi-gram: ' + str(func05(s05, 2)))

    s06_x = set(func05('paraparaparadise', 2))
    s06_y = set(func05('paragraph', 2))
    print('06: 和集合: ' + str(s06_x | s06_y))
    print('06: 積集合: ' + str(s06_x & s06_y))
    print('06: 差集合: ' + str(s06_x - s06_y))
    print("06: Xの中に'se'があるか: " + str('se' in s06_x))
    print("06: Yの中に'se'があるか: " + str('se' in s06_y))

    print('07: ' + func07(12, '気温', 22.4))

    s08 = cipher('AaBbCc')
    print('08: 暗号: ' + s08)
    print('08: 復号: ' + cipher(s08))

    s09 = "I couldn't believe that I could actually understand "
    s09 += 'what I was reading : the phenomenal power of the human mind .'
    print('09: ' + func09(s09))


if __name__ == '__main__':
    main()
