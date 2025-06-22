my_list = [5, 3, 8, 1, 2]


for i in range(len(my_list)-1):

    current_small = my_list[i]
    index = i
    for j in range(i+1, len(my_list)):

        if (my_list[j] < current_small):
            current_small = my_list[j]
            index = j

    my_list[i], my_list[index] = my_list[index], my_list[i]


print(my_list)
