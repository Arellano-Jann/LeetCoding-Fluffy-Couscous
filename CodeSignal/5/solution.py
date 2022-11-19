def problem1(a):
    b = []
    for i in range(len(a)):
        left = a[i-1] if 0 <= i-1 < len(a) else 0
        right = a[i+1] if 0 <= i+1 < len(a) else 0 
        b.append(left + a[i] + right)
    return b

def problem2(pattern, source):
    vowels = 'aeiouy'
    source = ['0' if x in vowels else '1' for x in source ]
    source = ''.join(source)
    source_length = len(source)
    pattern_length = len(pattern)
    res = 0
    for i in range(source_length - pattern_length + 1):
        if source[i:i+pattern_length] == pattern:
            res += 1
    return res

def problem3(s1, s2):
    s1_map = {}
    s2_map = {}
    
    for i in s1:
        s1_map[i] = 1 + s1_map.get(i, 0)
    for i in s2:
        s2_map[i] = 1 + s2_map.get(i, 0)
    
    return

def problem4(a, k):
    def valid(current_length):
        pieces = 0
        for piece in a:
            pieces += piece // current_length
        return True if pieces >= k else False
        
    
    max_len = max(a)
    left, right = 1, max_len
    while left + 1 < right:
        mid = (left + right) // 2
        if valid(mid):
            left = mid
        else:
            right = mid - 1
    if valid(right):
        return right
    if valid(left):
        return left
    else:
        return 0