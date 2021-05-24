import random
import statistics

# create a blank list
mylist = []

# fill the blank list with 1000 random numbers between 1 and 100
while len(mylist) < 1000:
    mylist.append(random.randint(1,100))

print(len(mylist))
print(sum(mylist))
print(statistics.mean(mylist))
print(statistics.median(mylist))
print(statistics.mode(mylist))