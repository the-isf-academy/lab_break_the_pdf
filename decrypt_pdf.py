from adjectives import adjective_dictionary
from animals import animal_list
from time import time
from PyPDF2 import PdfFileReader


#  💻 You must edit the code below to solve the puzzle 💻 #


file = PdfFileReader('encrypted_pdf.pdf')   

if file.decrypt('password') == 1:                
    print('password successful')
else:
    print('password unsuccesful')
