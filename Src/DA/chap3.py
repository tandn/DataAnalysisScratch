## line chart
from matplotlib import pyplot as plt
from collections import Counter

"""years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

# create a line chart, years on x-axis, gdp on y-axis
plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

# add a title
plt.title("Nominal GDP")

# add y label
plt.ylabel("B of $")
plt.xlabel("Years")

# display
plt.show()"""


## bar type

"""movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

xs = [i+0.1 for i,_ in enumerate(movies)]

plt.bar(xs, num_oscars)

plt.title("My favor")
plt.ylabel("# of awards")
plt.xlabel("Movie names")

plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)

plt.show()
"""

def map(f, l):
    return [f(i) for i in l]

scale = lambda x : x / 10 * 10

grades = [83,95,91,87,70,0,85,82,100,67,73,77,0]

histogram = Counter(map(scale,grades))

print(histogram)

plt.bar([x - 4 for x in histogram.keys()], histogram.values(), 8)

plt.xlabel("Scaled")
plt.ylabel("# Students")
plt.axis([-5, 105, 0, 5])
plt.xticks([10 * i for i in range(11)])
plt.show()
