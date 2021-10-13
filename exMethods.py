from functools import reduce
# Map method
"""
liste = [1, 2, 3, 4, 5]
doubleList = list(map(lambda x: x**2, liste))
print(doubleList)
"""
# Sum with reduce method
"""
def toplama(a, b):
    return a+b


liste = [1, 2, 3, 4, 5]

print(reduce(toplama, liste))
"""
# Sorting with reduce method
"""
def maksimum(a, b):
    if(a > b):
        return a
    else:
        return b

print(reduce(maksimum, [1, 5, 2, 3, 6, 9, 15, 10, 7, 11, 13]))
"""

# Sum numbers 1...n
#print(reduce(lambda x, y: x+y, range(1, 10)))


# Filter method gets a iterational(list, tuple, ...) and return only true values
"""
liste = list(filter(lambda x: x % 2 == 0, range(0, 11)))
print(liste)
"""

# Find prime numbers in list
"""
def isPrime(x):
    if(x == 1):
        return False
    elif(x == 2):
        return True
    else:
        i = 2
        while (i < x):
            if(x % i == 0):
                return False
            i += 1
    return True

print(list(filter(isPrime, range(0, 101))))
"""

# Zip method is use for grouping 2 or more list
#print(list(zip(range(0, 50), range(50, 100))))

# Enumarate returns list values with their indexes
#print(list(enumerate([1, 2, 3, 4, 5, 6])))

# All method returns True if all values true
# Any method returns True even if only 1 value is true
