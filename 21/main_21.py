import cv2
from copy import copy
import numpy as np


def task_test():
    ver = 3
    name = './21/{}/'.format(ver)
    name_in = name + 'in{}.png'.format(ver)
    name_set = name + 'set{}.txt'.format(ver)
    name_wb = name + 'wb{}.png'.format(ver)
    name_out = name + 'out{}.png'.format(ver)
    file_in = open(name_set, 'r')
    k = float(file_in.readline().rstrip())
    x1, x2 = map(int, file_in.readline().split())
    y1, y2 = map(int, file_in.readline().split())
    hcv_vals = list(map(int, file_in.readline().split()))
    img_in = cv2.imread(name_in)
    y, x = img_in.shape[0], img_in.shape[1]
    x2 = x2 if x2 > 0 else x
    y2 = y2 if y2 > 0 else y

    imgray = cv2.cvtColor(img_in, cv2.COLOR_BGR2GRAY)
    _, edges = cv2.threshold(imgray, 127, 255, 0) # cv2.Canny(imgray, 127, 128)
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(img_in, contours, -1, (127, 127, 0), 2)

    # cv2.namedWindow('cv2')
    track = 'track '
    track1, track2 = 'track1_', 'track2_'
    cv2.namedWindow(track1)
    cv2.namedWindow(track2)
    
    def callback():
        # _, edges = cv2.threshold(imgray, l, m, 0) # cv2.Canny(imgray, 127, 128)
        
        # img1 = cv2.resize(img_in, (int(x/k), int(y/k)), cv2.INTER_NEAREST)
        # img = copy(img1)[y1:y2, x1:x2]
        
        k = float(cv2.getTrackbarPos(track+'k', track2)) / 10
        x1, x2, y1, y2 = [int(cv2.getTrackbarPos(track+i, track2)) for i in ['x1', 'x2', 'y1', 'y2']]
        img = copy(cv2.resize(img_in[y1:y2, x1:x2], (int((x2-x1+1)/k), int((y2-y1+1)/k)), cv2.INTER_NEAREST))
        
        # contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # cv2.drawContours(img, contours, -1, (127, 127, 0), 2)
        lower = np.array([cv2.getTrackbarPos(track + str(i), track1) for i in [0, 1, 2]])
        upper = np.array([cv2.getTrackbarPos(track + str(i), track1) for i in [3, 4, 5]])
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower, upper)
        res = cv2.bitwise_and(img, img, mask=mask)
        show_cv1_win(img)
        show_cv2_win(mask)
        show_cv3_win(res)
        cv2.imwrite(name_wb, mask)
        cv2.imwrite(name_out, res)

    def show_cv1_win(img0):
        cv2.imshow('cv1', img0)
    def show_cv2_win(edges2):
        cv2.imshow('cv2', edges2)
    def show_cv3_win(_img):
        cv2.imshow('cv3', _img)

    n = 6
    [cv2.createTrackbar(track+str(i), track1, 0, 255, lambda a:None) for i in range(n)]
    cv2.createTrackbar(track+'k', track2, 1, 60, lambda a:None)
    cv2.createTrackbar(track+'x1', track2, 0, x, lambda a:None)
    cv2.createTrackbar(track+'x2', track2, 0, x, lambda a:None)
    cv2.createTrackbar(track+'y1', track2, 0, y, lambda a:None)
    cv2.createTrackbar(track+'y2', track2, 0, y, lambda a:None)
    [cv2.setTrackbarPos(track+str(i), track1, hcv_vals[i]) for i in range(n)]
    cv2.setTrackbarPos(track+'k', track2, int(k*10))
    cv2.setTrackbarPos(track+'x1', track2, x1)
    cv2.setTrackbarPos(track+'x2', track2, x2)
    cv2.setTrackbarPos(track+'y1', track2, y1)
    cv2.setTrackbarPos(track+'y2', track2, y2)
    
    show_cv2_win(edges)
    #cv2.imwrite('for{}.png'.format(ver), img)
    
    while True:
        callback()
        if cv2.waitKey(1) == 27:
            file_out = open(name_set, 'w')
            k = float(cv2.getTrackbarPos(track+'k', track2)) / 10
            x1, x2, y1, y2 = [int(cv2.getTrackbarPos(track+i, track2)) for i in ['x1', 'x2', 'y1', 'y2']]
            hcv_vals = [int(cv2.getTrackbarPos(track+str(i), track1)) for i in range(n)]
            print(k, '\n', x1, ' ', x2, '\n', y1, ' ', y2, '\n', ' '.join([str(i) for i in hcv_vals]), sep='', file=file_out)
            break


task_test()
cv2.destroyAllWindows()
