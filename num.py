# name="sanjay"
# # print(name[0:3])
# list1 = [1, 2, 3, 4, 5]
# list2 = [6, 7, 8, 9, 10]
# ziplist=(list(zip(list1, list2)))
# flatList= [item for sublist in ziplist for item in sublist]
# print(flatList)
# # print(list1[0:3])

import datetime
year = int(input("year of birth : "))
print(f" age is : {datetime.datetime.now().year - year}")  
