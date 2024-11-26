## Exploring Bit Coin and Block Chain with Python

* http://karpathy.github.io/2021/06/21/blockchain/
* https://andrea.corbellini.name/2015/05/17/elliptic-curve-cryptography-a-gentle-introduction/
* https://github.com/karpathy/cryptos/blob/main/blog.ipynb

## Simple blockchain mining example

```
import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, data, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.data = data
        self.nonce = nonce
        self.timestamp = time.time()
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data_to_hash = str(self.index) + self.previous_hash + str(self.timestamp) + str(self.data) + str(self.nonce)
        return hashlib.sha256(data_to_hash.encode()).hexdigest()

def mine_block(previous_block, data, difficulty):
    new_block = Block(previous_block.index + 1, previous_block.hash, data)
    while not new_block.hash.startswith('0' * difficulty):
        new_block.nonce += 1
        new_block.hash = new_block.calculate_hash()
    return new_block

def create_genesis_block():
    return Block(0, "0", "Genesis Block")

if __name__ == "__main__":
    blockchain = [create_genesis_block()]
    previous_block = blockchain[0]

    for i in range(1, 4):
        new_block = mine_block(previous_block, f"Block {i} Data", 2)
        blockchain.append(new_block)
        previous_block = new_block
        print(f"Block {i} mined: {new_block.hash}")
```
