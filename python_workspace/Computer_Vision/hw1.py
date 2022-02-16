import cv2 as cv

from tkinter import filedialog
from tkinter import *

imagePath = ''

root = Tk()
root.title("Picture Filtering")
root.geometry("540x300+100+100")
root.resizable(False, False)

def getFile():
    global imagePath
    filename = filedialog.askopenfile(initialdir='path', title='select file', filetypes=(('png files', '*.png'), ('all files', '*.*')))
    imagePath=filename.name
    print(imagePath)
    
def meanFilter():
    img1 = cv.imread(imagePath, cv.IMREAD_GRAYSCALE)
    cv.imshow("1",img1,cv.IMREAD_GRAYSCALE)
    cv.waitKey(0)
    cv.destroyAllWindows()
    
def medianFilter():
    pass
    
def RafFilter():
    pass


btngetFile = Button(root, text='select file', command=getFile)
btnMeanFilter = Button(root, text='Mean filter',command=meanFilter)
btnMedianFilter = Button(root, text='Median filter',command=medianFilter)
btnRafFilter = Button(root, text='Raf filter',command=RafFilter)

btngetFile.pack()
btnMeanFilter.pack()
btnMedianFilter.pack()
btnRafFilter.pack()

root.mainloop()
