#Ques1, so here we do the loops , first we strt from writing the table of the any number given by user

# number = int(input("enter your number which table u want:- "))

# for i in range (1,11):
#     print(number ,'x', '=', (number*i))


# Ques2 ,Note - as this code runs and now the new problem is u have to skip the 5th iteration

# number = int(input("enter your number which table u want:- "))

# for i in range (1,11):
#     if i == 5:
#         continue
#     print(number ,'x', i ,'=', number*i)

# Ques3- Now the ques is take the user input and count only positive numers 

number = list(map(int,input("enter your numbers here:- ").split()))
count = 0

for i in number:
    if i > 0:
        count +=1

print("positive numbers count:-",count)