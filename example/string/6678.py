while True:
    words = input()
    if words == '':
        break
    print(">> {}".format(words.upper()))

data = []
while True:
    new = input()
    if new == "":
        break
    else:
        data.append(new)

for i in data:
    print(">> {}".format(i.upper()))

