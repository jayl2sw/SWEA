fruit = ['   apple    ','banana','  melon']

fruit_dict = {fruit[i].strip():len(fruit[i].strip()) for i in range(len(fruit))}
print(fruit_dict)