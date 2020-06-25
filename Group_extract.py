#pip install pytesseract
#sudo apt install tesseract-ocr
import pytesseract
import cv2
from PIL import Image
import os,sys
import pdf2image
import shutil

pytesseract.pytesseract.tesseract_cmd = r"D:Tesseract-OCR/tesseract.exe"     #Set to your installation path

if('Output' not in os.listdir()):
        os.mkdir('Output')

if('PDF_images' not in os.listdir()):
        os.mkdir('PDF_images')

flocation=''
if(len(sys.argv)<2):
    flocation=input("Enter the path to the folder containing the pdfs. (Entire path) :")
else:
    flocation=str(sys.argv[1])
try:
    a=os.listdir(flocation)
except:
    flocation=input('Folder not found.\n Enter a valid path:\t')

    print(os.listdir(flocation))

pdfs=[ele for ele in os.listdir(flocation) if '.pdf' in ele]
if(len(pdfs)==0):
    print('No pdfs found!')
    exit()
print(pdfs)
for file in pdfs:
    file_location=flocation+'/'+file
    pages = pdf2image.convert_from_path(file_location,500,grayscale=True) 

    #Converting the pages of the pdf to images.
    fdir=str(file)[:-4]
    
    if(fdir not in os.listdir('PDF_images')):
        os.mkdir('PDF_images/'+fdir)
    #Keep a counter to store the images
    image_counter = 1
    for page in pages: 
        filename = "PDF_images/"+fdir+"/page_"+str(image_counter)+".jpg"
        # Save the image of the page in system 
        page.save(filename, 'JPEG') 
        image_counter = image_counter + 1

    #Extracting text from the pages
    
    if(fdir not in os.listdir('Output')):
        os.mkdir('Output/'+fdir)

    flimit=image_counter      #flimit is greater than total number of images by 1s
    print("FILE:"+ file)
    for i in range(1,flimit):
        print("Extracting => Page "+str(i))
        o_fname="Output/"+fdir+"/page_"+str(i)+".txt"
        with open(o_fname,'w') as f:
            filename="PDF_images/"+fdir+"/page_"+str(i)+".jpg"
            text = str(((pytesseract.image_to_string(Image.open(filename),config='--psm 1 oem 2')))) #Works on RGB data, thus used PIL
            f.write(text)
        f.close()
print("Extracted and stored in the folder named 'Output'")