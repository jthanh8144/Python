# Yêu cầu bài tập:
# Hãy tìm chu trình ngắn nhất đi qua n điểm trên không gian 2 chiều
import random as rd
import math

n = 100
p = [(rd.randint(0,10000),rd.randint(0,1000)) for _ in range(n)]
print(p)

def distance(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

