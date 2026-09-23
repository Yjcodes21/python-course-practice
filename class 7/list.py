# ok now here we learn about data structures in list and solve some questions 

#fques 1 find the sum and average of the numbers 
# print("ques 1")
# a= [ 10,20,30,40,50]
# sum = 0 

# for i in a:
#     sum = sum + i

# print(f"the sum of the given list is {sum}")
# print(f"the average of the given list is {sum/len(a)}")

#this is the version for the taking a user input
# print("")
# print("ques 1 upper variant")

# a= input("enter your numbers here but dont use comma use space :-").split()
# sum = 0 

# for i in a:
#     sum = sum + int(i)

# print(f"the sum of the given list is {sum}")
# print(f"the average of the given list is {sum/len(a)}")

# print("")
# print("ques 3")
#print the greatest no in the given list 

# a= [10 , 20 ,30 ,23, 43, 89, 45,67,23]
# max = 0
# index = a[0]

# for i in range (len(a)):
#     if a[i] > max :
#         max = a[i]
#         index = i
# print(f"the maximum no is {max} at the index value of ")

#print the 2nd greatest no in the list

# a = [10 , 20 , 50 , 20 ,93,91 , 5]
# max = a[0]
# max2 = a[0]
# index = 0
# index2 = 0

# for i in range(len(a)):
#     if max < a[i]:
#         max2 = max
#         max = a[i]
#         index2 = index
#         index = i
#     elif max2 < a[i] and a[i] != max:
#         max2 = a[i]
#         index2 = i
# print(f"the second greatest no is {max2} at the index of {index2}")
# here is the question of sorting to check the sorting , is the list sorted or not
# a = [10,20,30,40]
# for i in range(len(a)-1):
#     if a[i]< a[i+1]:
#         continue
#     else :
#         print("not sorted")
#         break
# else:
#     print(" sorted")

# here we go for the swaping left to right and right to left

# a= [10,20,23,32,12,32]
# b= [10,20,23,32,12,32]

# for i in range(len(a)-1):
#     a[i],a[i+1]=a[i+1],a[i]
# print (f"here is left to right swaping {a}")

# for i in range(len(b)-1,0,-1):
#     b[i],b[i-1]=b[i-1],b[i]
   
# print (f"here is  right to left  swaping {b}")

# if the ques says  n times u wanna roatate the list then 

# a= [10,20,30,40,50]
# n= int(input("enter the no for the times u wanna list rotate left:-"))

# for i in range(n):
#     for i in range(len(a)-1):
#         a[i],a[i+1]= a[i+1],a[i]
# print(a)
#reverse the list question
# a = [10,20,30,40,50,50]
# b = len(a)-1

# for i in range(len(a)//2):
#     a[i],a[b]=a[b],a[i]
#     b = b-1
# print(a)

# a = [10, 20, 30, 40, 50]

# search = 40

# start = 0
# last = len(a) - 1

# while start <= last:

#     mid = (start + last) // 2

#     if a[mid] == search:
#         print(f"The search is completed. {search} is at index {mid}")
#         break

#     elif a[mid] < search:
#         start = mid + 1

#     elif a[mid] > search:
#         last = mid - 1

# else:
#     print("The number isn't in the array")

a= [10,90,900,49,1,9,2,9999,384]
for j in range(len(a)-1):
    for i in range (len(a)-1-j):
        if a[i] > a[i+1]:
            a[i],a[i+1] = a[i+1],a[i]
print(a)