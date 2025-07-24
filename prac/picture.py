picture =[
    [0,0,0,1,0,0,0],  
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],  
    [0,0,0,1,0,0,0],  
]

# for i in range(len(picture)):
#     for j in range(len(picture[i])):
#         if picture[i][j]==0:
#             print("_" , end="")
#             print("")
#         else:
#             print("*" , end="")

fill="*"
empty=" " 
for image in picture:
    for pixel in image:
        if pixel==1:
            print(fill,end=" ")
        else:
            print(empty, end=" ")
    print("")