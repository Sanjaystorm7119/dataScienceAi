#find dup using list comprehension
from collections import Counter
myList = [1,2,3,4,5,5,6,6,7,7,8]
duplicates = [value for value,count in Counter(myList).items() if count>1]
print(duplicates)