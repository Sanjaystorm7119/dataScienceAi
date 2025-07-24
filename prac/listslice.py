amazon_cart = ["laptop", "mouse", "keyboard", "monitor", "printer"]
#shallow copy - just a reference

# amazon_cart1= amazon_cart
# amazon_cart1[0]='pineapple'
# print(amazon_cart)
# print(amazon_cart1)

# deepcopy - new assigned

amazon_cart1= amazon_cart[:]
amazon_cart1[0]='pineapple'
print(amazon_cart)
print(amazon_cart1)
