# Python-Project---pillow-tesseract-opencv
General concept: Face Detection using opencv and text detection using tesseract -- from images (eg.newspaper)
Description:
  1. a zip file of images(e.g. newspaper) is taken as input. then they're processed using pillow.
  2. pytesseract is used for optical character recognition from the images.
  3. opencv is used to detect faces in the images.
  4. a contact sheet is created using pillow to accummulate all the faces detected in a particular page.
  5. Finally when a search word is entered, the program will look for that word in the newspaper pages. If the word is found in a particular page, all the faces detected      in that page is returned as a contact sheet.
  
 
