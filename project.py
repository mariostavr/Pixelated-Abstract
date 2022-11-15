
#============================= LIBRARIES ==============================
import sys
import keyboard
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from numpy import random
from matplotlib.pyplot import *
from matplotlib.colors import ListedColormap,LinearSegmentedColormap
from PIL import Image  
import os
import turtle
from turtle import done
from os import path
from tkinter import *
from PIL import ImageTk,Image  
#======================================================================


#========================= FUNCTION - GENERATE =========================
def gen(x, y, clms, rows, color):
    fig = plt.figure(figsize=(int(clms)+5, int(rows)+5))
    fig.suptitle('Results ' + str(counter), fontsize=25)
    for i in range(1, int(clms)*int(rows) +1):
        img_rlt = np.random.randint(10, size=(int(x),int(y)))
        fig.add_subplot(int(rows), int(clms), i)
        ax = plt.gca()
        ax.axes.xaxis.set_visible(False)
        ax.axes.yaxis.set_visible(False)
        plt.title(str(i))
        plt.imshow(img_rlt, cm.get_cmap(color), interpolation='none')   
    plt.savefig('Results' + str(counter) + '.png')
    img_rlt = Image.open('Results' + str(counter) + '.png')
    img_rlt.show()
#======================================================================


#----------------------------------------------------------------------Welcome Screen Message.
print("\n\n\t>>> Welcome! Press SPACE to start or ESC to cancel.")  
counter = 1

#----------------------------------------------------------------------Start/End Program
while True:
    if keyboard.is_pressed('Space'):
        break
    elif keyboard.is_pressed('Esc'):
        print('\t>>> Program ended!\n')
        exit()


#----------------------------------------------------------------------Restart Program
while True:

    #----------------------------------------------------------------------Input Information
    size_x = input("\n\t>>> Choose size for width (1-10): ")
    size_y = input("\t>>> Choose size for height (1-10): ")
    columns = input("\t>>> Choose number of columns (1-10): ")
    rows = input("\t>>> Choose number of rows (1-10): ")


    #----------------------------------------------------------------------Method
    flag = True
    option = input("\n\t>>> Do you want to combine two colors of your choice? (Yes/No): ")
    
    while flag:

        if option == "Yes":
            #----------------------------------------------Combining Colors
            flag = False
            
            #------------------------Read File
            colorNames = open('Colors.txt')
            file = colorNames.read()

            while True:
                color1 = input("\n\t>>> Choose color 1: ")
                color2 = input("\t>>> Choose color 2: ") 

                if color1 not in file or color2 not in file:
                    print("\n\t>>> Something went wrong. Press SHIFT to see the available colors or ESC to continue.")

                    while True:
                        if keyboard.is_pressed('Shift'):
                            if path.exists('Colors.png'):
                                imgColors = cv2.imread(r'./Colors.png')
                                cv2.imshow(r'./Colors.png', imgColors)
                            else:
                                import colors
                                imgColors = cv2.imread(r'./Colors.png')
                                cv2.imshow(r'./Colors.png', imgColors)
                            break
                        elif keyboard.is_pressed('Esc'):
                            break
                else:
                    break

            N = 256
            clr_1 = np.ones((N, 4))
            clr_1[:, 0] = np.linspace(255/256, 1, N) 
            clr_1[:, 1] = np.linspace(232/256, 1, N) 
            clr_1[:, 2] = np.linspace(11/256, 1, N) 

            clr_2 = np.ones((N, 4))
            clr_2[:, 0] = np.linspace(255/256, 1, N)
            clr_2[:, 1] = np.linspace(0/256, 1, N)
            clr_2[:, 2] = np.linspace(65/256, 1, N)
            
            clr_1_cmp = ListedColormap(color1)
            clr_2_cmp = ListedColormap(color2)

            colors_mixed = np.vstack((clr_1_cmp(np.linspace(0, 1, 128)), clr_2_cmp(np.linspace(1, 0, 128))))
            clr = ListedColormap(colors_mixed, name='color')


        elif option == "No":

            #----------------------------------------------------------------------Using Palette
            flag = False

            print("\n\t>>> Press SHIFT to open the list or ESC to cancel.")

            while True:
                if keyboard.is_pressed('Shift'):
                    if path.exists('Palette.png'):
                        imgPalette = cv2.imread(r'./Palette.png')
                        cv2.imshow(r'./Palette.png', imgPalette)
                    else:
                        print("\t>>> Importing Palette...")
                        import palette
                        print('\t\t>>> Imported!')
                        imgPalette = cv2.imread(r'./Palette.png')
                        cv2.imshow(r'./Palette.png', imgPalette)

                    while True:
                        clr = input("\n\t>>> Choose a color from the list: ")   
                        if clr not in palette.clr_names:
                            print('\t>>> Wrong name. Try again')
                        else:
                            break                       
                    break
                elif keyboard.is_pressed("Esc"):
                    flag = True
                    break
                
        else:
            option = input("\t>>> Something went wrong. Try Again: ")

    #----------------------------------------------------------------------Show Results
    gen(size_x, size_y, columns, rows, clr)

    #----------------------------------------------------------------------Restart/End Program
    print('\n\t>>> Press Esc to end program or SHIFT to restart.')
    while True:
        if keyboard.is_pressed('Esc'):
            print('\t>>> Program ended!\n')
            if os.path.exists('./Colors.png'):
                os.remove("./Colors.png")
            if os.path.exists('./Palette.png'):
                os.remove("./Palette.png") 
            exit()
        elif keyboard.is_pressed('Shift'):
            print('\t>>> Program restarted.')
            counter = counter + 1
            break
    
