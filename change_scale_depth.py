import cv2
import numpy as np

def im_chscaledepth (img, depth, scale):
    scale = float(scale)
    if depth < 1 or depth > 8:
        return -1, None
    if scale <= 0:
        return -2, None
    # teste de escala de cinza ou cor

    depth_factor = 2 ** (8 - depth)
    img_temp_1 = np.floor(img / depth_factor).astype(int)
    img_temp_1 = np.floor((img_temp_1 * depth_factor * 255) / (depth_factor * (2 ** depth - 1))).astype(int)

    h = img.shape[0]
    w = img.shape[1]

    if scale < 1:
        keep = []
        for i in range(w):
            if (len(keep) + 1) / (i + 1) <= scale:
                keep.append(i)

        img_temp_2 = img_temp_1[:, keep]

        keep.clear()
        for i in range(h):
            if (len(keep) + 1) / (i + 1) <= scale:
                keep.append(i)

        img_temp = img_temp_2[keep, :]
    elif scale > 1:
        scale_up = int(np.ceil(scale))

        img_temp_2 = np.empty((h, scale_up * w, 3), dtype = img.dtype)
        for i in range(scale_up):
            img_temp_2[:, i::scale_up] = img_temp_1

        img_temp_3 = np.empty((scale_up * h, scale_up * w, 3), dtype = img.dtype)
        for i in range(scale_up):
            img_temp_3[i::scale_up, :] = img_temp_2

        scale_down = scale / scale_up

        if scale.is_integer():
            img_temp = img_temp_3
        else:
            keep = []
            for i in range(scale_up * w):
                if (len(keep) + 1) / (i + 1) <= scale_down:
                    keep.append(i)

            img_temp_4 = img_temp_3[:, keep]
            
            keep.clear()
            for i in range(scale_up * h):
                if (len(keep) + 1) / (i + 1) <= scale_down:
                    keep.append(i)

            img_temp = img_temp_4[keep, :]
    else:
        img_temp = img_temp_1

    
    return 1, img_temp

def main():
    img = cv2.imread("im1.jpg", cv2.IMREAD_ANYCOLOR)
    ret, new_img = im_chscaledepth(img, 2, 2.4)
    cv2.imwrite("nova.jpg", new_img)

if __name__  == "__main__":
    main()