print("Hello World!")
# this is a single line comment

'''
This is a multi-line comment
This is a multi-line comment
This is a multi-line comment
'''
# line 1
# line 2
# line 3
x=10
x="hello"
x = [1,2,3]
print(x)
x = 100
y = 10
z = x + y
print(z)
raised = pow(2,3)
print(raised)
raised = 2**3
print(raised)
x = -1
y - 0
if x<0:
    print("x is negative")
elif x>0:
    print("x is positive")
else:
    print("x is zero")

counter = 0
while counter<5:
    print(counter)
    counter+=1
    for i in range(5):
        print(i)
lst=[1,2,3,4,5]
for i in range(len(lst)):
    print(i, lst[i], end = " ")
print()

for val in lst:
    print(val)

for i, val in enumerate(lst):
    print(i, val, end=" ")
print()
def hello(name):
    print("Hello", name)
hello("world")