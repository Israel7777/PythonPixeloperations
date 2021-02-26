#importing Python pillow library for image processing 
from PIL import Image

#method to find out black pixels 
def to_countblackPixel():
  
    #to open image , image to be placed in same directory as the code is placed 
    img = Image.open('[image name].[image format]')# ex : testimage.png
    
    #list containing the RGB value of Black pixel
    black32bitlist = [0,0,0]
    
    #x = iteration variable  , countblack = count variable for black pixel initialized to zero
    x =countblack = 0
    
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
            if list1[0] == black32bitlist[0]:
                if list1[1] == black32bitlist[1]:
                  if list1[2] == black32bitlist[2]:
                        countblack = countblack + 1
                
            y = y + 1
        x = x + 1
        
    #print number of black pixels
    print(countblack)

#define main method
def main():
    to_countblackPixel()

#main method definition 
if __name__ == "__main__":
    main()
