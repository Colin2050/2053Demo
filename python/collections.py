#list
cart = ["apples", "bananas", "pears"]
print(cart)
cart.append("donuts")
cart.append("eggs")
cart.append("milk")
print (cart)
cart.remove("bananas")
print(cart)
if "apples" in cart:
    print("apples are in the cart")

cart.pop(2)
print(cart)
cart.reverse()
print(cart)
cart.sort()
print(cart)
cart.append("grapes")
cart.append("apples")
cart.append("oranges")
fruit_basket=cart[3:]
print(fruit_basket)
squares=[]
for i in range(11):
    squares.append(i**2)
print(squares)
squares=[i**2 for i in range(11)]
print(squares)
nums_set={1,1,3,4}
print(nums_set)