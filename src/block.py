import datetime

class Block(object):
    def __init__(self):
        self.index = None
        self.time_stamp = st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        self.transactions = 0
        self.proof = None
        self.previous_proof= None
        