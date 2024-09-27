import statistics

# start
numbers_count = {}
numbers_list = []

while True:
    user_input : int = int(input("Give a number between 0 - 10: "))
    num = int(user_input)
    if num < 0 or num > 10:
        continue
    if num == -999:
        break
    numbers_list.append(num)
    if num in numbers_count:
        numbers_count[num] += 1
    else:
        numbers_count[num] = 1
    statistics = [f"[ {num} ]: {count}" for num, count in numbers_count.items() if count > 0]
    print(f"Statistics :", " ".join(statistics))
print()

