from pdf2docx import Converter
from docx2pdf import convert 
chos=input("Enter 'pdf' if you want to convert a pdf to word \nEnter 'word' if you want to convert word to pdf : ")
inpfile=input("Enter the File Location of the pdf file to convert: ")
if chos == "pdf":
    newdoc="converted.docx"
    magic= Converter(inpfile)
    magic.convert(newdoc)
    magic.close()
    print("File is converted successfully")
elif chos=="word":
    convert(inpfile,"convertedword.pdf")
    print("File successfully converted")

print("Thanks for using our convertor")