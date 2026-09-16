#here we learn about data structures 1- list[] , 2- tuple() , 3-dictionary{}

# 1- List

import copy
a= [2.3,2.0,3.20,4.40]

b= copy.deepcopy(a)

b[0]= 100

print("here is teh list a:-",a) 
print("here is teh list b:-",b)