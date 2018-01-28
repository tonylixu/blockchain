import hashlib
import json

def hash(block):
    """
    Creates SHA256 hash of a block
    Params
        block: dict

    Return: string
    """

    # To have a consistent hash value, make sure that the dictionary is ordered    
    json_str = json.dumps(block, sort_keys = True).encode()
    return hashlib.sha256(json_str).hexdigest()
             
