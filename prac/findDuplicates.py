from collections import Counter
list1=[1,2,3,4,5,5,6,7,7,8]

#method1
# my_set = set()
# duplicate=[]
# for i in list1:
#     if i not in my_set:
#         my_set.add(i)
#     else:
#         duplicate.append(i)
# print(duplicate)
# print(my_set)

#method 2
counts = Counter(list1)
duplicates = [item for item,count in counts.items() if count>1]
print(duplicates)

#method 3
duplicates=[]
for item in list1:
    if list1.count(item) > 1:
        if item not in duplicates:
            duplicates.append(item)
print(duplicates)

    

    

