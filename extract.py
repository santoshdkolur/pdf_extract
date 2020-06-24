#pip install pytesseract
#sudo apt install tesseract-ocr
import pytesseract
import cv2
from PIL import Image
import os
import pdf2image
import shutil

pytesseract.pytesseract.tesseract_cmd = r"D:Tesseract-OCR/tesseract.exe"     #Set to your installation path

while(True):
	file=input("Enter the filename with the extension. Ex: ocr.pdf\n")
	if(file in os.listdir()):
		break;
	else:
		print("File not found! Try again.")

pages = pdf2image.convert_from_path(file, 300,grayscale=True) 

#Converting the pages of the pdf to images.
if('PDF_images' not in os.listdir()):
	os.mkdir('PDF_images')
#Keep a counter to store the images
image_counter = 1
for page in pages: 
    filename = "PDF_images/page_"+str(image_counter)+".jpg"
    # Save the image of the page in system 
    page.save(filename, 'JPEG') 
    image_counter = image_counter + 1

#Extracting text from the pages
if('Output' in os.listdir()):
	shutil.rmtree('Output')
	os.mkdir('Output')
else:
	os.mkdir('Output')

flimit=image_counter      #flimit is greater than total number of images by 1
for i in range(1,flimit):
    print("Extracting => Page "+str(i))
    o_fname="Output/page_"+str(i)+".txt"
    with open(o_fname,'w') as f:
        filename="PDF_images/page_"+str(i)+".jpg"
        text = str(((pytesseract.image_to_string(Image.open(filename))))) #Works on RGB data, thus used PIL
        f.write(text)
    f.close()




