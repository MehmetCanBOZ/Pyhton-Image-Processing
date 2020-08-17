import os
from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
from pygame import mixer
import pygame
import cv2
import numpy as np

root=Tk()#Create window and store it inside the root variable

root2=Tk()
root2.title("AREA OF THE DETECTED OBJECT")
root2.geometry("500x600") #Width x Height


#create menubar
menubar=Menu(root)#create a menu bar
root.config(menu=menubar)#fixed the menubar at top andto get submenus
menubar2=Menu(root2)#create a menu bar
root2.config(menu=menubar2)#fixed the menubar at top andto get submenus

def passing():
    pass
def browse_file():#browse function
    global filename
    filename=filedialog.askopenfilename()

sub_menu=Menu(menubar,tearoff=0)#make submenu it different from menu when we give menubar to value but in menu it give root
menubar.add_cascade(label="File",menu=sub_menu)
sub_menu.add_command(label="Exit",command=root.destroy)

def about_us():
    tkinter.messagebox.showinfo('NDVI APP','This is NDVI image processing app')

sub_menu=Menu(menubar,tearoff=0)#make submenu it different from menu when we give menubar to value but in menu it give root
menubar.add_cascade(label="Help",menu=sub_menu)
sub_menu.add_command(label="About Us",command=about_us)


#create submenus
sub_menu2=Menu(menubar2,tearoff=0)#make submenu it different from menu when we give menubar to value but in menu it give root
menubar2.add_cascade(label="File",menu=sub_menu2)
sub_menu2.add_command(label="Exit",command=root2.destroy)




sub_menu2=Menu(menubar2,tearoff=0)#make submenu it different from menu when we give menubar to value but in menu it give root
menubar2.add_cascade(label="Help",menu=sub_menu2)
sub_menu2.add_command(label="About Us",command=about_us)

mixer.init()  #initializing the mixer

root.title("TAGEM")#title of the window


text=Label(root,text='NDVI APP')#write text on window, first parameter is the window itself, second parameter is the type of text yo want to write
text.pack(pady=10)#it help to show text in the window it just like packing yr clothes in to the bag#pady give space between widget

text=Label(root2,text='AREA OF THE OBJECT')#write text on window, first parameter is the window itself, second parameter is the type of text yo want to write
text.pack(pady=10)



upper_frame=Frame(root)
upper_frame.pack(pady=10)

upper_frame2=Frame(root2)
upper_frame2.pack(pady=10)




name=Label(upper_frame, text="NDVI= ",font='Times 15 italic')
name.grid(row=0,column=0,padx=10)

name2=Label(upper_frame2, text="AREA= ",font='Times 15 italic')

name2.grid(row=0,column=0,padx=10)

img = PhotoImage(file="images/tagem.png")
img_gg=Button(upper_frame,image=img,command=passing)
img_gg.grid(row=0,column=2,padx=10)


#img2 = PhotoImage(file="play.png")
#img_gg2=Button(upper_frame2,image=img2,command=passing)
#img_gg2.grid(row=0,column=1,padx=10)

e1 = Entry(upper_frame)
e1.grid(row=0,column=1,padx=10)



text_1=Label(upper_frame,text="0=Diseased Area",relief=SUNKEN,anchor=W,font='Times 15 italic',fg='black')#SUNKEN sunk it in the bar
text_1.grid(row=1,column=0,padx=10,pady=5)

text_1=Label(upper_frame,text="1= Soil Area",relief=SUNKEN,anchor=W,font='Times 15 italic',fg='black')#SUNKEN sunk it in the bar
text_1.grid(row=1,column=1,padx=10,pady=5)

text_1=Label(upper_frame,text="2=Plant Area",relief=SUNKEN,anchor=W,font='Times 15 italic',fg='black')#SUNKEN sunk it in the bar
text_1.grid(row=1,column=2,padx=10,pady=5)

middle_frame2=Frame(root2)#arrange the widget with seperate it with the window so we use another frame to change the position of the widget
middle_frame2.pack(padx=30,pady=30)

middle_frame=Frame(root)#arrange the widget with seperate it with the window so we use another frame to change the position of the widget
middle_frame.pack(padx=30,pady=30)

