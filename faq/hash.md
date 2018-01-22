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

Can you fill the blanks and give deails to each scenario?