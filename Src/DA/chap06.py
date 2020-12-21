# approximate binomial distribution by normal distribution
from __future__ import division
from matplotlib import pyplot as plt
from collections import Counter
import random
import math

# helper function
def fact(n):
    def go(n, acc):
        if n == 0: return acc
        else: return go(n-1, acc*n)
    return go(n,1)

def binomial(n, p, k):
    """binomal X can be approximated by poison limit, as long as np = constant"""
    mu = n*p
    return (math.exp(-mu) * (mu ** k)) / fact(k)

"""
test = [binomial(100, 1/100, k) for k in range(0,10)]
for i,j in enumerate(test):
    print i,j
"""

# standard pdf function for z with mu and sigma
def normal_pdf(z, mu=0, sigma=1):
    denom = math.sqrt(2*math.pi) * sigma
    return math.exp(- (((z-mu) / sigma) ** 2) / 2 ) / denom

def normal_cdf(z, mu=0, sigma=1):
    return (1 + math.erf( (z-mu) / sigma /  math.sqrt(2))) / 2

def bernoulli_trial(p):
    return 1 if random.random() < p else 0

def binomial2(n, p):
    return sum(bernoulli_trial(p) for _ in range(n))

def simulation(n, p, times):
    data = [binomial2(n, p) for _ in range(times)]
    histogram = Counter(data)
    xs = histogram.keys()
    ys = [v / times for v in histogram.values()]
    plt.bar(xs,ys,color='white')
    plt.show()

def experiment(n, p):
    data = [binomial(n, p, i) for i in range(0,n+1)]
    xs = range(0,n+1)
    ys = data
    plt.bar(xs, ys, color='grey')
    plt.ylabel("Probability")

    mu = n*p
    sigma = math.sqrt(n*p*(1-p))
    zs = [normal_pdf(z, mu, sigma) for z in xs]
    #zs = [normal_cdf((z + 0.5 - mu)/sigma , 0, 1) - normal_cdf((z - 0.5 - mu) / sigma, 0, 1) for z in xs]
    plt.plot(xs, zs, linestyle='solid', color='green')

    plt.show()

experiment(20, 1/2)
#simulation(100, 3/4, 1000)
