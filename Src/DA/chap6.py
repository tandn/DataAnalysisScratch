from __future__ import division
from collections import Counter
from matplotlib import pyplot as plt
import math
import random

def uniform_pdf(x):
    return 1 if x >= 0 and x < 1 else 0

def uniform_cdf(x):
    if x < 0: return 0
    elif x < 1: return x
    else: return 1

def normal_pdf(z, mu=0, sigma=1):
    co = math.sqrt(2* math.pi) * sigma
    return (math.exp(-(z-mu) ** 2 / 2 / sigma ** 2) / co)

def normal_cdf(x, mu=0, sigma=1):
    return ((1 + math.erf((x-mu) / sigma / math.sqrt(2))) /2)

def bernoulli_trial(p):
    return 1 if random.random() < p else 0

def binomial_pdf(n,p):
    return sum([bernoulli_trial(p) for _ in range(n)])

def experiment1(n, p, times):
    data = [binomial_pdf(n, p) for _ in range(times)]
    mu = n*p
    sigma = math.sqrt(n*p*(1-p))

    histogram = Counter(data)
    plt.bar([i - 0.4 for i in histogram.keys()], [v / times for v in histogram.values()], 0.8)

    xs = range(min(data), max(data) + 1)
    ys = [normal_cdf(x + 0.5, mu, sigma) - normal_cdf(x - 0.5, mu, sigma) for x in xs]
    plt.plot(xs,ys,linestyle='solid')

    plt.show()

def draw(n):
    mu = 5/2
    sigma = math.sqrt(5) / math.sqrt(12)
    return (((sum(random.random() for _ in range(n))) - mu) / sigma)

def experiment2(n, times):
    data = [draw(n)  for _ in range(times)]
    histogram = Counter(data)
    print(histogram)
    plt.bar(histogram.keys(), [v for v in histogram.values()])

    xs = [x / 10.0 for x in range(-50, 50)]
    ys = [normal_pdf(x,sigma=1) for x in xs]
    plt.plot(xs,ys,linestyle='solid')

    plt.show()

experiment2(5, 40)
