This utility is designed to convert a directory of images to MP3 files by way of Tesseract OCR and the Google Text to Speech API.  To use this script the user must have installed Tesseract OCR, the pytesseract package available in the pip repository, and the gTTS package which is also available in the pip repository.

For the pytesseract package to work, the Tesseract binary must be available in your system path using the call "tesseract".

This script accomplishes its task by walking through all files in the directory the script is run in, passes each image to pytesseract to convert to text, and passes the generated text to Google Text to Speech to generate an mp3.  Script assumes mpg123 is users playback program, if not, update script with appropriate call on line 52.

Ensure there are no other files in the directory of pngs.
<br><br>
Required Packages:<br>
opencv-python  (pip)<br>
pytesseract (pip)<br>
gTTS (pip)<br>
Tesseract OCR - https://github.com/tesseract-ocr/tesseract/wiki/Downloads or in most Linux distribution repositories<br><br>

Optional Package:<br>
mpg123 https://www.mpg123.de/download.shtml or in most Linux distribution repositories or change system call to preferred program<br>
