import hashlib
import json

def hash(block):
    """
    Creates SHA256 hash of a block
    Params
        block: dict

    Return: string
    """

    json_str = json.dumps(block, sort_keys = True).encode()
    return hashlib.sha256(json_str).hexdigest()
             
