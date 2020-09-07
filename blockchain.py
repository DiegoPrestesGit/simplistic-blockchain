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


def updatedHash(*args):
  hashing_txt = ''; h = sha256()
  for arg in args:
    hashing_txt += str(arg)

  h.update(hashing_txt.encode('utf-8'))
  return h.hexdigest()

print(updatedHash('deregue', 'i do hash things'))

def main():
  block = Block('Hey you', 1)
  print(block)

if __name__ == '__main__':
  main()

class Blockchain():
  pass
