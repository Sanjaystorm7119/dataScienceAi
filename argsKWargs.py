def super_fun(*args,**kwargs):
    return sum(args)+sum(value for value in kwargs.values())
print(super_fun(1,2,3,4,num1=10,num2=10))