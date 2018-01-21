from transaction import Transaction

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.nodes = set()  # A set store all the nodes

    def register_nore(self, address):
        """
        Add a new node to the list of nodes.
        How to implement:
            - Prase the url address and retrieve the network location part
            - Add the network location part into nodes

        :param address: Address of node. Eg. 'http://192.168.0.1:5000'
        :return None
        """
        pass


    def new_block(self, proof, previous_hash):
        """
        Create a new Block in the Blockchain. 
        How to implement:
            - A block contains the following elements:
        block= {
            'index': Integer, the length of block chain + 1, Eg. 10
                The genesis block index is of course 1.
            'timestamp': time in seconds since the epoch when new block is created
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
        Create a new transaction to go into the next mined Block. 
        How to implement:
            - New transaction will be appended to self.current_transactions
            - Sample transaction: {
                'sender': sender,
                'recipient': recipient,
                'amount': amount,
            }

        :param sender: Address of the Sender
        :param recipient: Address of the Recipient
        :param amount: Amount
        :return: The index of the Block that will hold this transaction
        """
        tran = Transaction(sender, recipient, amount)
        self.current_transactions.append(tran)
        # TODO: 
        #   Check if chain is zero    
        #   Chcek if block size limit before use the last block
        idx_dest_block = len(self.chain) - 1
        return idx_dest_block


    @property
    def last_block(self):
        return self.chain[-1]
    
    def valid_chain(self, chain):
        """
        Determine if a given blockchain is valid. 
        How to implement:
            - Traverse the whole chain, for each block, 
                verify the 'previous_hash" is equal to the calculate 
                hash of last_block. If they don't match, return False.
            - Then verify the proof of work is correct. Run valid_proof against 
                current block and last block's proof

        :param chain: A blockchain
        :return: True if valid, False if not
        """
        pass

    def resolve_conflict(self):
        """
        This is the consensus algorithm, it resolves conflicts by
        replacing the chain with the longest one in the network.

        :return: True if our chain was replaced, False if not
        """

    @staticmethod
    def hash(block):
        """
        Create a SHA-256 hash of block. 
        How to implement:
            - You can sort the block (which is a dictionary), 
                then dump into a JSON format, run the hashlib.sha256()
                function

        :param block: Block
        """
        pass

    def proof_of_work(slef, last_proof):
        """
        Simple Proof of Work Algorithm:
            - Find a number p2 such that hash(p1p2) contains leading 4 zeroes
            - p1 is the previous proof, p2 is the new proof
            - You can call the valid_proof method
        :param last_proof: previous proof
        :return: proof
        """
    
    def valid_proof(last_proof, proof):
        """
        Validates the Proof.
        How to implement:
            - Combine last_proof and proof into a string
            - Calculate the SHA-256 hash of the string
            - If string[:4] == '0000', return True, otherwise return False

        :param last_proof: Previous Proof
        :param proof: Current Proof
        :return: True if correct, False if not.
        """
        pass
