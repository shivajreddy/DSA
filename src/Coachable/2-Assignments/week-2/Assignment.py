"""
Week 2 - Assignment
"""

'''
Write a function that runs in each of the following runtimes
O(1), O(log n), O(n), O(n log n), O(n^2), O(n^2 log n), O(n (log n)^2), O(2^n).
'''


def func_1(n):
    count = 1  # runs just once
    print(f"n:{n} | Run time: {count}")


def func_logn(n):
    count = 0
    i = 1
    while i < n + 1:  # runs log(n) times
        i = i * 2
        count += 1
    print(f"n:{n} | Run time: {count}")


def func_n(n):
    count = 0
    for i in range(n):  # runs n times
        count += 1
    print(f"n:{n} | Run time: {count}")


def func_nlogn(n):
    count = 0
    for i in range(n):  # runs n times
        j = 1
        while j < n + 1:  # runs log(n) times
            j = j * 2
            count += 1
    print(f"n:{n} | Run time: {count}")


def func_n2(n):
    count = 0
    for i in range(n):  # runs n times
        for j in range(n):  # runs n times
            count += 1
    print(f"n:{n} | Run time: {count}")


def func_n2_logn(n):
    count = 0
    for i in range(n):  # runs n times
        for j in range(n):  # runs n times
            k = 1
            while k < n + 1:  # runs log(n) times
                k = k * 2
                count += 1
    print(f"n:{n} | Run time: {count}")


def func_n_logn2(n):
    count = 0
    for i in range(n):  # runs n times
        j = 1
        while j < n + 1:  # runs log(n) times
            k = 1
            while k < n + 1:  # runs log(n) times
                k = k * 2
                count += 1
            j = j * 2
    print(f"n:{n} | Run time: {count}")


def func_2n(n):
    count = exponential_function(n)
    print(f"n:{n} | Run time: {count}")


def exponential_function(n):
    if n == 0:  # base condition
        return 1
    count = 0
    count += exponential_function(n - 1)  # since 2^n, call recursively twice. if 3^n call thrice.
    count += exponential_function(n - 1)
    return count


func_1(1000)
func_logn(1000)
func_n(1000)
func_nlogn(1000)
func_n2(1000)
func_n2_logn(1000)
func_n_logn2(1000)
func_2n(10)
