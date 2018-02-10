from __future__ import division

"""Declaring users data in the form of a list of of users where each user is characterized by a dictionary"""
users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" }
]

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]


"""friendship information is denoted by a list of tuples
The social network is an undirectional graph """
friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

"""create attribute friends for each user"""
for user in users:
    user["friends"] = []

"""filling data for the friends key"""
for i, j in friendships:
    """This work because each users[i] give rise a user, which is in turn a dictionary"""
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])

def num_of_friend(user):
    """How many does this user have"""
    return len(user["friends"])

"""Calculate the total connections in the network"""
total_connections = sum(num_of_friend(user) for user in users)

"""Calculate the average number of connections"""
num_users = len(users)
avg_connections = total_connections / num_users


"""Sort users according to the number of friends they have"""
number_friends_by_id = [(user["id"], num_of_friend(user))
                        for user in users]
sorted(number_friends_by_id, key = lambda (user_id, num_friends): num_friends, reverse = True)

#print(number_friends_by_id)

def friend_you_might_know(user):
    return [floaf["id"]
            for friend in user["friends"]
            for floaf in friend["friends"]]

#print(friend_you_might_know(users[0]))


def people_who_like(topic):
    return [user_id
           for user_id, interest in interests
           if interest == topic]

print(people_who_like("Hadoop"))



from matplotlib import pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

plt.title("Nomial GDP")

plt.ylabel("Billions of $")
#plt.show()
