import random

boys = ['mohammad', 'sobhan', 'abdollah', 'kiya', 'mahdi', 'sajjad', 'homan', 'arman']
girls = ['mahtab', 'hane', 'harir', 'fateme', 'kiana', 'faezeh', 'minoo', 'mina', 'soghra']

results = []

for i in range(min(len(boys),len(girls))):
    boys = random.choice(boys)
    girls = random.choice(girls)
    result.append([boys,girls])
    boye.remove(boys)
    girle.remove(girls)

print("result=", result)
