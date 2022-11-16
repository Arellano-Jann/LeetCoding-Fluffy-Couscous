def solution(numbers):
    res = []
    for i in range(1, len(numbers)-1):
        left = numbers[i-1]
        right = numbers[i+1]
        mid = numbers[i]
        if left < mid > right or left > mid < right:
            res += [1]
        else:
            res += [0]
    return res


    

def solution(a, b, k):
    res = 0
    for left, right in zip(a, b[::-1]):
        lst = [str(left), str(right)]
        total = int(''.join(lst))
        if total < k:
            res += 1
    return res




from numpy import mean
from collections import defaultdict

def solution(a):
    res = []
    means = {}
    means_reverse = defaultdict(list)
    for i in range(len(a)):
        avg = mean(a[i])
        means[i] = avg
        means_reverse[avg].append(i)
    # for key, val in means.items():
    #     pass
    for key, val in means_reverse.items():
        res.append(val) 
    # print(means, means_reverse)
    return res



def solution(queryType, query):
    total_val = 0
    total_key = 0
    total_get = 0
    hashmap = {}
    
    # def insert(x, y):
    #     hashmap[x-total_key] = y - total_val
    # def get(x):
    #     total_get += hashmap[x - total_key] + total_val
    # def addToKey(x):
    #     total_key += x
    # def addToValue(y):
    #     total_val += y
    
    for command, param in zip(queryType, query):
        x = param[0]
        y = param[-1]
        if command == 'insert':
            # insert(param[0], param[1])
            hashmap[x-total_key] = y - total_val
        if command == 'get':
            # get(param[0])
            total_get += hashmap[x - total_key] + total_val
        if command == 'addToKey':
            # addToKey(param[0])
            total_key += x
        if command == 'addToValue':
            # addToValue(param[0])
            total_val += x

    return total_get