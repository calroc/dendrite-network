import fileinput
from collections import defaultdict


class Logan:

    REGISTER = {}
    BUMPS = defaultdict(set)
    ENGAGES = defaultdict(set)

    def process(self, line):
        self.what_it_is(*line.split())

    def what_it_is(self, day, time, kind, *rest):
        method = getattr(self, kind)
        method(day, time, *rest)

    def register(self, day, time, tag, url):
##        print 'register\t', tag, url
        self.REGISTER.setdefault(tag, url)

    def bump(self, day, time, from_, what, to):
##        print 'bump    \t', from_, what, to
        self.BUMPS[what].add((from_, to))

    def engage(self, day, time, who, what):
##        print 'engage  \t', who, what
        self.ENGAGES[what].add(who)

    def bump_anon(self, day, time, who, what):
        pass

    def engage_anon(self, day, time, who, what):
        pass

    def h(self, tag):
        return self.REGISTER.get(tag, tag + "!?")

    def print_reg(self):
        for tag, url in sorted(self.REGISTER.items()):
            print tag, '=>', url

    def print_bumps(self):
        for tag, bumps in self.BUMPS.items():
            print self.h(tag)
            for from_, to in sorted(bumps):
                print '   ', self.h(from_), '--->', self.h(to)
            print

    def print_eng(self):
        for tag, eng in self.ENGAGES.items():
            print self.h(tag)
            for who in eng:
                print ' -->', self.h(who)
            print

    def print_report(self):
        print
        print 'Registered URLs'
        print
        logan.print_reg()
        print; print
        print 'Bumps (by subject URL)'
        print
        logan.print_bumps()
        print; print
        print 'Engages (by subject URL)'
        print
        logan.print_eng()
        print



if __name__ == '__main__':
    from pprint import pprint
    logan = Logan()
    for line in fileinput.input():
        logan.process(line)
    logan.print_report()
