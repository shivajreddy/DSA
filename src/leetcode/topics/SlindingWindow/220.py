# arr = [1,5,9,1,5,9]
from input import arr

def containes3(arr, k, t):

  start = 0

  for end in range(len(arr)):
    curr = arr[end]
    print(f'iter starts with start={start}, end={end}')

    # reduce the win size to keep checking
    act_start = start
    while end-act_start <=k and (end != act_start):
      print(f'checking with, first={arr[start]}, curr={curr}')
      if abs(curr - arr[act_start]) <= t:
        return True
      act_start += 1
    
    if end+1-start > k:
      start += 1
    
  return False

print(containes3(arr,10000,0))