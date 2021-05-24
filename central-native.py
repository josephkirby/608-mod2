values = [47, 95, 88, 73, 88, 84]

print(len(values))
print(sum(values))
print(sum(values)/len(values))

# median - with help from https://www.geeksforgeeks.org/finding-mean-median-mode-in-python-without-libraries/
values = sorted(values)
if len(values) % 2 == 0:
    upper = values[len(values)//2]
    lower = values[len(values)//2-1]
    print((lower+upper)/2)
else:
    print(values[len(values)//2])

# mode - with help from https://www.geeksforgeeks.org/finding-mean-median-mode-in-python-without-libraries/
valuescount = []
x = 0
while x < len(values):
    valuescount.append(values.count(values[x]))
    x += 1

dictionary = dict(zip(values,valuescount))
print({k for (k,v) in dictionary.items() if v == max(valuescount)})