nameList = ["Bruce Lee",
"Nathan Chen",
"Coby Bryan",
"Shawn White",
"Tyrion Bryan",
"Allison Chen",
"Stan Lee",
"Catelyn Chen",
"Joy Chen",
"Jonathan Lee",
"Bob White",
"Ned Chen"]

nameCountMap = {}

for name in nameList:
    names = name.split(' ')
    lastname = names[1]
    if lastname in nameCountMap:
        nameCountMap[lastname] += 1
    else:
        nameCountMap[lastname] = 1

print(nameCountMap)
maxCount = 0
maxLastName = ''
for lastname, count in nameCountMap.items():
    if maxCount < count:
        maxCount = count
        maxLastName = lastname
print("Family " + maxLastName + " is the biggest family")

