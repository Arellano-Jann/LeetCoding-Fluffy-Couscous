def problem1(a):
    res = []
    length = len(a)
    for x in range(length):
        left = x - 1
        right = x + 1
        left = a[left] if (0 <= left < length) else 0
        right = a[right] if (0 <= right < length) else 0
        res.append(left + a[x] + right)
    return res

def problem2(a):
    # if not a:
    #     return 0
    count = {}
    length = len(a)
    res = 0
    for num in range(length):
        temp = "".join(sorted(str(a[num])))
        count[temp] = 1 + count.get(temp, 0)
    for val in count.values():
        res += (val * (val-1)) // 2
    return res


def problem3(a):
    return -1
    
def split_digits(num):
    return [int(x) for x in str(num)]
    
def problem4(a):
    if not a:
        return []
    num_set = set()
    counter = {}
    most_num = 0
    for num in a:
        for digit in split_digits(num):
            counter[digit] = 1 + counter.get(digit, 0)
            if counter[digit] > most_num:
                most_num = counter[digit]
    for key, value in counter.items():
        if value == most_num:
            num_set.add(key)
    return sorted(list(num_set))
