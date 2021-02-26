#importing python pillow library to perform image processing 
from PIL import Image

#method to count number of pixels in image
def to_countPixel():
    
    # image to be present in same directory where the code is present 
    img = Image.open('[ image name].[format]') #example : picture.png
    
    #obtains height and width of the image and stores in w and h variable 
    w, h = img.size
    
    print(w*h)

#main method
def main():
    to_countPixel()

#main method called
if __name__ == "__main__":
    main()
