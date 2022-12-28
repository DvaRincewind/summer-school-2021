# from time import sleep
import numpy as np
import cv2
from random import randint
from time import time
import imageio


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
    print('Start!!!')
    # setup
    infile = open('in_19.txt', 'r')
    x_len, y_len = [int(i)-1 for i in infile.readline().split()]
    char1, char2 = infile.readline().split()                                             # '#', '_'
    str_in = [[[1, 0][randint(0, 1)] for _ in range(x_len)] for _ in range(y_len)]  
    # str_in = [i[:-1].split() for i in infile.readlines()]
    infile.close()
    window_name = 'A live'
    t = time()
    cv2.namedWindow(window_name)
    writer = imageio.get_writer('live_out_img.gif', mode = 'I')
    # setup 2
    def show_gen(gen_i):
        def color_cell(j):
            return  int(j)*255 #int(j == char2)*0 + int(j == char1)*255
        int_in = [[color_cell(j) for j in i] for i in str_in]
        np_arr = np.array(int_in, dtype=np.float32)
        cv2.imwrite('liveimg/img'+str('0'*(3-len(str(gen_i)))+str(gen_i))+'.png', np_arr)
        image = imageio.imread('liveimg/img'+str('0'*(3-len(str(gen_i)))+str(gen_i))+'.png')
        writer.append_data(image)
        
        # array_show = cv2.resize(np_arr, (790, 790), interpolation=cv2.INTER_AREA)
        # cv2.imshow(window_name, array_show)
        # array_show = cv2.cvtColor(array_show, cv2.COLOR_)

    def gen(old_bool):
        def cell(lived):
            sum_cell = 0
            neighbours = [-1, 0, 1]
            for x in neighbours:
                for y in neighbours:
                    if not x == 0 == y:
                        sum_cell += old_bool[(a + y) % y_len][(b + x) % x_len]
            return 1 if sum_cell == 3 or sum_cell == 2 and lived else 0
        new_bool = [[0]*(x_len+1) for _ in range(y_len+1)]
        for a in range(y_len):
            for b in range(x_len):
                new_bool[a][b] = cell(old_bool[a][b])
        return new_bool
    gen_i = 0
    while True:
        show_gen(gen_i)
        print(gen_i, time() - t)
        t = time()
        if cv2.waitKey(1) == 27:
            print('End!!!')
            writer.close()
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
