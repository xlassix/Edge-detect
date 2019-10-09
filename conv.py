import numpy as np
def conv(image,im_filter):
    #compute dimesions of image
    height,width=image.shape
    im_filter=np.asarray(im_filter)
    #output image size init with zero
    out_image=np.zeros((height-len(im_filter) +1,width-len(im_filter)+1))
    x=len(im_filter)
    #calcuating the out_image
    for row in range(len(out_image)):
        for col in range(len(out_image[0])):
            out_image[row,col]=np.sum(image[row:row+x,col:col+x]*im_filter)
    #fix cumulative that exceed 255
    out_image[out_image>255]=255
    out_image[out_image<0]=0
    return out_image
