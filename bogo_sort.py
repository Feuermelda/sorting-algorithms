import random
from time import time

my_list = [3, 1, 4, 2, 6, 7, 5, 0]

unsorted = True

attempt_counter = 0


start = time()

while unsorted:
    random.shuffle(my_list)
    smallest = my_list[0]
    biggest = my_list[-1]
    for index, element in enumerate(my_list):

        if smallest <= element <= biggest:
            smallest = element
            if element == biggest:
                unsorted = False

        else:
            attempt_counter += 1
            break


end = time()
difference = end - start

print(my_list, attempt_counter, difference)
