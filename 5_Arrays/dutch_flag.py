from random import randint
from collections import namedtuple

def dutch_flag_partition(A, i):
    pivot = A[i]
    front_p = 0
    num_equal = 0
    back_p = len(A) - 1
    roll = True
    while front_p <= back_p - num_equal:
        print(A, front_p, back_p, num_equal)
        if roll:
            A[front_p], A[front_p + num_equal] = A[front_p + num_equal], A[front_p]
        roll = True
        if A[front_p] < pivot:
            front_p += 1
        elif A[front_p] == pivot:
            num_equal += 1
        else:
            A[front_p], A[back_p] = A[back_p], A[front_p]
            back_p -=1
            roll = False
    return A


def dutch_flag_partition_2(A, i):
    pivot = A[i]
    class_p = 0
    larger_p = len(A) - 1
    num_equal = 0

    while class_p <= larger_p:
        if A[class_p] < pivot:
            A[class_p], A[class_p - num_equal] = A[class_p - num_equal], A[class_p]
            class_p += 1
        elif A[class_p] == pivot:
            class_p += 1
            num_equal += 1
        else:
            A[class_p], A[larger_p] = A[larger_p], A[class_p]
            larger_p -= 1
    return A

def three_key_part(A):
    keys = []
    class_p = 0
    larger_p = len(A) - 1
    num_keys_1 = 0
    while class_p <= larger_p:
        if A[class_p] not in keys:
            keys.append(A[class_p])
        if A[class_p] == keys[0]:
            A[class_p], A[class_p - num_keys_1] = A[class_p - num_keys_1], A[class_p]
            class_p += 1
        elif A[class_p] == keys[1]:
            num_keys_1 += 1
            class_p += 1
        else:
            A[class_p], A[larger_p] = A[larger_p], A[class_p]
            larger_p -= 1
    return A

def four_key_part(A):
    keys = []
    class_p, num_keys_1, num_keys_2, larger_p = 0,0,0, len(A) - 1

    while class_p <= larger_p:
        if A[class_p] not in keys:
            keys.append(A[class_p])
        if A[class_p] == keys[0]:
            temp = A[class_p]
            A[class_p] = A[class_p - num_keys_2]
            A[class_p - num_keys_2] = A[class_p - num_keys_2 - num_keys_1]
            A[class_p - num_keys_2 - num_keys_1] = temp
            class_p += 1
        elif A[class_p] == keys[1]:
            A[class_p], A[class_p - num_keys_2] = A[class_p - num_keys_2], A[class_p]
            num_keys_1 += 1
            class_p += 1
        elif A[class_p] == keys[2]:
            num_keys_2 += 1
            class_p += 1
        else:
            A[class_p], A[larger_p] = A[larger_p], A[class_p]
            larger_p -= 1
    return A

def order(A):
    #splits array into false and true, but maintains relative
    #ordering of true items
    next_true, last_true = len(A) - 1, len(A) - 1
    while next_true >= 0:
        while next_true >= 0 and not A[next_true].k:
            next_true -= 1
        if next_true >= 0:
            A[last_true], A[next_true] = A[next_true], A[last_true]
            last_true -= 1
            next_true -= 1
    return A


#print(dutch_flag_partition_2([0], 0))
#print(three_key_part([6,8,7,8,7,6,8,7,6,6,6,6,7,7,8,6,7,8,7,8,7]))
#print(four_key_part([4,1,3,2,1,3,2,4,1,2,3,4,2,3,4,4,4,4,2,3,3,1,2,2,2,1]))
elements = []
kvpair = namedtuple("kvpair", "k v")
for i in range(10):
    elements.append(kvpair(randint(0,1) == 1, i))
order(elements)
[print("({0}, {1})".format(x.k,x.v)) for x in elements]
