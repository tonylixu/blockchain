class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.nodes = set()

    def register_nore(self, address):
        """
        Add a new node to the list of nodes

        :param address: Address of node. Eg. 'http://192.168.0.1:5000'
        """
        # Prase the url and retrieve the network location part
        # Add the network location part into nodes
        pass


    def new_block(self):
        # Creates a new Block and adds it to the chain
        pass
    
    def new_transaction(self):
        # Adds a new transaction to the list of transactions
        pass

    @staticmethod
    def hash(block):
        # Hashes a Block
        pass
    
    @property
    def last_block(self):
        # Returns the last Block in the chain
        pass
