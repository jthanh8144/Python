import csv
from math import floor
import numpy as np

def getCol(ld, key):
    result = []
    for i in range(len(ld)):
        result.append(ld[i][key])
    return result
        
def Mean(array):
    array = [float(item) for item in array]
    return sum(array) / len(array)

def Variance(array):
    array = [float(item) for item in array]
    m = Mean(array)
    return sum((item - m)**2 for item in array) / len(array)

def STD(array):
    return Variance(array)**0.5

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

def MAD(array):
    m = Median(array)
    return Median([abs(item - m) for item in array])

with open('Chuong2/state.csv') as f:
    reader = csv.DictReader(f)
    data = [row for row in reader]

population = getCol(data, 'Population')
population = [float(item) for item in population]
# print(STD(population))
# print(np.std(population))

print(MAD(population))

