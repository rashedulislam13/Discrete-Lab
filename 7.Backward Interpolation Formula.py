from math import factorial

# read input value from file

x, y = [ 1,2,3,4,5,6,7,8], [1,8,27,64,125,216,343,512]


# Value to interpolate at

print("\nBackward difference table: ")

# Calculating the backward difference table
table = [y]
for l in range(len(y) - 1):
    yn = []
    for i, k in zip(y[1::1], y[0::1]):
        yn.append(i - k)
    table.append(yn)
    y = yn

# Displaying the backward  difference table
formated_table = ["x", "f(x)", "∇f(x)"]
for i in range(2, len(table)+1):
    formated_table.append("∇^" + str(i) + "f(x)")
for i in range(len(table)+1):
    print(formated_table[i], end=" \t");
print()
for i in range(len(table)):
    print(x[i], end="  \t");
    for j in range(len(table) - i):
        if j>1:
            print(end="\t")
        print(table[j][i], end="\t\t");
    print();

# calculation of r
r = (inp - x[-1]) / (x[1] - x[0])
# result calculation
r_component = 1
partial_result = 0
for i in range(1, len(table)):
    r_component = r_component * (r + i - 1)
    partial_result = partial_result + (table[i][-1] * r_component) / factorial(i)
final_result = table[0][-1] + partial_result

# Printing Result
print("\nValue of", "f(",inp,") is : ", final_result);
