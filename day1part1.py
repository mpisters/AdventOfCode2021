list = open("day1inputpart1.txt").read().split()
list_number = [int(x) for x in list]
list_higher = []
for i in range(len(list_number)):
    if i + 1 >= len(list_number):
        break
    next_item = list_number[i+1]
    current_item = list_number[i]
    is_increased = next_item > current_item
    list_higher.append(is_increased)

true_list = [x for x in list_higher if x == True]
print(len(true_list))

