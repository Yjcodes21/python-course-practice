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

a = [10 , 20 , 50 , 20 , 5]
max = a[0]
max2 = a[0]
index = 0
index2 = 0

for i in range(len(a)):
    if max < a[i]:
        max2 = max
        max = a[i]
        index2 = index
        index = i
print(f"the second greatest no is {max2} at the index of {index2}")
