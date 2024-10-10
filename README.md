
# Project Title

Face and text detection from newspaper images

![PyPI version](https://img.shields.io/pypi/v/pillow?label=Pillow)
![opencv](https://img.shields.io/pypi/v/opencv-python?label=opencv)
![pytesseract](https://img.shields.io/pypi/v/pytesseract?label=pytesseract)

## Task

When a search word is entered, the program will look for that word in the newspaper pages. If the word is found in a particular page, all the faces detected in that page is returned as a contact sheet.
## Synopsis

* A zip file of images(e.g. newspaper) is taken as input. Then they're processed using the pillow library.
* pytesseract is used for optical character recognition from the images.
* Opencv is used to detect faces in the images.
* A contact sheet is created using the pillow library to accumulate all the faces detected on a particular page.



## Usage/Examples

If the search word is 'Cavillrine', the program will extract all the images present in the page where that word has been mentioned. 

## Screenshots
![output](https://github.com/newaz-aa/Face-and-Text-Detection-using-OpenCV-Tesseract/blob/master/output.png)

![sample page](https://github.com/newaz-aa/Face-and-Text-Detection-using-OpenCV-Tesseract/blob/master/a-1.png)

