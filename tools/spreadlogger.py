import logging
import spread


SPREADD = '4803@localhost'
GROUP = 'test'
UNAME = 'logger-0'


class SpreadHandler(logging.Handler):
    def __init__(self,
        spreadd=SPREADD,
        group=GROUP,
        user=UNAME,
        level=logging.NOTSET,
        ):
        logging.Handler.__init__(self, level)
        self.spreadd = spreadd
        self.group = group
        self.user = user
        self.mb = spread.connect(spreadd, user)
        self.mb.join(GROUP)

    def emit(self, record):
        message = self.format(record)
        sent = self.mb.multicast(spread.FIFO_MESS, self.group, message)
        assert sent == len(message)

    def close(self):
        logging.Handler.close(self)
        self.mb.disconnect()


if __name__ == '__main__':
    handler = SpreadHandler()
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)

    log = logging.getLogger()
    log.setLevel(logging.DEBUG)
    log.addHandler(handler)

    log = logging.getLogger("Heeheehee")
