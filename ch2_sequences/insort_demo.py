import random
from bisect import insort

if __name__ == "__main__":

    SIZE = 7
    random.seed(1729)

    my_list = []
    for i in range(SIZE):
        new_item = random.randrange(SIZE * 2)
        insort(my_list, new_item)
        print('%2d ->' % new_item, my_list)