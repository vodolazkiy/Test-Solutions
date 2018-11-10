# Given a list containing integers in order, for example: [1, 3, 5, 8, 12, 13, 22] and a target number, for example 16.
#
# Can you find a pair of numbers whose sum equals the target number?
#
# From https://notebooks.rmotr.com/santiagobasulto/google-interview-question-9f26238f/1.+Introduction.ipynb

l = # Any array of integers
target = # Any integer
solutions, answer = [], []

while True: #Cleans the array of values that couldn't possible be part of the sum.
    final = len(l) - 1
    tail = len(l) / 10 
    test = int(final - tail) # Top 10% removed. Adjust the integer in tail to adjust the number of values tested for cropping.
    if l[test] > target:
        del l[test:]
        continue
    else:
        break

for i in l:
    if i == target: # If the array contains the target value, this removes the value from the array and adds it as a solution.
        solutions.append(i)
        del i
    elif i > target: # Cleans the array of any lingering impossible solutions before heavy iteration to speed it up.
        del i
    else:
        for pair in l:
            if l.index(i) == l.index(pair): # Prevents a given value from testing against itself.
                continue
            elif target == i + pair:
                solutions.append([i, pair])
                del pair
            else:
                continue

for i in solutions: # Removes duplicates so that only unique solutions are ultimately returned.
    if type(i) is list:
        i.sort()
        if i not in answer:
            answer.append(i)
    else:
        answer.append(i)

print("These are the solutions: ")
for i in answer:
    print(i)
print("Total number of solutions:")
print(len(answer))
