from functools import reduce
my_list=[1,2,3,4]

new_list = list(map(lambda value:value  * 2,my_list))
print(new_list)

even = list(filter(lambda value:value%2==0,my_list))
print(even)

red= reduce(lambda x,y:x+y , my_list,1)
print(red)