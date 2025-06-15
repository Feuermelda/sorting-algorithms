my_list = [3, 1, 4, 2]


for i in range(1, len(my_list)):
    key_value = my_list[i]
    j = i - 1
    while (j >= 0) and (my_list[j] > key_value):
        my_list[j + 1] = my_list[j]
        j -= 1
    my_list[j + 1] = key_value

print(my_list)
