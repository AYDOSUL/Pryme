import math, random

def TrialDivCheck(num):

    if num < 2:
        return False

    else:
        for i in range(2, round(math.sqrt(num) + 1)):
            if num % i == 0:
                return False
        return True

#Rabin-Miller Primality written by Al Sweigart
def rabinMillerTest(num):
    # Returns True if num is a prime number.
    if num % 2 == 0 or num < 2:
        return False # Rabin-Miller doesn't work on even integers.
    if num == 3:
        return True
    s = num - 1
    t = 0
    while s % 2 == 0:
        # Keep halving s until it is odd (and use t
        # to count how many times we halve s):
        s = s // 2
        t += 1
    for trials in range(5): # Try to falsify num's primality 5 times.
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1: # (This test does not apply if v is 1.)
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num
    return True
def fermatPrimeTest(num):
    cyclenum = round((math.sqrt(num))/2)
    if num % 2 == 0:
        return False
    else:
        cycletotal = 0
        while cyclenum + 1 != cycletotal:
            divnum = random.randrange(2, round(math.sqrt(num)))
            if num % divnum == 0:
                return False
            else: 
                cycletotal = cycletotal + 1
        return True

def FullCheck(num):
    if fermatPrimeTest(num) == True:
        if rabinMillerTest(num) == True:
            if TrialDivCheck(num) == True:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

start = 6
cycletime = 1
searchfield = int(input('How many numbers do you want to search through? '))
print('2')
print('3')
print('5')
numsfound = 0
while cycletime < searchfield:
    if FullCheck(start) == True:
        print(start)
        start = start + 1
        cycletime = cycletime + 1
        numsfound = numsfound + 1
    else:
        start = start + 1
        cycletime = cycletime + 1

print('Prime Numbers Found:')  
print(numsfound + 3)  