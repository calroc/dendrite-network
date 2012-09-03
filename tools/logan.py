#!/usr/bin/env python
import fileinput
from collections import defaultdict


class Logan:

    REGISTER = {}
    BUMPS = defaultdict(set)
    ENGAGES = defaultdict(set)
    ANON_BUMPS = defaultdict(lambda: defaultdict(int))
    ANON_ENGAGES = defaultdict(lambda: defaultdict(int))

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
        self.ANON_BUMPS[what][who] += 1

    anon = bump_anon

    def engage_anon(self, day, time, who, what):
        self.ANON_ENGAGES[what][who] += 1

    anon_engage = engage_anon

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

    def print_abumps(self):
        for tag, bumps in self.ANON_BUMPS.items():
            print self.h(tag)
            for who in sorted(bumps):
                print '   ', self.h(who), '--->', bumps[who]
            print

    def print_aeng(self):
        for tag, eng in self.ANON_ENGAGES.items():
            print self.h(tag)
            for who in sorted(eng):
                print ' -->', self.h(who), '--->', eng[who]
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
        print; print
        print 'Anonymous Bumps (by subject URL)'
        print
        logan.print_abumps()
        print; print
        print 'Anonymous Engages (by subject URL)'
        print
        logan.print_aeng()
        print



if __name__ == '__main__':
    from pprint import pprint
    logan = Logan()
    for line in fileinput.input():
        logan.process(line)
    logan.print_report()
