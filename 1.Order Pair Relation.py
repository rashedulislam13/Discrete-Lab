from itertools import product

S = {1,2,3,4}
print("Set A"+ str(S))


R1 = [(a,b) for a,b in product(S,repeat=2) if a%b==0 or b%a == 0]
R2 = [(a,b) for a,b in product (S,repeat=2) if a<=b]

print("The pair list is for a/b:"+str(R1))
print("The pair list is for a<=b:"+str(R2))
