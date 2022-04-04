import re

T = int(input())
arr = []
for i in range(T):
    arr.append(input())

__SIGN__ = '+-'
__NUMBER__ = '0123456789.'

def func(s):
    count = 0
    if s.count('+') > 1 or s.count('-') > 1 or s.count('.') > 1:
        return False
    for i in range(len(s)):
        if s[i] in __SIGN__:
            count += 1
        if not re.search('([0-9][+-])', s[i]):
            return False
    if count != 1:
        return False
    return True

for i in range(T):
    print(func(arr[i]))