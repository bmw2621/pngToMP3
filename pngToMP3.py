#! /usr/bin/python3

# import the necessary packages
from PIL import Image
import pytesseract
import argparse
import cv2
import os
from gtts import gTTS 

def getText(fileToConvert, thresh=True, blur=False):
    """getText function loads the image on the path passed to the function, converts it to
    greyscale, and extracts text using pytesseract package (package is an interface with tesseract
    software which must be installed separately).  If thresh arguement default is set to true, and 
    should be used if the loaded image needs to be sharpened.  If the blur arguement default is set 
    to false, and should be set to true if the passed image requires moise reduction to prevent 
    interference with character recognition"""
  
    # load the example image and convert it to grayscale
    image = cv2.imread(fileToConvert)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
    # check to see if we should apply thresholding to preprocess the image
    if thresh:
        gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
 
    # make a check to see if median blurring should be done to remove noise
    elif blur:
        gray = cv2.medianBlur(gray, 3)
 
    # write the grayscale image to disk as a temporary file so we can apply OCR to it
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)

    # load the image as a PIL/Pillow image, apply OCR, and then delete the temporary file
    mytext = pytesseract.image_to_string(Image.open(filename))
    os.remove(filename)
    print(mytext)

    # show the output images
    cv2.imshow("Image", image)
    cv2.imshow("Output", gray)

    return mytext

def convertToSpeech(mytext, outputTitle, playAfter):
    """convertToSpeech function receives text to be converted to audio file, the output filename, and the option to play
    the file after the conversion.  Line 62 system call should reflect the appropriate command to run the preferred playback
    software (default is mpg123)"""
  
    # Language in which you want to convert 
    language = 'en'
  
    # Passing the text and language to the engine, here we have marked slow=False. Which tells the module that the converted audio should have a high speed 
    myobj = gTTS(text=mytext, lang=language, slow=False) 

    # Saving the converted audio in a mp3 file named from user input above
    myobj.save("{}.mp3".format(outputTitle)) 
  
    # Playing the converted file 
    if playAfter:
        os.system("mpg123 {}.mp3".format(outputTitle))

def main():
    compiledText = ""
    prep = input("Preprocess? (T) Threshold  (B) Blur  (N) None   ")
    outputTitle = input("Output filename?   ")
    play = input("Play file after compiling? Y/N   ")
    if play.lower() == "y":
        playAfter = True
    else:
        playAfter = False
    if outputTitle[-4:] == ".mp3":
        outputTitle = outputTitle[:-4]
    prep = prep.lower()
    for root, dirs, files in os.walk("."):  
        for filename in files:
            if prep == 't':
                compiledText += str(" " + getText(filename))
            elif prep == 'b':
                compiledText += str(" " + getText(filename, thresh=False, blur=True))
            elif prep == 'n':
                compiledText += str(" " + getText(filename, thresh=False, blur=False))
    convertToSpeech(compiledText, outputTitle, playAfter)
    
if __name__ == "__main__":
    main()
