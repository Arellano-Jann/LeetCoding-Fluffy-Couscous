def problem1(numbers, left, right):
    res = []
    for i in range(len(numbers)):
        calc = numbers[i] / (i+1)
        print(calc, calc in numbers)
        if left <= calc <= right and calc.is_integer():
            res.append(True)
        else:
            res.append(False)
    return res

def problem2(numbers):
    def inverse(num):
        return int(str(num)[::-1])
    first_non_increasing = -1
    if len(numbers) == 1:
        return True
    for i in range(len(numbers)):
        # print(numbers[i] < numbers[i+1], inverse(numbers[i]) < numbers[i+1])
        if i == 0:
            if not numbers[i] < numbers[i+1]:
                first_non_increasing = i
                break
        elif i == len(numbers)-1:
            if not numbers[i-1] < numbers[i]:
                first_non_increasing = i-1
                break
        else:
            if numbers[i-1] < numbers[i] < numbers[i+1]:
                first_non_increasing = i
                break
    if first_non_increasing == -1:
        return True
    print(numbers[first_non_increasing])
    numbers[first_non_increasing] = inverse(numbers[first_non_increasing])
    print(numbers[first_non_increasing])
    for i in range(1, len(numbers)):
        if not numbers[i-1] < numbers[i]:
            return False
        
        
                
        # if (numbers[i] < numbers[i+1]):
        #     continue
        # elif (inverse(numbers[i]) < numbers[i+1]) and not swapped:
        #     swapped = True
        #     if not (numbers[i-1] < inverse(numbers[i])) and i > 0:
        #         return False
        #     continue
        # else:
        #     return False
    return True


def problem3(a, k):
    res = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if (a[i] + a[j]) % k == 0:
                res += 1
    return res
