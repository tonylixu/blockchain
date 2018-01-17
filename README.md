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
* Proof of Work: PoW is basically how new blocks are `mined` on the blockchain. In our implementation, the goal of PoW is to discover a number which solves a problem. We define the mathmatical problem as: The hash string of the last proof (from last block) and the new proof contains `4` leading `0`s. `sha256(last_proof+proof)[:4] == 0000`. This new `proof` number must be difficult to calculate but easy to verify.
* Transaction: A transaction is a piece of information that contians at lest:
  * An input/sender address: Which address was used to send the coins.
  * An amount: The amount of bitcoins that will be sent.
  * An output/receiver address: The receiver's address.
```python
# Sample transaction
{
 "sender": "d4ee26eee15148eefdsafdsafdsaf",
 "recipient": "fdsaf87687dsafdsaf6876fdsa",
 "amount": 3
}
```
* Mining: Mining is the process of collecting new transactions, add new transactions into a new block, append the new block into the existing chain:
  * Calculate the PoW
  * Reward the miner (In our case 4 coins)
  * Create the new block and add current transactions
  * Append the new block to the existing block chain

* Consensus: Since Blockchain is decentralized, how do we ensure that every node refelcts the same chain? This is called "The problem of Consensus". This problem occurs when one node has different chain to another node. In our code, we use the rule of "the longest valid chain is authoritative". The node that contains the longest chain on the blockchain network is the valid one.