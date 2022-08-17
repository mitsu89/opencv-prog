# coding: utf-8
# sample02.py

import cv2

try:
    img = cv2.imread(
        '/Volumes/Devdata/develop/pydev/opencv_prog/sample02.png',
        cv2.IMREAD_COLOR)
    if img is None:
        raise FileNotFoundError('ファイルが見つかりません。')

    img = cv2.circle(img, (250, 250), 100, (0, 255, 0), 3)

    cv2.imshow('sample02', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except FileNotFoundError as e:
    print(e)
