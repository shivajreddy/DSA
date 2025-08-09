# 118 - Pascal's Triangle

def generate(numRows):
    if numRows == 1:
        return [[1]]
    if numRows == 2:
        return [[1],[1,1]]

    result = [[1], [1,1]]

    while numRows > 2:
        current = result[-1] 

        nxt = [1]

        for i in range(len(current)-1):
            nxt.append(current[i]+current[i+1])
        nxt.append(1)

        result.append(nxt)

        numRows -= 1

    return result


print(generate(1))
print(generate(5))
print(generate(6))