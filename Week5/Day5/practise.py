# write a function that takes a list of numbers
# return a total of those numbers 

def total_sum(numbers): 
    total = 0 
    for n in numbers: 
        total += n
    return total

answer = total_sum([1,2,3])
print(answer)
