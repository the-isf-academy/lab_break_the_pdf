from adjectives import adjective_dictionary
from animals import animal_list
from PyPDF2 import PdfFileReader


#  💻 You must edit the code below to solve the puzzle 💻 #


file = PdfFileReader('encrypted_pdf.pdf')   

file.decrypt('password')   # returns 0 or 1

