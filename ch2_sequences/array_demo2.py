from array import array
import random

if __name__ == "__main__":

    test_array = array('i', (random.randrange(10) for _ in range(10)))

    print("Initial array: ", test_array)

    array2 = array('i', (random.randrange(10) for _ in range(5)))
    print("New array after adding elements: ", test_array.__add__(array2))
    print("New array after adding elements with concatenation: ", test_array + array2)

    test_array.append(100)
    print("Append element: ", test_array)

    test_array.pop()
    print("Then removed: ", test_array)

    print("Containment check: Is 9 in the array ? ", test_array.__contains__(9))
    print("Same containment check: Is 9 in the array ? ", 9 in test_array)

    print("Counting elements: ", test_array.__len__())
    print("Same count: ", len(test_array))

    print("Counting element occurrence. How many 5s are in the array ? ", test_array.count(5))

    array2 = test_array.__copy__()
    array2.extend((random.randrange(10) for _ in range(5)))
    print("Append item from iterable: ", array2)
    array2.fromlist([1, 2, 3])
    print("Append item from list: ", array2)

    print("Position of first occurrence of 9: ", test_array.index(9))

    test_array.reverse()
    print("Array reversed: ", test_array)

    print("Array as list: ", test_array.tolist())

