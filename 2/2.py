import math

a = [2,3,4,5,6]
print(a)

n = len(a)
def mean(a):
    mean = sum(a) / n
    return mean

def find_sum(a):
    sum_ = sum(a)
    return sum_

def variance(a):
    n = len(a)
    mean = sum(a) / n
    return sum((x - mean) ** 2 for x in a) / (n)

def stddev(a):
    var = variance(a)
    std_dev = math.sqrt(var)
    return std_dev

print("Mean of a: %s" %(mean(a)))
print("Sum of a: %s" %(find_sum(a)))
print("Standard Deviation of a: %s" %(stddev(a)))
