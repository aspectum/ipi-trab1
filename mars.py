import cv2
import numpy as np
from matplotlib import pyplot as plt 

destination = (260, 415)
position = (815, 1000)

def find_next_pos(neighbors, img):
    darkest = 255
    for neighbor in neighbors[0:2]:
        row = position[0] + neighbor[0]
        col = position[1] + neighbor[1]
        if img[row, col] < darkest:
            darkest = img[row, col]
            next_pos = (row, col)
    return next_pos

def three_closest():
    neighbors = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            dist = (destination[0] - position[0] - i) ** 2 + (destination[1] - position[1] - j) ** 2
            neighbors.append((i, j, dist))
    
    return sorted(neighbors, key = lambda x: x[2])

def im_rgb2gray(img):
    img_gray = img.mean(axis = 2).astype(np.uint8)

    return img_gray

def main():
    global position
    img = cv2.imread("Mars.bmp", cv2.IMREAD_ANYCOLOR)
    img_gray = im_rgb2gray(img)

    img_equ = cv2.equalizeHist(img_gray)
    cv2.imwrite("nova.jpg", img_gray)
    cv2.imwrite("nova2.jpg", img_equ)

    img_path = np.tile(img_equ[:, :, None], (1, 1, 3))

    img_path[position] = (0, 0, 255)

    while position != destination:
        neighbors = three_closest()
        position = find_next_pos(neighbors, img_equ)
        img_path[position] = (0, 0, 255)
        cv2.imshow('mars', img_path)
        if cv2.waitKey(5) & 0xFF == ord('q'): 
            break
    cv2.imwrite("path.jpg", img_path)

    # plt.figure(200)
    # plt.hist(new_img.ravel(), bins=256)
    # plt.title("histogram") 

    # plt.figure(300)
    # plt.hist(new_img2.ravel(), bins=256)
    # plt.title("histogram2") 
    # plt.show()



if __name__  == "__main__":
    main()