a = [3,0,1]
b = [4,5,6]

c = sum([a_elem * b_elem for a_elem, b_elem in zip(a,b)])
print(c)