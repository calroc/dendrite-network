import fileinput


class Logan:
    def process(self, line):
        print line.rstrip()


if __name__ == '__main__':
    logan = Logan()
    for line in fileinput.input():
        logan.process(line)
