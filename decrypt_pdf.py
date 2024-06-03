from adjectives import adjective_dictionary
from animals import animal_list
from time import time
from PyPDF2 import PdfFileReader


#  💻 You must edit the code below to solve the puzzle 💻 #


start_time = time()                         # stores the current time to calculate total time to decrypt

file = PdfFileReader('encrypted_pdf.pdf')   # opens the PDF 
file.decrypt('password')                    # returns a 0 or 1, if the password was correct

    

# calculates total time to decrypt the pdf
end_time = time()
total_time_elapsed = round(end_time - start_time,2)
print('-'*50)
print(f'Total time to decrypt: {total_time_elapsed} seconds')