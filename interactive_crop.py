import cv2
import numpy as np

def draw_rectangle(event, x, y, flags, params):
    global x_init, y_init, drawing, top_left_pt, bottom_right_pt

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        x_init, y_init = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            top_left_pt = (min(x_init, x), min(y_init, y))
            bottom_right_pt = (max(x_init, x), max(y_init, y))
            img[y_init:y, x_init:x] = 255 - img[y_init:y, x_init:x]

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        top_left_pt = (min(x_init, x), min(y_init, y))
        bottom_right_pt = (max(x_init, x), max(y_init, y))
        img[y_init:y, x_init:x] = 255 - img[y_init:y, x_init:x]

if __name__=='__main__':
    drawing = False
    top_left_pt, bottom_right_pt = (-1,-1), (-1,-1)

    cv2.namedWindow('pic')
    cv2.setMouseCallback('pic', draw_rectangle)

    while True:

        img = cv2.imread('test.png')
        img = cv2.resize(img, None, fx=0.3, fy=0.3, interpolation=cv2.INTER_AREA)
        img_org = img.copy()
        cv2.imshow('pic',img)

        (x0,y0), (x1,y1) = top_left_pt, bottom_right_pt
        trim_img = img_org[y0:y1, x0:x1] 
        img[y0:y1, x0:x1] = 255 - img[y0:y1, x0:x1]
        cv2.imshow('pic', img)  

        if cv2.waitKey(1) == ord('q'):
            cv2.imwrite('trim_test.jpg', trim_img)
            break

    cv2.destroyAllWindows()
