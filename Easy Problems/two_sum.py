#Question: Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.


# Getting input
array_num = list(map(int,raw_input("Please enter an array of numbers: ").split()))
target = map(int,raw_input("Please enter the target: "))

# Creating dictionary with Element and Comp Values
complement = list()
for i in array_num:
    complement.append(target[0] - i) 

dicti = dict(zip(array_num, complement))

# Want to look if Key has its complement

for i in array_num:
    if ((dicti[i] in dicti.keys())): # if complement is located in the keys, print element + Complement 
        print("The element is : %d and the the complement is %d " % (i,dicti[i]))
        break

