status = True
N1 = 5
N2 = 3
N3 = 4
arr1 = [2, 1, 1, 1, 1, 3]
arr2 = [1, 4, 3]
arr3 = [1, 1, 1, 4]

min = sum(arr1)
while not (sum(arr1) == sum(arr2) and sum(arr1) == sum(arr3)):
    if not arr1 or not arr2 or not arr3:
        status = False
        break
    if (sum(arr1) < min):
        min = sum(arr1)
    if (sum(arr2) < min):
        min = sum(arr2)
    if (sum(arr3) < min):
        min = sum(arr3)

    if (sum(arr1) != min):
        arr1.pop(0)
    if (sum(arr2) != min):
        arr2.pop(0)
    if (sum(arr3) != min):
        arr3.pop(0)

if status:
    print(sum(arr1))
else:
    print('Cannot create three equal arrays')