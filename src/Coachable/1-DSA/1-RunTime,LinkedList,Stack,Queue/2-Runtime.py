from typing import List

from stopwatch import Stopwatch


# runtime analysis of linear

def linear(n: int) -> int:
    count = 0
    for i in range(n):
        count += 1
    return count


def two_sum(arr: List[int], target: int) -> List[int]:
    for idx, num in enumerate(arr):
        for idx2, num2 in enumerate(arr[idx + 1:]):
            if num + num2 == target:
                return [idx, idx + idx2 + 1]
    return [-1, -1]


two_sum_inputs = [([2, 7, 11, 15], 9), ([3, 2, 4], 6), ([3, 3], 6)]

# run the program
if __name__ == "__main__":

    for two_sum_input in two_sum_inputs:
        timer = Stopwatch()
        result = two_sum(two_sum_input[0], two_sum_input[1])
        print(f"result:{result}, Time: {timer.elapsed_time()}")
