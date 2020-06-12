# To declare 1D-array of 5 rows and 7 cols with value 0.
arr = [[0 for i in range(5)] for j in range(7)]
arr[0][1] = 10
print(arr)

# Avoid this. Because it uses shallow lists. It references same copy.
arr = [[0] * 5] * 7
arr[0][1] = 10
print(arr)