play_photo=PhotoImage(file='images/folder.png')
play_btn=Button(middle_frame,image=play_photo,command=browse_file)#create a button variable embedded(image=play_photo) image in to button
play_btn.grid(row=0,column=0,padx=10)#grid system row and column just website
#play_btn.pack(side=LEFT,padx=10)#package the button

status_bar=Label(root,text="Welcome to NDVI APP",relief=SUNKEN,anchor=W)#SUNKEN sunk it in the bar
status_bar.pack(side=BOTTOM,fill=X)#side decide the direction fill make it full in the coordinate


def ndvi_func():
    value = e1.get()
    ndvi_value = int(value)

    # cv2.namedWindow("Tracking")
    # cv2.createTrackbar("NDVI", "Tracking", 0, 2, nothing)
    def nothing(x):
        pass

    while True:

        frame = cv2.imread(filename)
        # convert image to HSV image
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # define upper and lower value for blue color
        # ndvi = cv2.getTrackbarPos("NDVI", "Tracking")
        imgray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(imgray, 150, 255, 0)

        if ndvi_value == 2:
            l_b = np.array([32, 72, 93])
            u_b = np.array([107, 255, 255])


        elif ndvi_value == 1:
            l_b = np.array([0, 23, 0])
            u_b = np.array([26, 255, 255])

        else:
            l_b = np.array([0, 23, 0])
            u_b = np.array([14, 255, 255])


        mask = cv2.inRange(hsv, l_b, u_b)
        res = cv2.bitwise_and(frame, frame, mask=mask)

        points = []
        """shapesdetection"""
        # imgGrey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # _, thrash = cv2.threshold(imgGrey, 240, 255, cv2.THRESH_BINARY)
        contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]


        if ndvi_value == 2:
            i = 2
            enter = 1
            i1=2

            text_12 = Label(upper_frame2, text="NDVI 2", relief=SUNKEN, anchor=W, font='Times 15 italic',
                            fg='black')  # SUNKEN sunk it in the bar
            text_12.grid(row=0, column=0, padx=10, pady=5)

            if (enter == 1):
                for contour in contours:
                    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
                    cv2.drawContours(frame, [approx], 0, (0, 0, 0), 2)

                    # print(len(approx))
                    x = approx.ravel()[0]
                    y = approx.ravel()[1] - 5
                    if len(approx) != 4:
                        area = cv2.contourArea(contour)
                    # cv2.putText(frame, str(area), (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0))
                    text_12 = Label(upper_frame2, text=str(area), relief=SUNKEN, anchor=W, font='Times 15 italic',
                                    fg='black')  # SUNKEN sunk it in the bar
                    text_12.grid(row=i1, column=0, padx=10, pady=5)
                    i1=i1+1

                    enter += 1
                    if len(approx) == 4:
                        x1, y1, w, h = cv2.boundingRect(approx)
                        rect_area = w * h / 10
                        # cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 0), 2)
                        aspectRatio = float(w) / h

                        # cv2.putText(frame, "rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
                        # cv2.putText(frame, str(i), (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.3, (255, 255, 255))
                        area = cv2.contourArea(contour)
                        # cv2.putText(frame, str(rect_area), (x - 10, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0))
                        text_12 = Label(upper_frame2, text=str(area), relief=SUNKEN, anchor=W, font='Times 15 italic',
                                        fg='black')  # SUNKEN sunk it in the bar
                        text_12.grid(row=i, column=1, padx=10, pady=5)
                        # print("rectangle  "+ str(i))
                        # print("area of rectangle "+ str(i)+str(area))
                        # print(approx)
                        i = i + 1
                        enter += 1
            else:
                pass

            cv2.imshow("frame", frame)
            cv2.imshow("mask", mask)
            cv2.imshow("res", res)
            root2.mainloop()

        elif ndvi_value == 1:
            i = 2
            enter = 1
            i1=2
            text_12 = Label(upper_frame2, text="NDVI 1", relief=SUNKEN, anchor=W, font='Times 15 italic',
                            fg='black')  # SUNKEN sunk it in the bar
            text_12.grid(row=0, column=2, padx=10, pady=5)
            if (enter == 1):
                for contour in contours:
                    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
                    cv2.drawContours(frame, [approx], 0, (0, 0, 0), 2)

                    # print(len(approx))
                    x = approx.ravel()[0]
                    y = approx.ravel()[1] - 5
                    if len(approx) != 4:
                        area = cv2.contourArea(contour)
                    # cv2.putText(frame, str(area), (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0))
                    text_12 = Label(upper_frame2, text=str(area), relief=SUNKEN, anchor=W, font='Times 15 italic',
                                    fg='black')  # SUNKEN sunk it in the bar
                    text_12.grid(row=i1, column=2, padx=10, pady=5)
                    i1 = i1 + 1
                    enter += 1

                    if len(approx) == 4:
                        x1, y1, w, h = cv2.boundingRect(approx)
                        rect_area = w * h / 10
                        # cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 0), 2)
                        aspectRatio = float(w) / h

                        # cv2.putText(frame, "rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
                        # cv2.putText(frame, str(i), (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.3, (255, 255, 255))
                        area = cv2.contourArea(contour)
                        # cv2.putText(frame, str(rect_area), (x - 10, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0))
                        text_12 = Label(upper_frame2, text=str(area), relief=SUNKEN, anchor=W, font='Times 15 italic',
                                        fg='black')  # SUNKEN sunk it in the bar
                        text_12.grid(row=i, column=3, padx=10, pady=5)
                        # print("rectangle  "+ str(i))
                        # print("area of rectangle "+ str(i)+str(area))
                        # print(approx)
                        i = i + 1
                        enter += 1
            else:
                pass

            cv2.imshow("frame", frame)
            cv2.imshow("mask", mask)
            cv2.imshow("res", res)
            root2.mainloop()
        else:
            i = 2
            i1=2
            enter = 1
            text_12 = Label(upper_frame2, text="NDVI 0", relief=SUNKEN, anchor=W, font='Times 15 italic',
                            fg='black')  # SUNKEN sunk it in the bar
            text_12.grid(row=0, column=4, padx=10, pady=5)
            if (enter == 1):
                for contour in contours:
                    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
                    cv2.drawContours(frame, [approx], 0, (0, 0, 0), 2)

                    # print(len(approx))
                    x = approx.ravel()[0]
                    y = approx.ravel()[1] - 5
                    if len(approx) != 4:
                        area = cv2.contourArea(contour)
                    # cv2.putText(frame, str(area), (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0))
                        text_12 = Label(upper_frame2, text=str(area), relief=SUNKEN, anchor=W, font='Times 15 italic',
                                        fg='black')  # SUNKEN sunk it in the bar
                        text_12.grid(row=i1, column=4, padx=10, pady=5)
                        i1 = i1 + 1
                        enter += 1

                    if len(approx) == 4:
                        x1, y1, w, h = cv2.boundingRect(approx)
                        rect_area = w * h / 10
                        # cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 0), 2)
                        aspectRatio = float(w) / h

                        # cv2.putText(frame, "rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
                        # cv2.putText(frame, str(i), (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.3, (255, 255, 255))
                        area = cv2.contourArea(contour)
                        # cv2.putText(frame, str(rect_area), (x - 10, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0))
                        text_12 = Label(upper_frame2, text=str(area), relief=SUNKEN, anchor=W, font='Times 15 italic',
                                        fg='black')  # SUNKEN sunk it in the bar
                        text_12.grid(row=i, column=5, padx=10, pady=5)

                        # print("rectangle  "+ str(i))
                        # print("area of rectangle "+ str(i)+str(area))
                        # print(approx)
                        i = i + 1
                        enter += 1
            else:
                pass

            cv2.imshow("frame", frame)
            cv2.imshow("mask", mask)
            cv2.imshow("res", res)
            root2.mainloop()


        text_12.grid(row=i, column=2, padx=10, pady=5)
        if cv2.waitKey(1) == ord('q'):
            break

btn = Button(middle_frame, text="Process the Image",command=ndvi_func)
btn.grid(column=1, row=0)
root.mainloop()#loop the window to see it without destroy

