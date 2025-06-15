my_list = [34, 21, 2, 15, 7, 39, 28]


swapped = True

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):

        if my_list[i] > my_list[i+1]:
            f = my_list[i]
            my_list[i] = my_list[i+1]
            my_list[i+1] = f
            swapped = True


print(my_list)
