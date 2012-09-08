#!/usr/bin/env python
import fileinput
import logging

from dendnet.stores import url2tag

logging.basicConfig()
log = logging.getLogger('load')
for line in fileinput.input():
    line = line.strip()
    print url2tag(line, log), line
