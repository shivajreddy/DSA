# def fibonacci(n: int) -> int:
#     if n <= 1:
#         return n
#
#     f_minus_2, f_minus_1 = 0, 1
#
#     for _ in range(1, n):
#         f = f_minus_2 + f_minus_1
#         f_minus_2, f_minus_1 = f_minus_1, f
#
#     return f_minus_1
#
#
# print(fibonacci(8))


def fibonacci(n: int, memo: dict) -> int:
    if n in memo:
        return memo[n]
    # if n < 2:
    #     return n

    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)

    return memo[n]


print(fibonacci(21, {0: 0, 1: 1}))
