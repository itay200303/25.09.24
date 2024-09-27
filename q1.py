
# start

list_temp: list[float] = []
while True:
    temp: float = float(input("Enter a temperate :"))
    if temp == -999:
        break
    if not -50.0 < temp < 50.0:
        continue
    list_temp.append(temp)
print(list_temp)

list_temp2: list[float] = [-20.0, 39.1, 18.5]
list_temp.extend(list_temp2)

print(f"max temp :", {max(list_temp)})
print(f"min temp :", {min(list_temp)})

if 18.5 in list_temp:
    print(True)
else:
    print(False)

print("list_temp.count(20) :" , list_temp.count(20))

avg_temp = sum(list_temp) / len(list_temp)
print(f"The average of the temperatures are :",  {avg_temp})

for temp in list_temp:
    print(temp)

print("list_temp.index(39.1) :" , list_temp.index(39.1))

print(list_temp)
del list_temp[0]
print("After deleting index[0] in list_temp :" , list_temp)

print(list_temp)
for i in range(len(list_temp) - 1, -1, -1):
    if i % 2 == 0:
        del list_temp[i]
print("After deleting index[zugi] in list_temp :" , list_temp)

if 18.5 in temp:
    list_temp.remove(18.5)
else:
    print("18.5 isn't in list")


temp_last = list_temp.pop()
print(f"After poping :" ,  {temp_last})

new_list_temp = list_temp.copy()
new_list_temp.sort()
print(f"The new list :" ,  {new_list_temp})

reverse_sorted_temperatures = list_temp.copy()
reverse_sorted_temperatures.sort()
print(f"the opposite sorted list :" , {reverse_sorted_temperatures})

# end
