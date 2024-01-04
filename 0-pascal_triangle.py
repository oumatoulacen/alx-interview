#!/usr/bin/python3
'''define a pascxal triangle function'''

def pascal_triangle(n):
    if n <= 0:
        return []

    result = [[1]]
    for i in range(n - 1):
        x = 0
        arr = []
        result[i].append(0)
        for j in range(len(result[i])):
            arr.append(x + result[i][j])
            x = result[i][j]
        result.append(arr)
    result[-1].append(0)
    return [res[:-1] for res in result]
