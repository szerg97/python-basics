x = 5
y = "John"
print(x)
print(y)

#casting
x = str(3)  # x will be '3'
y = int(3)  # y will be 3
z = float(3)  # z will be 3.0
print(x)
print(y)
print(z)

a, b, c = "Orange", "Banana", "Cherry"
print(a)
print(b)
print(c)

d = e = f = "Orange"
print(d)
print(e)
print(f)

#unpack a collection
fruits = ["apple", "banana", "cherry"]
g, h, i = fruits
print(g)
print(h)
print(i)

#output
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#sum
x = 5
y = 10
print(x + y)


def myfunc():
    global x
    x = "fantastic"


myfunc()

print("Python is " + x)
