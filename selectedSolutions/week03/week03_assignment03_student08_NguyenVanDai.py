from string import ascii_uppercase
def namescores(word):
    return sum(ascii_uppercase.index(c) + 1 for c in word.strip('"'))

with open('names.txt') as f:
  names = f.read().split(',')
  names.sort()
print (sum(i*namescores(x) for i, x in enumerate(names, 1)))