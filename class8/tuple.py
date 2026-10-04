a=(10,20,30,40)
sum=0
average=0
for i in range(len(a)):
    sum= a[i]+sum
    average = sum / len(a)

print (sum)
print(average)