#!/usr/bin/env python
import fileinput
import logging

from dendnet.stores import url2tag

logging.basicConfig()
log = logging.getLogger('load')
for line in fileinput.input():
    url2tag(line.strip(), log)
