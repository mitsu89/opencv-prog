# coding: utf-8
# sample04.py

import cv2


try:
    img = cv2.imread('./sample02.png', cv2.IMREAD_COLOR)
    if img is None:
        raise FileNotFoundError('ファイルが見つかりません。')

    img = cv2.circle(img, (250, 250), 100, (0, 255, 0), 3)
    cv2.imshow('sample04', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite('./sampleo3.png', img)

except FileNotFoundError as e:
    print(e)
