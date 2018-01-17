## Implement Your Own Blockchain
A Python implementation of Blockchain. You will need some certain amount of basic knowledge about Blockchain in order to understand the source code. To get the app running, you also need Python3.6 knowledge, Flask (A Python framework) and some basic REST API experiences.

### Prerequisite
* Python3.6+
* Flask0.12.2+
* requests2.18.4+
* CURL or Postman

### Blockchain Basics:
* Block: A block in Blockchain is a data structure (represented by files) that holds data permanently. A block represents the `present` and contains information about its past and future. Each time a block is `completed`, it gives way to the next block in the blockchain. The `completed` block is a permanent record of transactions in the past the the new transactions are recorded in the current one. In our code, an example block looks like:
```python
block = {
    'index': 'integer - len(blockchain) + 1',
    'timestamp': 'float - the time this block is completed',
    'transaction': 'list of dicts - all the transactions recorded',
    'proof': 'integer - the number that been used to solve the calcualtion problem, will be used for chain validation',
    'previous_hash': 'string - the hash string of previous block',
}
```