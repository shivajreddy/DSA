# 118 - Pascal's Triangle

def generate(numRows):
    x = numRows
    result = [[1], [1,1], [1,2,1]]

    if numRows < 3:
        return result[numRows]

    while numRows > 2:
        current = result[-1] 

        nxt = [1]

        for i in range(len(current)-1):
            nxt.append(current[i]+current[i+1])
        nxt.append(1)

        result.append(nxt)
        numRows -= 1

    return result[x]


print(generate(0))
print(generate(1))
print(generate(2))
print(generate(3))
print(generate(5))
print(generate(6))