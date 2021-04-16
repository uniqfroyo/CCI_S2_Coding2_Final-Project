from skimage.segmentation import slic,mark_boundaries
from skimage import io
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv

import time

class Texture(object):
    def __init__(self,np_matarr,idx=0,flag=1,center_ptxy=(0,0),segments=None):
        self.np_matarr=np_matarr
        self.id=idx
        self.flag=flag
        self.center_ptxy=center_ptxy
        self.colordic={'red':(255,0,0),'blue':(0,255,0),'green':(0,0,255),'default':(np_matarr[0,0,:][0],np_matarr[0,0,:][1],np_matarr[0,0,:][2])}
        self.segments=segments

    def get_reflect(self,srcimg,is_show=False,reflect_color='red'):
        ptcr=np.where(self.segments==self.id)
        color=None
        if isinstance(reflect_color,tuple): #Multitype input color
            color=reflect_color
        else:
            color=self.colordic[reflect_color]
        srcimg[ptcr[0],ptcr[1],:]=color
        if is_show:
            plt.imshow(srcimg)
            plt.show()
        return srcimg


def add_roi(backimg,logoimg,logox0,logoy0):
    backimg=backimg.copy()
    logoRs,logoCs,logoChels=logoimg.shape #Figure out the spatial parameters of the logo
    for y in range(logoy0,logoy0+logoRs):
            for x in range(logox0,logox0+logoCs):
                backimg[y,x,:]=logoimg[y-logoy0,x-logox0,:]
    return backimg

def roi_cutPoint(srcimg,x0,x1,y0,y1): #Cut the image
    return srcimg[y0:y1,x0:x1]

def hwSet(pixels_sum,limit=300):
    w,h,fr,bc=4,3,0,0
    for i in range(1,limit):
        w,h=4*i,3*i
        fr=bc
        bc=12*(i**2)
        #print('i={},{},{}'.format(i,fr,bc))
        if (pixels_sum<=bc)and(pixels_sum>=fr):
            break
    return h,w


def make_TextureRGB(mat_id_3,is_show=False):
    lens,_=mat_id_3.shape
    h,w=hwSet(lens)
    s=h*w
    re_texture=np.zeros([h,w,3],dtype=np.uint8)
    deta=(h*w)-lens
    deta_idxs=np.random.randint(0,(lens-1),[deta])
    idxn,idx=0,0
    for r in range(h):
        for c in range(w):
            if idx<lens:
                re_texture[r,c,:]=mat_id_3[idx]
                idx+=1
            else:
                re_texture[r,c,:]=mat_id_3[deta_idxs[idxn]]
                idxn+=1
    if is_show:
        plt.imshow(re_texture)
        plt.show()
    return re_texture


def superPixels(img,is_show=False):
    segments = slic(img, n_segments=4000, compactness=3,enforce_connectivity=True,convert2lab=True) #compactness
    #450,10 sumpixels=44540
    if is_show:
        out=mark_boundaries(img,segments)*255 # make boundaries to show
        out=add_roi(img,out,0,0)
        plt.imshow(out)
        plt.show()
    return segments,segments.max()


img = io.imread("venv/bin/sheep.JPG") # import image

#img=roi_cutPoint(img1,299, 469, 105, 367) # Trim the ROI X0x1Y0Y1 area
segments,blocks=superPixels(img,is_show=False)
Texture_list=[]
for idx in range(1,blocks+1):
    ptcr=np.where(segments==idx)
    arr=img[ptcr[0],ptcr[1],:]
    texture_mat=make_TextureRGB(arr,is_show=False)
    Texture_list.append(Texture(np_matarr=texture_mat,idx=idx,segments=segments))

imgv=img
for i in range(len(Texture_list)):
    imgv=Texture_list[i].get_reflect(imgv,is_show=False,reflect_color='default')

plt.imshow(imgv)
plt.axis('off')
plt.show()