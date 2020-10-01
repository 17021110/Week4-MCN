class PrefixCodeTree:
  def __init__(self):
    self.tree = [0]*1000

  def insert(self,codeword,symbol):
    index=0
    for element in codeword:
      if element == 1: 
        index = index * 2 + 2
      elif element == 0:
        index = index * 2 + 1
    self.tree[index]=symbol

  def decode(self,encodedData, datalen):
    result=""
    index=0
    data=""
    for byte in encodedData:
      data += f'{byte:0>8b}'
    for i in range(datalen):
      char = data[i]
      if char == '1': 
        index = index * 2 + 2
      elif char == '0':
        index = index * 2 + 1
      if self.tree[index] != 0:
        result += " " + self.tree[index]
        index=0 
    return result

codeTree = PrefixCodeTree()
codebook = {
'x1': [0],
'x2': [1,0,0],
'x3': [1,0,1],
'x4': [1,1]
}

for symbol in codebook:
  codeTree.insert(codebook[symbol], symbol)

message = codeTree.decode(b'\xd2\x9f\x20', 21)
print(message)