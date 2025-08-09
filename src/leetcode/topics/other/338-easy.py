

def countBits(n):
  n = n+1
  result = []

  for i in range(n):

    binary = f"{i:b}".format(37)
    arr = [int(i) for i in binary]
    sum_arr = sum(arr)
    result.append(sum_arr)
    print(binary)
  
  return result


print(countBits(5))