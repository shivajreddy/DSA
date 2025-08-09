# f(n) = f(n-1) + f(n-2)
# f(0) = f(1) = 1
def question6(n: int) -> int:
    if n < 2:
        return 1
    return question6(n - 1) + question6(n - 2)


# f(n) = f(n-1) + f(n-2) + f(n-3)
# f(0) = f(1) = f(2) = 1
def question7(n: int) -> int:
    if n < 3:
        return 1
    return question7(n - 1) + question7(n - 2) + question7(n - 3)


# is_even(n) = is_odd(n-1)
# is_odd(n) = is_even(n-1)
# is_even(0) = True
# is_odd(0) = False
# Return "even" if even, "odd" if odd
def question8(n: int) -> str:
    def is_even(x):
        if x == 0:
            return True
        return is_odd(x - 1)

    def is_odd(x):
        if x == 0:
            return False
        return is_even(x - 1)

    # if is_even(n):
    #     return "even"
    # return "odd"
    return "even" if is_even(n) else "odd"
