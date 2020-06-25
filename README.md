# Extract Data from pdfs
Extracts data from pdfs if the data is in the form of images/texts.
The extracted data is stored as a seperate text file for everypage.

Use Group_extract.py to extract from multiple pdfs by providing the path as a command line argument or as an input. 
```
python Group_extract.py D:/PDFS
```

or

```
python Group_extract.py
```


The program usues pytesseract and pdf2image python libraries. \
Refer for pytesseract: https://github.com/madmaze/pytesseract  \
Refer for pdf2image  : https://github.com/Belval/pdf2image


To use this on windows, you'll have to install the tessaract file for windows from https://github.com/UB-Mannheim/tesseract/wiki. \
Set the path to your installation directory. By default it is : C:\Users\USER\AppData\Local\Tesseract-OCR \
Also uncomment this line from the code: \
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe' \


