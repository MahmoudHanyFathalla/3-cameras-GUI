from distutils.cmd import Command
from pickle import TRUE
from tkinter import Button, Tk, Label, X, Frame, Y, LEFT, BOTH
import cv2
from tkinter import *
from PIL import Image, ImageTk 
import random 
import os

root = Tk()

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

root.geometry("%dx%d" % (width, height))

root.title("ROV")

# Initialize frames
root.attributes('-fullscreen', True)
snp_cnt=[0]
shots = [0,0,0]
try:
    with open ('numberOfShots', 'r') as f:
        shots[0] = int(f.readline())
        shots[1] = int(f.readline())
        shots[2] = int(f.readline())

except FileNotFoundError:
    f = open ('numberOfShots', 'w')
    f.write('0\n0\n0')
    f.close()
except FileExistsError:
    pass
try:
    os.mkdir('camera 1')
    os.mkdir('camera 2')
    os.mkdir('camera 3')
except FileExistsError:
    pass
def snaps(n,camera_shot,snp_cnt):
    
    ret, frame = camera_shot.read()
    # cv2.imwrite('Frame'+str(snp_cnt[0])+'.jpg', frame)
    file_name = 'Frame'+str(shots[n-1])+'.jpg'
    if camera_shot==camera_cap0:
        cv2.imwrite(os.path.join('camera 1', file_name), frame)
        shots[0] += 1
    elif camera_shot==camera_cap1:
        cv2.imwrite(os.path.join('camera 2', file_name), frame)
        shots[1] += 1
    else:
        print('hello')
    # elif camera_shot==camera_cap2:
        # cv2.imwrite(os.path.join('camera 3', file_name), frame)
        # shots[2] += 1
    return snp_cnt
     
    

def touch_1(n,width,height,camera_cap):
    dim = (width,height)
    new_window = Toplevel(root)
    new_window.title("camera " + str(n))
    new_window.geometry("%dx%d" % (width, height))

    f3 = Frame(new_window, bg="white")    
    f3.pack(fill=BOTH, expand=True)
    w4 = Button(f3, text="", bg="white", fg="black",relief="sunken",command=lambda:snaps(n,camera_cap,snp_cnt))
    w4.pack(side=LEFT, fill=BOTH, expand=True)

    while True:
        ret,cameras_frame = camera_cap.read()
        cv2image= cv2.cvtColor(cameras_frame,cv2.COLOR_BGR2RGB)
        img = cv2.resize(cv2image, dim,fx = 2, fy = 2, interpolation = cv2.INTER_AREA)
        img = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(image = img)
        w4.imgtk = imgtk
        w4.configure(image=imgtk)
        

        root.update_idletasks()
        root.update()
  
def end():
    with open ('numberOfShots', 'w') as f:
        f.write(str (shots[0]) + '\n')
        f.write(str (shots[1]) + '\n')
        f.write(str (shots[2]) + '\n')
    f.close()
    root.destroy()   


f1 = Frame(root)
f2 = Frame(root)
#roben1=PhotoImage(file="4.png")
# image resize
arr_image=['C:\\Users\\hp\\Downloads\\first-gui-main\\first-gui-main\\6.jpeg','C:\\Users\\hp\\Downloads\\first-gui-main\\first-gui-main\\7.jpeg','C:\\Users\\hp\\Downloads\\first-gui-main\\first-gui-main\\8.jpeg']
photos=random.sample(arr_image,2)
photo1=photos[0]
photo2=photos[1]
img_right=Image.open(photo2)
img_left=Image.open(photo1)
img_right=img_right.resize((width//4,height//2))
img_left=img_left.resize((width//4,height//2))
img_right=ImageTk.PhotoImage(img_right)
img_left=ImageTk.PhotoImage(img_left)
# Initialize labels

w1 = Label(f1, text="Camera", bg="white", fg="black",font=3)
w2 = Button(f1, text="", bg="white", fg="black",relief="sunken",command=lambda:touch_1(1,width,height,camera_cap0))
s1 = Button(w1,text = "Snap1",fg="black",font=3,relief="sunken",width=15,command=lambda:snaps(1,camera_cap0,snp_cnt)).pack(side=LEFT)
s2 = Button(w1,text = "Snap2",fg="black",font=3,relief="sunken",width=15,command=lambda:snaps(2,camera_cap1,snp_cnt)).pack(side=LEFT)
s3 = Button(w1,text = "Snap3",fg="black",font=3,relief="sunken",width=15,command=lambda:snaps(3,camera_cap1,snp_cnt)).pack(side=LEFT)

buttom_exit = Button(w1,text = "X",bg="red",fg="white",font=3,relief="sunken",width=10,command=end)

photo_left=Label(f1,bg="white", image=img_left)
photo_right=Label(f1,bg="white", image=img_right)
w1b = Button(f2, text="", bg="white", fg="black",relief="sunken",command=lambda:touch_1(2,width,height,camera_cap1))
w3b = Button(f2, text="", bg="white", fg="black",relief="sunken",command=lambda:touch_1(3,width,height,camera_cap1))


# Packing level 1
f1.pack(fill=X)
f2.pack(fill=BOTH, expand=True)

# Packing level 2
w1.pack(fill=X)
photo_left.pack(side=LEFT, fill=BOTH, expand=True)
photo_right.pack(side=RIGHT, fill=BOTH, expand=True)
w2.pack(fill=BOTH, expand=True)

buttom_exit.pack(side="right")

w1b.pack(side=LEFT, fill=BOTH, expand=True)

w3b.pack(side=LEFT, fill=BOTH, expand=True)

#for camera 1
camera_cap0 =cv2.VideoCapture(0)
camera_cap0.set(4,400)

#for camera 2
camera_cap1 =cv2.VideoCapture(1)
camera_cap1.set(4,400)

#for camera 3
#camera_cap2 =cv2.VideoCapture(2)
#camera_cap2.set(4,400)

dim = (width,height)
dim1 = (width//2,height//2)
dim2 = (width//2,height//2)
dim3 = (width//2,height//2)

while True:
    ret0,cameras_frame0 = camera_cap0.read()
    cv2image0= cv2.cvtColor(cameras_frame0,cv2.COLOR_BGR2RGB)
    ret1,cameras_frame1 = camera_cap1.read()
    cv2image1= cv2.cvtColor(cameras_frame1,cv2.COLOR_BGR2RGB)
    #ret2,cameras_frame2 = camera_cap2.read()
    #cv2image2= cv2.cvtColor(cameras_frame2,cv2.COLOR_BGR2RGB)
    img1 = cv2.resize(cv2image0,dim1,fx=1,fy=1, interpolation = cv2.INTER_AREA)
    img2 = cv2.resize(cv2image1, dim2,fx=1,fy=1,  interpolation = cv2.INTER_AREA)
    img3 = cv2.resize(cv2image1,dim3, fx=1,fy=1,interpolation = cv2.INTER_AREA)
    img1 = Image.fromarray(img1)
    img2 = Image.fromarray(img2)
    img3 = Image.fromarray(img3)
    imgtk1 = ImageTk.PhotoImage(image = img1)
    imgtk2 = ImageTk.PhotoImage(image = img2)
    imgtk3 = ImageTk.PhotoImage(image = img3)
    w3b.imgtk = imgtk3
    w3b.configure(image=imgtk3)
    w1b.imgtk = imgtk2
    w1b.configure(image=imgtk2)
    w2.imgtk = imgtk1
    w2.configure(image=imgtk1)

    root.update_idletasks()
    root.update()

root.mainloop()
