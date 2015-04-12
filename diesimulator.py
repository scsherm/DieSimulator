#Load modules
import random
import numpy as np

#Empty lists for carry over values & # of rolls
carry_over1, carry_over2, roll_count1, roll_count2 = [], [], [], [] 
loop = 0

#Define die_sim function
def die_sim(die_size, total_sum): 
    die_sum = 0 #Set the initial sum equal to zero
    die_list = [] #Create empty list
    while die_sum < total_sum:
            roll = random.randint(1,die_size)
            die_list.append(roll) #Add random number between 1 & 6 to list 
            die_sum += roll #calculate sum
    return die_sum, die_list, total_sum

#Calculate mean and standard dev. for sum >= 20
for i in range(1000): #Range determined by where the highest number converges
    die_sum, die_list, total_sum = die_sim(6,20)
    carry_over1.append(die_sum - total_sum) #Calculate value over 20
    roll_count1.append(len(die_list)) #Count number of rolls

#Print mean and standard deviation
print("mean carry over (sum >= 20):", round(np.mean(carry_over1), 1))
print("std carry over (sum >= 20):", round(np.std(carry_over1), 1))
print("mean number of rolls (sum >= 20):", round(np.mean(roll_count1), 1))
print("std number of rolls (sum >= 20):", round(np.std(roll_count1), 1))

#Calculate mean and standard dev. for sum >= 10000
for i in range(100000): #Ran for loop a few times 
    die_sum, die_list, total_sum = die_sim(6,10000)
    carry_over2.append(die_sum - total_sum) #Calculate value over 10000
    roll_count2.append(len(die_list)) #Count number of rolls

#Print mean and standard deviation
print("mean carry over (sum >= 10000):", round(np.mean(carry_over2), 1))
print("std carry over (sum >= 10000):", round(np.std(carry_over2), 1))
print("mean number of rolls (sum >= 10000):", round(np.mean(roll_count2), 1))
print("std number of rolls (sum >= 10000):", round(np.std(roll_count2), 1))    