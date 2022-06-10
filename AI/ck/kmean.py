import random as rd
import numpy as np

D = [(3, 12), (6, 9), (4.5, 12), (12,  3),
     (15,  6), (12, 15), (9, 18), (9, 12)]


def distance(a, b):
    dis = 0
    for i in range(len(a)):
        dis += (a[i] - b[i])**2
    return dis


def argminDistance(p, mu):
    id = -1
    mindis = 0
    for i in range(len(mu)):
        dis = distance(p, mu[i])
        if id == -1 or mindis > dis:
            mindis = dis
            id = i
    return id


def mySum(a, b):
    s = [0] * len(a)
    for i in range(len(a)):
        s[i] = a[i] + b[i]
    return s


def kmean(D, k):
    n = len(D)
    mu = rd.sample(D, k)
    C = [0] * n
    while True:
        cothaydoi = False
        for i in range(n):
            c = argminDistance(D[i], mu)
            if (C[i] != c):
                cothaydoi = True
            C[i] = c
        if not cothaydoi:
            break
        mu = [tuple([0] * len(mu[0]))] * len(mu)
        sl = [0] * len(mu)
        for i in range(n):
            mu[C[i]] = mySum(mu[C[i]], D[i])
            sl[C[i]] += 1
        for i in range(len(mu)):
            if sl[i] == 0:
                mu[i] = rd.choice(D)
            else:
                mu[i] = [x // sl[i] for x in mu[i]]
    return C, mu


print(kmean(D, 3))
