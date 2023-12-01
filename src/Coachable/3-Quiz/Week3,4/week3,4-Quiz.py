def question1(n: int) -> int:
    if n <= 0:
        return 1
    return n * question1(n - 1)


def question2(n: int) -> int:
    if n < 2:
        return 1
    return question2(n // 2) + question2(n // 2)


def question3(n: int) -> int:
    if n < 2:
        return 1
    return question3(n // 2) + question3(n - 1)


def question4(tuples: list[tuple[int, int]]) -> list[tuple[int, int]]:
    # tuples.sort(key=lambda tup: -(tup[0] + 3 * tup[1]))
    tuples.sort(key=lambda tup: tup[0] + 3 * tup[1], reverse=True)
    return tuples


def question5(tuples: list[tuple[int, int]]) -> list[tuple[int, int]]:
    tuples.sort(key=lambda tup: (-tup[0], tup[1]))
    return tuples


def test_question4():
    assert question4([(7, 2), (2, 7), (3, 4), (4, 2)]) == [(2, 7), (3, 4), (7, 2), (4, 2)]
    assert question4([(-7, -2), (-2, -7), (-3, -4), (-4, -2)]) == [(-4, -2), (-7, -2), (-3, -4), (-2, -7)]
    assert question4([(-2, 7), (2, -7)]) == [(-2, 7), (2, -7)]


def test_question5():
    assert question5([(1, 3), (2, 4), (3, 5)]) == [(3, 5), (2, 4), (1, 3)]
    assert question5([(1, 3), (1, 2), (1, 4)]) == [(1, 2), (1, 3), (1, 4)]
    assert question5([(1, 3), (2, 5), (2, 7), (3, 3)]) == [(3, 3), (2, 5), (2, 7), (1, 3)]


def question6(arr: list[int]) -> list[int]:
    curr_sum = 0
    result = []
    for num in arr:
        curr_sum += num
        result.append(curr_sum)
    return result


def question7(arr: list[int]) -> list[int]:
    left = [1]  # [1, first_item, _, _, _, n-1]
    right = [1]  # [_, _, last_item, 1]
    curr_mult = 1
    for i in range(len(arr) - 1):
        curr_mult *= arr[i]
        left.append(curr_mult)
    curr_mult = 1
    for i in range(len(arr) - 1, 0, -1):
        curr_mult *= arr[i]
        right.append(curr_mult)
    right.reverse()
    result = []
    for i in range(len(left)):
        result.append(left[i] * right[i])
    return result
    # return [left, right]


question7([1, 2, 3, 4])


def test_question6():
    assert question6([1, 2, 3, 4, 5]) == [1, 3, 6, 10, 15]
    assert question6([1, -1, 1, -1, 1]) == [1, 0, 1, 0, 1]


def test_question7():
    assert question7([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert question7([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    assert question7([-1, 1, -1, 1, -1]) == [1, -1, 1, -1, 1]
    assert question7([3, 5]) == [5, 3]


def question8(arr: list[int], size: int) -> list[int]:
    i, j = 0, 0
    result = []
    win_sum = 0
    for j in range(len(arr)):
        win_sum += arr[j]
        if j - i + 1 == size:
            result.append(win_sum)
            win_sum -= arr[i]
            i += 1
    return result


def test_question8():
    assert question8([1, 2, 3, 4, 5], 1) == [1, 2, 3, 4, 5]
    assert question8([1, 2, 3, 4, 5], 2) == [3, 5, 7, 9]
    assert question8([1, 2, 3, 4, 5], 3) == [6, 9, 12]
    assert question8([1, 2, 3, 4, 5], 4) == [10, 14]
    assert question8([1, 2, 3, 4, 5], 5) == [15]


def question9(n: int) -> int:
    if n < 3:
        return n
    fib = [1, 2]
    for i in range(2, n):
        x, y = fib[0], fib[1]
        fib[0], fib[1] = y, x + y
    return fib[1]


def question10(m: int, n: int) -> int:
    def dfs(a, b, memo):
        if a <= 1 or b <= 1:
            return 1
        memo[(a, b)] = dfs(a - 1, b, memo) + dfs(a, b - 1, memo)
        return memo[(a, b)]

    return dfs(m, n, {})


def test_question9():
    assert question9(1) == 1
    assert question9(2) == 2
    assert question9(3) == 3
    assert question9(7) == 21


def test_question10():
    assert question10(3, 7) == 28
    assert question10(3, 2) == 3
    assert question10(2, 3) == 3
    assert question10(1, 1) == 1


def question11(inp: str) -> str:
    arr = inp.split()
    return "-".join(arr)


def question12(inp: str) -> str:
    arr: list[str] = list(inp)
    for i in range(1, len(arr), 2):
        arr[i] = arr[i].upper()
    return ''.join(arr)


def question13(arr: list[str]) -> dict[str, int]:
    word_freq = {}
    for sentence in arr:
        words = sentence.split()
        for word in words:
            word = word.lower()
            word_freq[word] = word_freq.get(word, 0) + 1
    return word_freq


def test_question11():
    assert question11('hello there everyone') == 'hello-there-everyone'
    assert question11('  trailing whitespace ') == 'trailing-whitespace'


def test_question12():
    assert question12('coachable') == 'cOaChAbLe'


def test_question13():
    assert question13(['hello hi all', 'hello again']) == {'hello': 2, 'hi': 1, 'all': 1, 'again': 1}
    assert question13(['hello hI all', 'HELLO again']) == {'hello': 2, 'hi': 1, 'all': 1, 'again': 1}
