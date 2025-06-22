from itertools import permutations

my_list = [2, 5, 9, 6, 1, 7]

perms = permutations(my_list)


for i, p in enumerate(perms, start=1):
    list_p = list(p)

    if list_p == sorted(my_list):
        print(f"{i}. Permutation is sorted.")
        break
