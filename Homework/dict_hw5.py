nameAge = {"Allison": 18, "Benson": 48, "David": 20, "Erik": 20, "Galen": 15, "Grace": 18, "Bob": 48, "Janette": 18}

ageName = {}

for name, age in nameAge.items():
    if age not in ageName:
        ageName[age] = [name]
    else:
        ageName[age].append(name)
print(ageName)
print(sorted(ageName.keys()))

for age in sorted(ageName.keys()):
    print("People at age " + str(age) + " " + ", ".join(ageName[age]))
