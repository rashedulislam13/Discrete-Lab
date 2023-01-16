import numpy as np

A = {1,2,3}
B = {1,2}

# using list comprehension
R = [(a, b) for a in A for b in B if a > b]
Matrix = [1 if a>b else 0 for a in A for b in B]
arr = np.array(Matrix)
newarr = arr.reshape(3,2)
print("R = ",R)
print("Matrix  R = ")
for x in range(len(newarr)):
    print("\t\t",newarr[x])
