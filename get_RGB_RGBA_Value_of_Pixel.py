#Importing pillow library of python for image processing
from PIL import Image

#method to get RGB-RGBA Value for a specific pixel in a image
def to_getRGBARGB():
  
    #place the image in the same path as the code 
    img = Image.open('[imagename].[format]') #ex: testpicture.jpg
    
    #enter the pixel value
    x,y = (<pixel x value>,<pixel y value>) ex: 300,300
    
    #pixel read as co-ordinates of image
    coordinate = x, y
    
    #RGB/RGBA Caught in list 
    list1 = list(img.getpixel(coordinate))
    print(list1)

#main method
def main():
    to_getRGBARGB()

#call to main method
if __name__ == "__main__":
    main()
