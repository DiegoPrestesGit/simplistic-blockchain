from hashlib import sha256

class Block():
  data = None
  hash = None
  nonce = 0
  previous_hash = '0' * 64

  def __init__(self, data, number=0):
    self.data = data
    self.number = number

def updatedHash(*args):
  hashing_txt = ''; h = sha256()
  for arg in args:
    hashing_txt += str(arg)

  h.update(hashing_txt.encode('utf-8'))
  return h.hexdigest()

print(updatedHash('deregue'))

def hashFunction(self):
  return updatedHash(
    self.previous_hash, 
    self.number, 
    self.data, 
    self.nonce
  )


def main():
  block = Block('Hey you', 1)

if __name__ == '__main__':
  main()

class Blockchain():
  pass