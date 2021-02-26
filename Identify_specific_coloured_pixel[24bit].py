#importing Python pillow library for image processing 
from PIL import Image

#method to find out black pixels 
def to_countcolorPixel():
  
    #to open image , image to be placed in same directory as the code is placed 
    img = Image.open('[image name].[image format]')# ex : testimage.png
    
    #list containing the RGB value of colour needed pixel
    colour24bitlist = [<RGB Value>] #ex : black [0,0,0] 
    
    #x = iteration variable  , countcolor = count variable for color pixel initialized to zero
    x =countcolor = 0
    
    #while loop to loop the width of the image 
    while x < img.width:
        
        #y = iteration variable  
        y = 0
        
        #while loop to loop the height of the image 
        while y < img.height:
          
            #value of coordinates taken
            coordinate = x, y
            
             #list containing the RGB value of specific pixel (x,y)
            list1 = list(img.getpixel(coordinate))
            
            #comparing if the pixel is black
            if list1 == color24bitlist:
                countcolor = countcolor + 1
                
            y = y + 1
        x = x + 1
        
    #print number of black pixels
    print(countcolor)

#define main method
def main():
    to_countcolorPixel()

#main method definition 
if __name__ == "__main__":
    main()
