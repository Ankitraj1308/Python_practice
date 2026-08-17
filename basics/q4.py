'''
Write a program that can find the max number of each row of a matrix
Example:

Input:

[[1,2,3],[4,5,6],[7,8,9]]
Output:

[3,6,9]
'''
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

result = []

for row in matrix:
    result.append(max(row))

print(result)


'''
Write a list comprehension that can transpose a given matrix
matrix = [
[1,2,3],
[4,5,6],
[7,8,9]
]

[1, 4, 7]
[2, 5, 8]
[3, 6, 9]
'''

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

print(transpose)