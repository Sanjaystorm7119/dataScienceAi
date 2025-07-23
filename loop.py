from collections import Counter 
# for item in "something":
#     print(item)

list1=[1,2,3,4]
for i in range(0,5,2):
    print(i)

for index,num in enumerate(list1):
    print(index,num)

count = Counter(list1)
print(count)


dic={
    "name":"golem",
    "game":"coc",
    "can_swim":True
}

for key,val in dic.items():
    print(key,val)

for item in dic:
    print(item)

for key in dic.keys():
    print(key)

for val in dic.values():
    print(val)