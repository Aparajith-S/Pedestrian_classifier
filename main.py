import numpy as np
import glob2 as glob
import cv2
import matplotlib.pyplot as plt 

def roi(img,r,c):
 vis = np.zeros((36,18), np.uint8) 
 for i in range(r,r+36):
     for j in range(c,c+18):
         vis[i-r][j-c]=img[i][j]
 return vis

def getped():
    filename="B:\\Projectpython\\TrainingData\\Pedestrians\\18x36\\*.pgm"
    imgdata=[]
    for img in glob.glob(filename):
        imgdata.append(cv2.imread(img,0))      
    print(str(len(glob.glob(filename)))+' total elements'+str(len(imgdata)))
    return imgdata

def getnped():
    filename="B:\\Projectpython\\TrainingData\\NonPedestrians\\*.pgm"
    imgdata=[]
    for img in glob.glob(filename):
        imgdata.append(cv2.imread(img,0))      
    print(str(len(glob.glob(filename)))+' total elements'+str(len(imgdata)))
    return imgdata

def main():
    #ped=getped() 
    nped_diff_sizes=getnped()
    nped=[]
    #the following gets the ROI of 36x18 for all non ped images for any size
    for i in nped_diff_sizes:
      for rows in range(0,int(len(i)/36)):
              for cols in range(0,int(len(i[0])/18)):
                  nped.append(roi(i,rows*36,cols*18))
    print(str(len(nped)))    

main()