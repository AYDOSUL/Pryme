import math, time

primelist = [2]


def Sieve(num):
    reps = 0
    while len(primelist) > reps:
        if num % primelist[reps] == 0:
            return False
        else:
            if len(primelist) < reps:
                return True
            else:
                reps = reps + 1
start = 2
cycletime = 1
searchfield = int(input('Field of search for the program: '))
maxtime = int(input('Maximum amount of time the program is allowed to run(s):'))
numsfound = 0

startclock = time.time()
print('2')
while cycletime < searchfield:
    if Sieve(start) == None:
        if start > searchfield:
            break

        if (time.time() - startclock) > maxtime:
            break

        print(start, time.time() - startclock)
        primelist.append(start)
        start = start + 1
        cycletime = cycletime + 1
        numsfound = numsfound + 1
    else:
        start = start + 1
        cycletime = cycletime + 1
endclock = time.time()

print('Prime Numbers Found:')  
print(numsfound + 1)  

print('Largest Prime:')
print(start)

print('Elapsed time:')
print(endclock-startclock)