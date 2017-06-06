

given = [1,2,3,4,5,4,32,1,6,7,4,2,567,5]

new = []

while True:
    if len(given) == 0:
        break

    else:
        item = given.pop()
        if item not in new:
            new.append(item)


print(new)
