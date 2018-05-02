def a():
    return 5
print(a())

# Prediction: Will print 5.
# Results: Shell printed 5.

def a():
    return 5
print(a()+a())

# Prediction: Will print 10.
# Results: Shell printed 10.

def a():
    return 5
    return 10
print(a())

# Prediction: Will print 5.
# Results: Shell printed 5.

def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a)

# Prediction: Shell will print an error because we did not call our function.
# Results: Shell printed <function a at 0x10afbab90>

def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))

# Prediction: Will print 7, 14, 21.
# Results: Shell printed 7, 14, 21.

def a(b,c):
    return b+c
    return 10
print(a(3,5))

# Prediction: Will print 8.
# Results: Shell printed 8. 

b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)

# Prediction: Shell will print 500, 500, 300, 500
# Shell printed 500, 500, 300, 300

b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)

# Prediction: Shell will output 500, 300, 500, 500
# Results: Shell printed 500, 500, 300, 500

b = 500
print(b)
def a():
    b=300
    print(b)
    return b
print(b)
b=a()
print(b)

# Prediction: Shell will print 500, 500, 300, 300
# Results: Shell printed 500, 500, 300, 300