# XML to Excel Data Converter

This Python script extracts data from an XML file and saves it in an Excel format. The script reads book data from an XML file (`compiler.xml`), shuffles the entries, and exports them into an Excel file (`200901008_Assignment_3.xlsx`) using the **OpenPyXL** library.

## Features

- **XML Parsing**: Extracts book details (ID, author, title, genre, price, publish date, description) from `compiler.xml`.
- **Data Shuffling**: Randomizes the order of book entries.
- **Excel Export**: Saves the extracted data into an Excel file with proper headers.

## How to Run

Ensure you have **Python** installed, and then install the required library:

```bash
pip install openpyxl


Place your compiler.xml file in the same directory and run the script:

```bash
python xml_to_excel.py


The output will be saved as 200901008_Assignment_3.xlsx.
