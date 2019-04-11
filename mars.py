import cv2
import numpy as np
from matplotlib import pyplot as plt 


def im_rgb2gray(img):
    new_img = img.mean(axis = 2).astype(np.uint8)
    print(new_img.shape)
    print(np.amin(new_img))

    return new_img

def main():
    img = cv2.imread("Mars.bmp", cv2.IMREAD_ANYCOLOR)
    print(type(img))
    new_img = im_rgb2gray(img)
    print(new_img.dtype)
    #new_img3 = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
    new_img2 = cv2.equalizeHist(new_img)
    cv2.imwrite("nova.jpg", new_img)
    cv2.imwrite("nova2.jpg", new_img2)

    plt.figure(200)
    plt.hist(new_img.ravel(), bins=256)
    plt.title("histogram") 

    plt.figure(300)
    plt.hist(new_img2.ravel(), bins=256)
    plt.title("histogram2") 
    plt.show()

if __name__  == "__main__":
    main()