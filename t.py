l1 = [1, 3, 5, 7, 9, 10]
l2 = [2, 4, 6, 8]
l1.pop(0)
l2.extend(l1)
l1 = l2
print(l1)

data = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
print(min(data, key=sum))

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
print({**dic1, **dic2, **dic3})

data = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5'), ]
data.sort(key=lambda item: item[1], reverse=True)
print(data)

gcd = lambda a, b: a if b == 0 else gcd(b, a % b)
print(gcd(18, 24))
