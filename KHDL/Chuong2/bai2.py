import csv
from math import floor
from statistics import median

def getCol(ld, key):
    result = []
    for i in range(len(ld)):
        result.append(ld[i][key])
    return result
        
def Mean(array):
    array = [float(item) for item in array]
    return sum(array) / len(array)

def WeightMean(array, w):
    array = [float(item) for item in array]
    w = [float(item) for item in w]
    return sum(array[i] * w[i] / sum(w) for i in range(len(w)))

def Round(n):
    if n - int(n) == 0.5:
        if int(n) % 2 == 0:
            return round(n) + 1
    return round(n)

def TrimMean(array, percent):
    percent = float(percent)
    n = len(array)
    array = [float(item) for item in array]
    array.sort()
    k = Round(n * percent / 100)
    arr = array[k + 1 : n - k]
    return sum(arr) / len(arr)

def Median(array):
    array = [float(item) for item in array]
    array.sort()
    n = len(array)
    k = floor(n / 2)
    if n % 2 == 0:
        result = (array[k] + array[k - 1]) / 2
    else:
        result = array[k]
    return result

with open('Chuong2/state.csv') as f:
    reader = csv.DictReader(f)
    data = [row for row in reader]

# for row in data:
#     print(row)
murderRate = getCol(data, 'Murder.Rate')
murderRate = [float(item) for item in murderRate]

print(Mean(murderRate))

population = getCol(data, 'Population')
population = [float(item) for item in population]
population = [item / sum(population) for item in population]
# for item in population:
#     print(item)
# print(sum(population))
print(WeightMean(murderRate, population))
# from numpy import average
# print(average(murderRate, weights=population))

print(TrimMean(murderRate, 5))
# from scipy import stats
# import pandas as pd
# print(stats.trim_mean(murderRate, 0.05))

print(Median(murderRate))
# print(median(murderRate))