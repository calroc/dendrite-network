from os.path import exists
from hashlib import md5
from time import time
from dendnet.memcache import Client


gen_tag = lambda url: md5(url).hexdigest()


if exists('/home/calroc/memcached.sock'):
    U2T = T2U = ENG = Client(['unix:/home/calroc/memcached.sock'], debug=True)
else:
    U2T = Client(['127.0.0.1:11213'], debug=True)
    T2U = Client(['127.0.0.1:11214'], debug=True)
    ENG = Client(['127.0.0.1:11215'], debug=True)


def url2tag(url):
    url = str(url)
    tag = U2T.get(url)
    if not tag:
        tag = gen_tag(url)
        U2T.set(url, tag)
        T2U.set(tag, url)
    return tag


def tag2url(tag):
    tag = str(tag)
    url = T2U.get(tag)
    if not url:
        raise KeyError(tag)
    return url


def note_engage(me, it):
    me = str(me)
    it = str(it)
    key = '%s/%s' % (me, it)
    ENG.add(key, str(time())) # add() so only the first engage is recorded.
