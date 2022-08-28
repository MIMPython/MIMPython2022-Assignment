import cv2

img_input = cv2.imread('SD_mooncake.png')
img = img_input[0:498, 1:501]

an = img[0:248,0:250]
banh = img[0:248,250:500]
kieng = img[249:498,0:250]
trung_thu = img[248:498,250:500]


def hconcat_resize_min(im_list, interpolation=cv2.INTER_CUBIC):
    h_min = min(im.shape[0] for im in im_list)
    im_list_resize = [cv2.resize(im, (int(im.shape[1] * h_min / im.shape[0]), h_min), interpolation=interpolation)
                      for im in im_list]
    return cv2.hconcat(im_list_resize)

def vconcat_resize_min(im_list, interpolation=cv2.INTER_CUBIC):
    w_min = min(im.shape[1] for im in im_list)
    im_list_resize = [cv2.resize(im, (w_min, int(im.shape[0] * w_min / im.shape[1])), interpolation=interpolation)
                      for im in im_list]
    return cv2.vconcat(im_list_resize)

banh_trung_thu = hconcat_resize_min([banh, trung_thu])
an_kieng = hconcat_resize_min([an, kieng])

banh_trung_thu_an_kieng = vconcat_resize_min([banh_trung_thu, an_kieng])
cv2.imshow('image', banh_trung_thu_an_kieng)
cv2.waitKey(0)