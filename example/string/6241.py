data = input()

idx = data.find(':')
idx2 = data.find('/', 10)

protocol = data[:idx]
host = data[idx+3:idx2]
others = data[idx2+1:]

print("protocol: {}".format(protocol))
print("host: {}".format(host))
print("others: {}".format(others))

