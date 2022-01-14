from random import random, uniform, randrange, choice,shuffle

random = random()
print(random)

a = []
for i in range(3):
    a.append(float("{:.2f}".format(uniform(0.5,0.8))))

print(a)
print(shuffle(a))

randrange = randrange(1,7,2)
print(randrange)

print(choice(a))

from datetime import datetime, timezone, timedelta

now = datetime.now()

print(now)

fmt = "%Y{} %m{} %d{} %H{} %M{} %S{}"