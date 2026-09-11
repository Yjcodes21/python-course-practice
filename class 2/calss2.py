# the class is about the operators in the python so here are the basics operators questions 

#it is the canndies question and on which we have to equally distribute candies to the n no of children and candies are also n and also give the output of the remaining candies 

total_no_of_candies = int(input("total no of candies:- "))
total_no_of_children = int(input("total no of children:- "))

candies_per_kid = total_no_of_candies // total_no_of_children
remaining_candies = total_no_of_candies % total_no_of_children

print(f"candies per kid is :- {candies_per_kid} remaing candies :- {remaining_candies}")