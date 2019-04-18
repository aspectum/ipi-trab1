import cv2
import numpy as np
from matplotlib import pyplot as plt

destination = (815, 1000)   # Destination pixel
position = (260, 415)       # Starting pixel


# Between the 3 neighbors closest to destination,
# returns the one with the least brightness
def find_next_pos(neighbors, img):
    darkest = 255
    for neighbor in neighbors[0:2]:
        row = position[0] + neighbor[0]
        col = position[1] + neighbor[1]
        if img[row, col] < darkest:
            darkest = img[row, col]
            next_pos = (row, col)
    return next_pos


# Sorts the adjacent pixels by least distance to destination
def closest_neighbors():
    neighbors = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            dist = (destination[0] - position[0] - i) ** 2 + (destination[1] - position[1] - j) ** 2
            neighbors.append((i, j, dist))

    return sorted(neighbors, key = lambda x: x[2])


# Transforms colored image into grayscale
def im_color2gray(img):
    img_gray = img.mean(axis = 2).astype(np.uint8)

    return img_gray


def main():
    global position
    img = cv2.imread("Mars.bmp", cv2.IMREAD_ANYCOLOR)
    img_gray = im_color2gray(img)

    img_equ = cv2.equalizeHist(img_gray)
    cv2.imwrite("nova.jpg", img_gray)
    cv2.imwrite("nova2.jpg", img_equ)

    # Creating a 3 color image from a grayscale
    img_path = np.tile(img_equ[:, :, None], (1, 1, 3))

    img_path[position] = (0, 0, 255)

    cv2.imshow('mars', img)
    cv2.waitKey(2000)

    cv2.imshow('mars', img_gray)
    cv2.waitKey(2000)

    cv2.imshow('mars', img_equ)
    cv2.waitKey(2000)

    while position != destination:
        neighbors = closest_neighbors()
        position = find_next_pos(neighbors, img_equ)
        img_path[position] = (0, 0, 255)
        cv2.imshow('mars', img_path)
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

    cv2.imwrite("path.jpg", img_path)

    cv2.waitKey()


if __name__  == "__main__":
    main()