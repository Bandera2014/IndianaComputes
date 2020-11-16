'''
Problem 1: 
1.	Utilizing binary is a simpler data format to share with the Martians since it is either an on and off situation.  Plus, the bits needed is easy to utilize than trying to range 3 values.  
2.	Most software is already built using a binary situation.  
3.  ?????
'''

#Problem2:

from PIL import Image, ImageDraw, ImageFont
from resizeimage import resizeimage
import time
def printTime():
    t = time.localtime()
    current_time = time.strftime("%M:%S", t);
    return current_time
## Convert image by applying a filter
def imageFilter(filter, sourceFile, destFile):
    print('Begin applying ', filter, ' filter to image: ', sourceFile)
    print('Start Processing at: ', printTime());
    mySourceImage = Image.open(sourceFile); # Open the source image file
    myDestImage = Image.new('RGB',mySourceImage.size); # create a new image object for the destination
    width = mySourceImage.size[0];
    height = mySourceImage.size[1];
    # Go through the image line by line and extract each pixel, and
    # manipulate its RGB depending on the filter parameter.
    for x in range(width):
        for y in range(height):
            curPix = mySourceImage.getpixel( (x,y) )
            if(filter == "RED"):
                redPix = curPix[0]; # extract the Red color attribute of current pixel
                myDestImage.putpixel( (x,y), (redPix,0,0) )
            elif (filter == "GREEN"):
                grnPix = curPix[1]; # extract the green color attribute of current pixel
                myDestImage.putpixel( (x,y), (0,grnPix,0) )
            elif (filter == "BLUE"):
                bluPix = curPix[2]; # extract the blue color attribute of current pixel
                myDestImage.putpixel( (x,y), (0,0, bluPix) )
            elif(filter == "GRAYSCALE"):
                2
                # Calculate the sum of 3 colors (R,G, and B) and divide by three.
                #gray = (R + G + B) // 3
                # use putpixel() function to place the “gray” value in the myDestImage
                # Your code eventually goes here (See step 5)
                gray=127
                rpix = int(max(curPix[0],curPix[1],curPix[2]) * 0.50);
                gpix = int(max(curPix[0],curPix[1],curPix[2]) * 0.50);
                bpix = int(max(curPix[0],curPix[1],curPix[2]) * 0.50);
                myDestImage.putpixel( (x,y), (127,127,127) );
        
            else:
                print("Invalid Filter. (usage: RED, GREEN, BLUE, GRAYSCALE)");
                break;
    myDestImage.save(destFile);
    print('End Processing at : ', printTime());

##-------------------------------- MAIN ---------------------------------------------------
def main():
    #Apply Filter
    #imageFilter("RED", "Original_Mars1-nasa.jpg", "_Filtered_Mars1_Red.jpg" );
    #imageFilter("GREEN", "Original_Mars1-nasa.jpg", "_Filtered_Mars1_Grn.jpg" );
    #imageFilter("BLUE", "Original_Mars1-nasa.jpg", "_Filtered_Mars1_Blu.jpg" );
    imageFilter("GRAYSCALE", "Original_Mars2-Small.jpg", "_Filtered_Mars2_Small_Gry1.jpg" );
    imageFilter("GRAYSCALE", "Original_Mars2-Big.jpg", "_Filtered_Mars2_Big_Gry1.jpg" );
    imageFilter("GRAYSCALE", "Original_Mars3-Selfie_Red.jpg", "_Filtered_Mars3_Selfie_Gry1.jpg" );
# Call the main
main()