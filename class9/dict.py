#ques is calculate the frequqency in the given list 

a= [1,2,1,3,2,3,1,4,2,3,3,3,4,1,2,3,4]
d = {}

for i in a:
    if i in d.keys():
        d[i] += 1
    else:
        d[i]=1
print(d.keys())
print(d)
