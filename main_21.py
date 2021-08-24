from cv2 import cv2 as cv2
from copy import copy
import numpy as np


def task_test():
    name_img = 'for1.png'
    img_in = cv2.imread(name_img)
    y, x = img_in.shape[0], img_in.shape[1]
    img1 = cv2.resize(img_in, (x//2, y//2), cv2.INTER_NEAREST)
    name_txt = 'in2.txt'
    file_in = open(name_txt, 'r')
    x1, x2 = map(int, file_in.readline().split())
    y1, y2 = map(int, file_in.readline().split())
    track_vals = list(map(int, file_in.readline().split()))
    img = copy(img1)[y1:y2, x1:x2]

    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, edges = cv2.threshold(imgray, 127, 255, 0) # cv2.Canny(imgray, 127, 128)
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img, contours, -1, (127, 127, 0), 2)

    def callback():
        # _, edges = cv2.threshold(imgray, l, m, 0) # cv2.Canny(imgray, 127, 128)
        img = copy(img1)[y1:y2, x1:x2]
        # contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # cv2.drawContours(img, contours, -1, (127, 127, 0), 2)
        lower = np.array([cv2.getTrackbarPos('track' + str(i), 'track') for i in [0, 1, 2]])
        upper = np.array([cv2.getTrackbarPos('track' + str(i), 'track') for i in [3, 4, 5]])
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower, upper)
        res = cv2.bitwise_and(img, img, mask=mask)
        show_cv2_win(mask)
        show_cv3_win(res)

    def show_cv2_win(edges2):
        cv2.imshow('cv2', edges2)
    def show_cv3_win(_img):
        cv2.imshow('cv3', _img)
    cv2.namedWindow('cv2')
    cv2.namedWindow('track')

    n = 6
    [cv2.createTrackbar('track'+str(i), 'track', 0, 255, lambda a:None) for i in range(n)]
    [cv2.setTrackbarPos('track'+str(i), 'track', track_vals[i]) for i in range(n)]
    show_cv2_win(edges)
    cv2.imwrite('for2.png', img)
    while True:
        callback()
        if cv2.waitKey(1) == 27:
            file_out = open(name_txt, 'w')
            print(x1, ' ', x2, '\n', y1, ' ', y2, '\n', ' '.join(list(track_vals)), sep='', file=file_out)
            break


task_test()
cv2.destroyAllWindows()
