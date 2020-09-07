from hashlib import sha256

class Block():
  data = None
  hash = None
  nonce = 0
  previous_hash = '0' * 64

  def __init__(self, data, number=0):
    self.data = data
    self.number = number

  def hashFunction(self):
    return updatedHash(
      self.previous_hash, 
      self.number, 
      self.data, 
      self.nonce
    )
  
  def __str__(self):
    return str('Block#: %s\nHash: %s\nPrevious: %s\nData: %s\nNonce: %s\n' 
      %(self.number, self.hashFunction(), self.previous_hash, self.data, self.nonce))

class Blockchain():
  difficulty = 4

  def __init__(self, chain=[]):
    self.chain = chain

  def addBlock(self, block):
    self.chain.append({
      'hash': block.hashFunction(), 
      'previous': block.previous_hash, 
      'number': block.number, 
      'data': block.data, 
      'nonce': block.nonce
    })

  def mining(self, block):
    try:
      block.previous_hash = self.chain[-1].get('hash')
    except IndexError:
      pass
    
    while True:
      if block.hashFunction()[:4] == "0" * self.difficulty:
        self.addBlock(block); break
      else:
        block.nonce += 1

def updatedHash(*args):
  hashing_txt = ''; h = sha256()
  for arg in args:
    hashing_txt += str(arg)

  h.update(hashing_txt.encode('utf-8'))
  return h.hexdigest()

print(updatedHash('deregue', 'i do hash things'))

def main():
  blockchain = Blockchain()
  fonDatabase = ['de', 'gu', 're', 'degurengo']

  num = 0
  for fon in fonDatabase:
    num += 1
    blockchain.mining(Block(fon, num))

  print(blockchain.chain)

  for block in blockchain.chain:
    print(block)

if __name__ == '__main__':
  main()
