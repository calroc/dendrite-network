from hashlib import md5
from string import digits, lowercase


STR = (digits + lowercase).__getitem__


def to36(i):
    acc = []
    while i:
        i, r = divmod(i, 36)
        acc.append(STR(r))
    return ''.join(acc[::-1])


def tag_for(s):
    return to36(int(md5(s).hexdigest(), 16))


if __name__ == '__main__':
    m = md5("Hey! Funny").hexdigest()
    n = int(m, 16)
    print n, m
    M = to36(n)
    print int(M, 36), M
