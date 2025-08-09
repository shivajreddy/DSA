s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

def dna_sequence(s: str)-> list:

  if len(s) < 10:
    return s
  
  start = 0
  hashmap = {}
  result = []
  temp = []

  for end in range(len(s)):
    curr = s[end]

    hashmap[curr] = 1 + hashmap.get(curr,0)

    if end >= 10:
      sub = s[start:end]
      if hashmap in temp and sub not in result:
        result.append(sub)
      temp.append(hashmap)
      first = s[start]
      hashmap[first] -= 1
      start += 1
    
  return result

print( dna_sequence(s) )