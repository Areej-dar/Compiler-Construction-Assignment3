import xml.etree.ElementTree as ET
import openpyxl
import random

# start by parse the xml file using ElementTree
tree = ET.parse("compiler.xml")
root = tree.getroot()

book_data_list = []

#now iterate through each book element and extract relevant information
for book in root.findall("book"):
    book_data = {}
    book_data["id"] = book.get("id")
    book_data["author"] = book.find("author").text
    book_data["title"] = book.find("title").text
    book_data["genre"] = book.find("genre").text
    book_data["price"] = book.find("price").text
    book_data["publish_date"] = book.find("publish_date").text
    book_data["description"] = book.find("description").text
    book_data_list.append(book_data)

#this is o shuffle the book data so that the order is random
random.shuffle(book_data_list)

# create a new excel workbook and worksheet
workbook = openpyxl.Workbook()
worksheet = workbook.active

#this is to add a header row to the worksheet
worksheet.append(["Book_Id", "Author_Name", "Title", "Genre", "Price", "Publish_date", "Description"])

#this is to add the book data to the worksheet
for book_data in book_data_list:
    worksheet.append([book_data["id"], book_data["author"], book_data["title"], book_data["genre"], book_data["price"], book_data["publish_date"], book_data["description"]])

# save the workbook to a file and generate excel
workbook.save("200901008_Assignment_3.xlsx")
