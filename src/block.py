import datetime
import time

class Block(object):
    def __init__(self):
        self.index = None
        self.time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        self.transactions = []
        self.proof = None
        self.previous_blocks_hash= None