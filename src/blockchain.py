class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.nodes = set()  # A set store all the nodes

    def register_nore(self, address):
        """
        Add a new node to the list of nodes

        :param address: Address of node. Eg. 'http://192.168.0.1:5000'
        :return None
        """
        # Prase the url and retrieve the network location part
        # Add the network location part into nodes
        pass


    def new_block(self, proof, previous_hash):
        """
        Create a new Block in the Blockchain. A block contains the following
        elements:
        block= {
            'index': Integer, the length of block chain + 1, Eg. 10
            'timestamp': time in seconds since the epoch
            'transactions': Current transactions in this block, 0 for new block
            'proof': proof,
            'previous_hash': hash of the previous block
        }

        :param proof: The proof given by the Proof of Work method
        :param previous_hash: Hash of previous Block
        :return: New Block
        """
        pass
    
    def new_transaction(self, sender, recipient, amount):
        """
        Create a new transaction to go into the next mined Block. New
        transaction will be appended to self.current_transactions

        :param sender: Address of the Sender
        :param recipient: Address of the Recipient
        :param amount: Amount
        :return: The index of the Block that will hold this transaction
        """
        pass

    @property
    def last_block(self):
        return self.chain[-1]
    
    def valid_chain(self, chain):
        """
        Determine if a given blockchain is valid

        :param chain: A blockchain
        :return: True if valid, False if not
        """
        # Traverse the whole chain, for each block, verify the
        # 'previous_hash" is equal to the calculate hash of last_block
        # If they don't match, return False
        #
        # Then verify the proof of work is correct
        # Run valid_proof against current block and last block's proof

    def resolve_conflict(self):
        """

        """

    @staticmethod
    def hash(block):
        # Hashes a Block
        pass
    
    @property
    def last_block(self):
        # Returns the last Block in the chain
        pass
