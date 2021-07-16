#!/usr/bin/env python
# coding: utf-8

# # The Sparks Foundation
# 
# # GRIP July 2021¶
# 
# # Internet of Things and Computer Vision
# 
# # Name: Saujanya Mundargi
# 
# # Task 2: Color Identification of images

# In[1]:


import cv2
import pandas as pd


# In[2]:


#path declaration

img_path = 'colorpic.jpg'
csv_path = 'colors.csv'


# In[3]:


#reading the csv file

index = ["color", "color_name", "hex", "R", "G", "B"]
df = pd.read_csv(csv_path, names=index, header=None)


# In[4]:


#reading the image

img = cv2.imread(img_path)
img = cv2.resize(img, (800, 600))


# In[5]:


#declaring global variables

clicked = False
r = g = b = x_pos = y_pos = 0


# In[6]:


#calculating minimum distance from all colors in csv file and returning the color name

def get_color_name(R, G, B):
    minimum = 10000
    for i in range(len(df)):
        d = abs(R - int(df.loc[i, 'R'])) + abs(G - int(df.loc[i, 'G'])) + abs(B - int(df.loc[i, 'B']))
        if d <= minimum:
            minimum = d
            cname = df.loc[i, "color_name"]
    return cname


# In[7]:


#calculating (x,y) coordinates of mouse double click.

def draw_function(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b, g, r, x_pos, y_pos, clicked
        clicked = True
        x_pos = x
        y_pos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)


# In[8]:


#creating window
cv2.namedWindow("image")
cv2.setMouseCallback('image', draw_function)


# In[ ]:


while True:
    cv2.imshow("image", img)
    if clicked:
        cv2.rectangle(img, (20, 20), (600, 60), (b, g, r), -1)
        text = get_color_name(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)
        cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

        if r + g + b >= 600:
            cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)
        clicked = False

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

