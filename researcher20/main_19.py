# from time import sleep
import numpy as np
import cv2
from random import randint


def task3_2():
    res, ints = [0 for _ in range(8)], [int(i) for i in input().split()]
    buf = int(ints[1] >= 0) + 2*int(ints[1] >= 0)
    for i in ints[2:]:
        if i >= 0:
            buf += 4
        res[buf] += 1
        buf = buf >> 1
    for i, val in enumerate(res):
        o = '0'*(3-len(str(bin(i))[2:])) + str(bin(i))[2:]
        print(o.replace('0', '-').replace('1', '+')[::-1], val)
    # 6 67 -54 4 0 3 -7


def task_live():
    # setup
    infile = open('in.txt', 'r')
    x_len, y_len = [int(i)-1 for i in infile.readline().split()]
    char1, char2 = infile.readline().split()                                             # '#', '_'
    str_in = [[[char1, char2][randint(0, 1)] for _ in range(x_len)] for _ in range(y_len)]  # [i[:-1].split() for i in infile.readlines()]
    infile.close()
    window_name = 'A live'
    cv2.namedWindow(window_name)

    # setup 2
    def show_gen(gen_i):
        def color_cell(j):
            return j                                                                # int(j == char2)*127 + int(j == char1)*128
        int_in = [[color_cell(j) for j in i] for i in str_in]
        np_arr = np.array(int_in, dtype=np.float32)
        array_show = cv2.resize(np_arr, (850, 850), interpolation=cv2.INTER_AREA)
        cv2.imshow(window_name, array_show)
        cv2.imwrite('img'+str(gen_i), array_show)

    def gen(old_bool):
        def cell(lived):
            sum_cell = 0
            neighbours = [-1, 0, 1]
            for x in neighbours:
                for y in neighbours:
                    if not x == 0 == y:
                        sum_cell += old_bool[(a + y) % y_len][(b + x) % x_len] == char1
            return char1 if sum_cell == 3 or sum_cell == 2 and lived == char1 else char2
        new_bool = [[char2]*(x_len+1) for _ in range(y_len+1)]
        for a in range(y_len):
            for b in range(x_len):
                new_bool[a][b] = cell(old_bool[a][b])
        return new_bool
    gen_i = 0
    while True:
        show_gen(gen_i)
        if cv2.waitKey(1) == 27:
            cv2.destroyAllWindows()
            break
        str_in = gen(str_in)
        gen_i += 1
        # sleep(0.01)


def task6():
    file_in = open('in6.txt', 'r')
    # in_val = [_.split() for _ in file_in.readlines()]
    file_in.close()


task_live()
