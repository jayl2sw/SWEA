array = list(range(1,11))

even_array = list(filter(lambda x: x%2==0, array))
even_pow_array = list(map(lambda x: pow(x,2), even_array))
print(even_pow_array)