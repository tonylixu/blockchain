from urllib.parse import urlparse

def register_node(self, address):
    """
    Add a new node to the list of nodes.
    :param address: Address of node. Eg. 'http://192.168.0.1:5000'
    :return None
    """
    node = urlparse(address).netloc
    self.nodes.add(node)

