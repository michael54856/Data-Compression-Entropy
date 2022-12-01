from cv2 import CAP_PROP_XI_DEBOUNCE_T0
import numpy as np
import cv2
import math

img = cv2.imread('image2.png', cv2.IMREAD_GRAYSCALE)
temp = np.array(img)
arr = temp.reshape(-1)

length = arr.shape[0]

#white vale is 255
#black value is 0

whiteCount = 0 
blackCount = 0

for i in range(length):
    x = arr[i]
    if x == 0:
        blackCount += 1
    else:
        whiteCount += 1

whiteProbablity = whiteCount/length
blackProbablity = blackCount/length

w_w = 0 #last white and next white
b_w = 0 #last white and next black
w_b = 0 #last black and next white
b_b = 0 #last black and next black


for i in range(1,length):
    if arr[i] == 0 and arr[i-1] == 0: #b_b
        b_b += 1
    elif arr[i] == 255 and arr[i-1] == 0: #w_b
        w_b += 1
    elif arr[i] == 0 and arr[i-1] == 255: #b_w
        b_w += 1
    elif arr[i] == 255 and arr[i-1] == 255: #w_w
        w_w += 1

p_w_w = 0 #probability of last white and next white
p_b_w = 0 #probability of last white and next black
p_w_b = 0 #probability of last black and next white
p_b_b = 0 #probability of last black and next black

if w_w+b_w > 0:
    p_w_w = w_w / (w_w+b_w)
if w_w+b_w > 0:
    p_b_w = b_w / (w_w+b_w)
if w_b+b_b > 0:
    p_w_b = w_b / (w_b+b_b)
if w_b+b_b > 0:
    p_b_b = b_b / (w_b+b_b)

H_w = 0
if p_w_w > 0:
    H_w += p_w_w*math.log((1.0/p_w_w),2)
if p_b_w > 0:
    H_w += p_b_w*math.log((1.0/p_b_w),2)
    
H_b = 0
if p_w_b > 0:
    H_b += p_w_b*math.log((1.0/p_w_b),2)
if p_b_b > 0:
    H_b += p_b_b*math.log((1.0/p_b_b),2)

e1 = H_w*whiteProbablity + H_b*blackProbablity
print(f'1st-order entropy: {e1}')


w_ww = 0 #last white_white and next white
b_ww = 0 #last white_white and next black
w_wb = 0 #last white_black and next white
b_wb = 0 #last white_black and next black
w_bw = 0 #last black_white and next white
b_bw = 0 #last black_white and next black
w_bb = 0 #last black_black and next white
b_bb = 0 #last black_black and next black

for i in range(2,length):
    if arr[i] == 255 and arr[i-2] == 255 and arr[i-1] == 255: #w_ww
        w_ww += 1
    elif arr[i] == 0 and arr[i-2] == 255 and arr[i-1] == 255: #b_ww
        b_ww += 1
    elif arr[i] == 255 and arr[i-2] == 255 and arr[i-1] == 0: #w_wb
        w_wb += 1
    elif arr[i] == 0 and arr[i-2] == 255 and arr[i-1] == 0: #b_wb
        b_wb += 1
    elif arr[i] == 255 and arr[i-2] == 0 and arr[i-1] == 255: #w_bw
        w_bw += 1
    elif arr[i] == 0 and arr[i-2] == 0 and arr[i-1] == 255: #b_bw
        b_bw += 1
    elif arr[i] == 255 and arr[i-2] == 0 and arr[i-1] == 0: #w_bb
        w_bb += 1
    elif arr[i] == 0 and arr[i-2] == 0 and arr[i-1] == 0: #b_bb
        b_bb += 1

total = w_ww+b_ww+w_wb+b_wb+w_bw+b_bw+w_bb+b_bb

p_w_ww = 0 #probability of last white_white and next white
p_b_ww = 0 #probability of last white_white and next black
p_w_wb = 0 #probability of last white_black and next white
p_b_wb = 0 #probability of last white_black and next black
p_w_bw = 0 #probability of last black_white and next white
p_b_bw = 0 #probability of last black_white and next black
p_w_bb = 0 #probability of last black_black and next white
p_b_bb = 0 #probability of last black_black and next black

if (w_ww+b_ww) > 0:
    p_w_ww = w_ww / (w_ww+b_ww)
if (w_ww+b_ww) > 0:
    p_b_ww = b_ww / (w_ww+b_ww)
if (w_wb+b_wb) > 0:
    p_w_wb = w_wb / (w_wb+b_wb)
if (w_wb+b_wb) > 0:
    p_b_wb = b_wb / (w_wb+b_wb)
if (w_bw+b_bw) > 0:
    p_w_bw = w_bw / (w_bw+b_bw)
if (w_bw+b_bw) > 0:
    p_b_bw = b_bw / (w_bw+b_bw)
if (w_bb+b_bb) > 0:
    p_w_bb = w_bb / (w_bb+b_bb)
if (w_bb+b_bb) > 0:
    p_b_bb = b_bb / (w_bb+b_bb)

H_ww = 0
if p_w_ww > 0:
    H_ww += p_w_ww*math.log((1.0/p_w_ww),2)
if p_b_ww > 0:
    H_ww += p_b_ww*math.log((1.0/p_b_ww),2)

H_wb = 0
if p_w_wb > 0:
    H_wb += p_w_wb*math.log((1.0/p_w_wb),2)
if p_b_wb > 0:
    H_wb += p_b_wb*math.log((1.0/p_b_wb),2)

H_bw = 0
if p_w_bw > 0:
    H_bw += p_w_bw*math.log((1.0/p_w_bw),2)
if p_b_bw > 0:
    H_bw += p_b_bw*math.log((1.0/p_b_bw),2)

H_bb = 0
if p_w_bw > 0:
    H_bb += p_w_bb*math.log((1.0/p_w_bb),2)
if p_b_bw > 0:
    H_bb += p_b_bb*math.log((1.0/p_b_bb),2)

p_ww = (w_ww+b_ww) / total
p_wb = (w_wb+b_wb) / total
p_bw = (w_bw+b_bw) / total
p_bb = (w_bb+b_bb) / total

e2 = H_ww*p_ww + H_wb*p_wb + H_bw*p_bw + H_bb*p_bb
print(f'2nd-order entropy: {e2}')




mylist = []
for i in range(0,length-1):
    mylist.append(int(arr[i+1])-int(arr[i]))
diffArr = np.array(mylist)

Count255 = 0
Count0 = 0
CountNegative255 = 0
for i in diffArr:
    if i == 0:
        Count0 += 1
    elif i == 255:
        Count255 += 1
    else:
        CountNegative255 += 1

totalCount = len(diffArr)
e3 = 0
p_255 = Count255/totalCount
p_0 = Count0/totalCount
p_Negative255 = CountNegative255/totalCount

if p_255 > 0:
    e3 += p_255 * math.log((1.0/p_255),2)
if p_0 > 0:
    e3 += p_0 * math.log((1.0/p_0),2)
if p_Negative255 > 0:
    e3 += p_Negative255 * math.log((1.0/p_Negative255),2)

print(f'neighbor difference entropy: {e3}')





