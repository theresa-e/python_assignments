# 1. Basic - Print all the numbers/integers from 0 to 150.
for count in range(0, 251):
    print(count)

# 2. Multiples of Five - Print all the multiples of 5 from 5 to 1,000,000.
for count in range(5, 1000005):
    if count % 5 == 0:
        print(count)

# 3. Counting, the Dojo Way - Print integers 1 to 100.  If divisible by 5, print "Coding" instead. If by 10, also print " Dojo".
for count in range(1, 105):
    if count % 5 == 0 and count % 10 == 0:
        print(count, "Coding Dojo")
    elif count % 5 == 0:
        print(count, "Coding")
    elif count % 10 == 0:
        print(count, "Dojo")

# 4. Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
def onlyOdd():
    sum = 0
    for i in range(0, 101):
        if i % 2 != 0:
            sum+=i
    return(sum)

# 5. Countdown by Fours - Print positive numbers starting at 2018, counting down by fours (exclude 0).
for i in range(10, 0, -4):
    print(i)

# 6. Flexible Countdown - Based on earlier "Countdown by Fours", given lowNum, highNum, mult, print multiples of mult from lowNum to highNum, using a FOR loop.  For (2,9,3), print 3 6 9 (on successive lines)

def flexCountdown(lowNum, highNum, mult):
    for i in range(highNum, lowNum, -(mult)):
        print(i)

flexCountdown(2, 9, 3)