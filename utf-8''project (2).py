#!/usr/bin/env python
# coding: utf-8

# # The Project #
# 1. This is a project with minimal scaffolding. Expect to use the the discussion forums to gain insights! It’s not cheating to ask others for opinions or perspectives!
# 2. Be inquisitive, try out new things.
# 3. Use the previous modules for insights into how to complete the functions! You'll have to combine Pillow, OpenCV, and Pytesseract
# 4. There are hints provided in Coursera, feel free to explore the hints if needed. Each hint provide progressively more details on how to solve the issue. This project is intended to be comprehensive and difficult if you do it without the hints.
#
# ### The Assignment ###
# Take a [ZIP file](https://en.wikipedia.org/wiki/Zip_(file_format)) of images and process them, using a [library built into python](https://docs.python.org/3/library/zipfile.html) that you need to learn how to use. A ZIP file takes several different files and compresses them, thus saving space, into one single file. The files in the ZIP file we provide are newspaper images (like you saw in week 3). Your task is to write python code which allows one to search through the images looking for the occurrences of keywords and faces. E.g. if you search for "pizza" it will return a contact sheet of all of the faces which were located on the newspaper page which mentions "pizza". This will test your ability to learn a new ([library](https://docs.python.org/3/library/zipfile.html)), your ability to use OpenCV to detect faces, your ability to use tesseract to do optical character recognition, and your ability to use PIL to composite images together into contact sheets.
#
# Each page of the newspapers is saved as a single PNG image in a file called [images.zip](./readonly/images.zip). These newspapers are in english, and contain a variety of stories, advertisements and images. Note: This file is fairly large (~200 MB) and may take some time to work with, I would encourage you to use [small_img.zip](./readonly/small_img.zip) for testing.
#
# Here's an example of the output expected. Using the [small_img.zip](./readonly/small_img.zip) file, if I search for the string "Christopher" I should see the following image:
# ![Christopher Search](./readonly/small_project.png)
# If I were to use the [images.zip](./readonly/images.zip) file and search for "Mark" I should see the following image (note that there are times when there are no faces on a page, but a word is found!):
# ![Mark Search](./readonly/large_project.png)
#
# Note: That big file can take some time to process - for me it took nearly ten minutes! Use the small one for testing.

# In[3]:


import zipfile
from PIL import Image,ImageDraw
import pytesseract
import cv2 as cv
import numpy as np
from zipfile import ZipFile

# loading the face detection classifier
face_cascade = cv.CascadeClassifier('readonly/haarcascade_frontalface_default.xml')


# In[4]:


#extract data from zipfile

def extract_zip(filename):
    with ZipFile(filename,'r') as my_zip:
        names=ZipFile.namelist(my_zip)
        return names



# In[5]:


filename1 = 'readonly/small_img.zip'
filename2= 'readonly/images.zip'
extract_zip(filename1)
#extract_zip(filename2)


# In[6]:


#extract images from zip file using pillow

def extarct_img(names):
    img_list=[]
    for i in names:
        img_list.append(Image.open(i))
    return img_list


# In[7]:


names = extract_zip(filename1)
img_list = extarct_img(names)

print(img_list)
#display(img_list[1])


# In[38]:


# detect faces from a image using opencv
# img_name -- name of the image from zip file

def detect_faces(img_name):
    cv_img = cv.imread(img_name)
    gray_img = cv.cvtColor(cv_img,cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_img,1.3)
    faces_list = faces.tolist()


    if faces_list is []:
        return print('But there were no faces in that file!')
# now using faces_list, i'll draw rectangle on the faces using pillow
# then crop that portion
# then save it in a list

    pil_img = Image.fromarray(gray_img,mode='L')
    draw = ImageDraw.Draw(pil_img)

    thum_list=[]

    for x,y,w,h in faces_list:
        draw.rectangle( (x,y,x+w,y+h),outline='white' )
        cr_img = pil_img.crop ( ((x,y,x+w,y+h)) )
        cr_img.thumbnail( (100,100) )
        thum_list.append(cr_img)

    return thum_list


# In[9]:


x=detect_faces(names[1])


# In[37]:


for i in x:
    display(i)


# In[10]:


# now we'll build a canvas/contact sheet
def my_canvas(thum_list):
    canvas=Image.new( thum_list[0].mode , (len(thum_list)*100,100) )
    x,y=0,0
    for i in thum_list:
        canvas.paste(i, (x,y) )
        x+=100
    return canvas



# In[11]:


display(my_canvas(x))


# In[12]:


# now we'll use pytesseract to extract texts from those images

def text_extract(pil_img):
    text=pytesseract.image_to_string(pil_img)
    return text


# In[13]:


#list of all the texts from all the images
text_list=[]

for i in img_list:
    t=text_extract(i)
    text_list.append(t)


# In[14]:


len(text_list)


# # now lets wrap all the things together
#

# In[39]:


filename='readonly/small_img.zip'

names = extract_zip(filename)  # names of images
img_list = extarct_img(names)  # pil images

canvas_list=[]

for i in names:
    thum_list = detect_faces(i)   # thumbnails from each pages
    canvas_list.append(my_canvas(thum_list))  # canvas of all faces in each pages









# In[40]:


search_word = 'Chris'
for i in range(len(text_list)):
    if search_word in text_list[i]:
        print ('Results found in file {}'.format(names[i]))
        display(canvas_list[i])


# In[41]:


search_word = 'Dingell'
for i in range(len(text_list)):
    if search_word in text_list[i]:
        print ('Results found in file {}'.format(names[i]))
        display(canvas_list[i])


# In[44]:


search_word = 'The_Quiet_Wolf'
out=0
for i in range(len(text_list)):
    if search_word in text_list[i]:
        print ('Results found in file {}'.format(names[i]))
        display(canvas_list[i])
    else:
        out+=1
if out==len(text_list):
    print('The word is not found in any images')


# # for final file

# In[36]:


filename2 = 'readonly/images.zip'
names = extract_zip(filename2)  # names of images
img_list = extarct_img(names)  # pil images

canvas_list=[]

for i in names:
    thum_list = detect_faces(i)   # thumbnails from each pages
    canvas_list.append(my_canvas(thum_list))  # canvas of all faces in each pages
