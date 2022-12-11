with open("11.txt") as f:
    lines = f.read().strip().split("\n")

i = 0
monkey_infos = []
while i != len(lines) + 1:
    monkey_infos.append(lines[i:i+6])
    i += 7

worry_level = []
inspected_time = [0 for i in range(len(monkey_infos))]
for i in range(len(monkey_infos)):
    worry_level.append([])
    info = monkey_infos[i]
    starting_item = info[1][17:].strip().split(", ")
    for item in starting_item:
        worry_level[i].append(int(item))

# foreach monkey(index: i)
operator = []
operation_number = []
test_number = []
if_true_to_list = []
if_false_to_list = []
for i in range(len(monkey_infos)):
    info = monkey_infos[i]
    operations = info[2]
    test = info[3]
    test_true = info[4]
    test_false = info[5]

    tmp_op = operations.split("=")[1].strip().split(" ")
    tmp_test = test.strip().split(" ")
    tmp_true = test_true.strip().split(" ")
    tmp_false = test_false.strip().split(" ")
    if_true_to = int(tmp_true[5])
    if_false_to = int(tmp_false[5])

    operator.append(tmp_op[1])
    operation_number.append(tmp_op[2])
    test_number.append(tmp_test[3])
    if_true_to_list.append(if_true_to)
    if_false_to_list.append(if_false_to)

mod_number = 1
for i in test_number:
    mod_number *= int(i)

for k in range(10000):
    for i in range(len(monkey_infos)):
        # foreach processes
        for j in range(len(worry_level[i])):
            inspected_time[i] += 1
            item = worry_level[i][j]
            if item == -1: continue
            if operator[i] == "*":
                if operation_number[i] == "old":
                    item *= item
                else:
                    item *= int(operation_number[i])
            if operator[i] == "+":
                if operation_number[i] == "old":
                    item += item
                else:
                    item += int(operation_number[i])
            item %= mod_number

            # print(item, worry_level[i])
            if item % int(test_number[i]) == 0:
                worry_level[if_true_to_list[i]].append(item)
            else: 
                worry_level[if_false_to_list[i]].append(item)
        worry_level[i] = []
print(inspected_time)
inspected_time.sort()
print(inspected_time[-1] * inspected_time[-2])


            