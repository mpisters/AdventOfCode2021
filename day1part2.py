list = open("day1inputpart1.txt").read().split()
list_number = [int(x) for x in list]
list_higher = []
for i in range(len(list_number)):
    if i + 3 >= len(list_number):
        break
    item1 = list_number[i]
    item2 = list_number[i+1]
    item3 = list_number[i+2]
    nextitem1 = list_number[i+1]
    nextitem2 = list_number[i+2]
    nextitem3 = list_number[i+3]

    is_increased = (item1 + item2 + item3) < (nextitem1 + nextitem2 + nextitem3)
    list_higher.append(is_increased)

true_list = [x for x in list_higher if x == True]
print(len(true_list))

