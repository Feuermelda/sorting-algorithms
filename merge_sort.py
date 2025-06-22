my_list = [20, 5, 31, 9, 12]


def merge(left, right):
    new_list = left + right
    unsorted = True
    while unsorted:
        unsorted = False
        for i in range(len(new_list)-1):

            if new_list[i] > new_list[i+1]:
                new_list[i], new_list[i+1] = new_list[i+1], new_list[i]
                unsorted = True

    return new_list


def merge_sort(lst):
    if len(lst) <= 1:
        return lst  # base case
    else:

        upper_half = len(lst) // 2

        left = merge_sort(lst[:upper_half])

        right = merge_sort(lst[upper_half:])

        return merge(left, right)


sorted_list = merge_sort(my_list)
print(sorted_list)
