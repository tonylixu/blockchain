## Hash

Hash is a function that can be used to map data of arbitrary size to data of fixed size. In our project, hash() is been used to map a block data to a string. No matter what your input is, the output will always have a fixed 256-bits length (hexdecimal, each digit code has 4 bits).

For example:
```python
block = {
    'index': 1,
    'timestamp': time(),
    'transactions': [],
    'proof': 100,
    'previous_hash': '1',
}

hash_str = sha256(block)
```
The value of hash_str is `0460d780524d192841a2b47f6911b0da2c0caa54ed4672d60acf5afe8256d742`.

### Why do we need hash?
In our project, we use `hash()` in two different scenarios.

1. Scenario 1: consensus



2. Scenario 2: PoW

We need to use hash() in our Proof of Work function because the miner will have to use hash() to turn a block into a hash value, which will be 256-bits in length using the sha256 function. However, the hash value generated will have to satisfy a certain criteria in order for the block to be valid, which is to avoid multiple miners creating a block at the same time. When calculating the hash value of the block, a nonce value is added in the calculation to help the end result meeting the criteria. If the value generated does not meet the criteria, then the nonce value will have to be changed and the hash value recalculated. This process repeats until a hash value that meets the criteria is successfully generated. 

Can you fill the blanks and give deails to each scenario?
