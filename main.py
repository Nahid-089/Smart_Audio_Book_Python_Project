import pyttsx3
import PyPDF3
book = open('object_oriented_python_tutorial.pdf', 'rb')
pdfReader = PyPDF3.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
friend = pyttsx3.init()
for num in range(7, 12):
    page = pdfReader.getPage(num)
    text = page.extractText()
    friend.say(text)
    friend.runAndWait()