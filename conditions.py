# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

a = 23
b = 4

if b > a:
    print('B is greater than A')
elif b < a:
    print('B is less than A')
else:
    print('B and A are equal')

a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")

a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")

