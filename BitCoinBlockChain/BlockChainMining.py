

import hashlib
import time

###############################


class Block:

    def __init__(self, index, previous_hash, data, control=0):
        self.index         = index
        self.previous_hash = previous_hash
        self.data          = data
        self.timestamp     = time.time()
        self.control       = control
        self.hash          = self.calculate_hash()
        self.nonce         = 0

    def calculate_hash(self):
        data_to_hash = str( self.index  ) + self.previous_hash + str(self.timestamp) + str( self.data )  + str( self.control )
        return hashlib.sha256( data_to_hash.encode()  ).hexdigest()


##############################

def create_genesis_block():
    return Block(0, "0", "Genesis Block")


##############################


def mine_block( previous_block, data1, data2 ):
    difficulty = 0
    total_data = data1 + data2
    new_block = Block( previous_block.index + 1, previous_block.hash, total_data )
    while not new_block.hash.startswith( '0' * difficulty  ):
        new_block.hash  = new_block.calculate_hash()
        new_block.nonce = new_block.nonce + 1
    return new_block




##############################
## MAIN_LOOP()


## new_block = mine_block()
## MyBlock = Block( 3, "hdge54h", "transaction",   )


block_chain = [  create_genesis_block()   ]

print( block_chain  )

##############################

previous_block = block_chain[0]

for i in range(1, 4):
    new_block   = mine_block( previous_block, f"Block {i} Data", "some data"  )
    block_chain.append( new_block  )
    previous_block = new_block
    print(f"Block {i} mined: { new_block.hash }")

print( block_chain )


print( block_chain[2].nonce )


## difficulty = 7
## print( '0' * difficulty  )
