my_list=[1,2,4,6,10,8,12]
highest_even=0
for i in my_list:
    if i%2==0 and i > highest_even:
        highest_even = i
print(highest_even)