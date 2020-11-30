print({ch: ord(ch) for ch in input().split(', ')})

# or: 
d = {}
for ch in input().split(', '):
    d[ch] = ord(ch)