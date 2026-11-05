my_list = [10, "Python", 20, 10, "Java", True, "Python", 20, 30]

result = []

for item in my_list:
    if item not in result:
        result.append(item)

print(result)