def generate_list(a, b):
    list1 = []
    for i in range(a, b+1):
        list1.append(i**2)
    return list1


var1 = generate_list(1, 20)
print(var1[5:])
