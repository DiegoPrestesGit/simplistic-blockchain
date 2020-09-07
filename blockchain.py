from hashlib import sha256

class Block():
  data = None
  hash = None
  nonce = 0
  previous_hash = '0' * 64

  def __init__(self, data, number=0):
    self.data = data
    self.number = number

class Blockchain():
  pass

def main():
  block = Block('Hey you', 1)

if __name__ == '__main__':
  main()