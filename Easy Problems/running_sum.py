#Given an array nums. We define a running sum of an array as runningSum[i] 
# sum(nums[0]…nums[i]).


# getting input:
array = [3,1,2,10,1]
answer = list()


# simple loop for running counter
index = 1
while index <= len(array):
    result = 0 # reset result
    for x in range (0,index):
        result += array[x]
    answer.append(result)  
    index = index + 1

print(answer)