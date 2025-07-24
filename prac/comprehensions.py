# name = "jay"
# my_list = [char for char in name]
# print(my_list)

nums = [num**2 for num in range(0,101) if num%2==0]
print(nums)

#set comprehension

name = "jay"
myset = {char for char in name}
print(myset)

nums = {num**2 for num in range(0,101) if num%2==0}
print(nums)

#dict comp

simpleDict = {
    "a":1,
    "b":2
}

mydict = {key:value**2 for key,value in simpleDict.items()}
print(mydict)
#list values as key and values
print({num:num*2 for num in [1,2,3]})