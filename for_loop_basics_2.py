# 1. Biggie Size
def biggieSize(list):
    for i in range(len(list)):
        if list[i] > 1:
            list[i] = "Big"
    print(list)

# 2. Count Positives
def countPositives(list):
    count = 0
    for i in range(len(list)):
        if list[i] > 0:
            count+=1
    list[len(list)-1] = count
    print list

# 3. SumTotal
def sumTotal(list):
    sum = 0
    for value in list:
        sum+=value
    return sum

# 4. Average
def average(list):
    sum = 0
    for value in list:
        sum += value
    avg = sum/len(list)
    return avg

# 5. Length 
def length(list):
    return len(list)

# 6. Minimum
def minimum(list):
    if len(list) < 1:
        return False
    min = list[0]
    for i in list:
        if i < min:
            min = i
    return min

# 7. Maximum
def maximum(list):
    if len(list) < 1:
        return False
    max = list[0]
    for i in list:
        if i > max:
            max = i
    return max

# 8. UltimateAnalyze

def ultimateAnalyze(list):
    sum = 0
    min = list[0]
    max = list[0]
    dict = {}
    for i in list:
        sum+=i
        if i < min:
            min = i
        elif i > max:
            max = i
    dict["sum"] = sum
    dict["minimum"] = min
    dict["maximum"] = max
    dict["length"] = len(list)
    dict["average"] = sum/len(list)
    return dict

# 9. Reverse List
def reverseList(list):
    for i in range(0, int(len(list)/2)):
        temp = list[i]
        list[i] = list[len(list)-1-i]
        list[len(list)-1-i] = temp
    return list