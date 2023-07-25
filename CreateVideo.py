import os
import cv2

path = "Images/"
Images=[]

path = "Images"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)

img=cv2.imread(images[0])
h,w,c=img.shape
size=(w,h)
video=cv2.VideoWriter("video.mp4",cv2.VideoWriter_fourcc(*'DIVX'),20,size)
for i in range (count-1,0,-1):
    frame=cv2.imread(images[i])
    video.write(frame)
video.release()
print("Done")