# Invoice PDF extractor

This project reads invoice PDFs and extracts key information such as:
- Order number
- Customer details (name, phone, email)
- Product names, quantities and SKUs(if available)
- Address (city, state, zip, country)

# Description

This tool uses Python, 'pdfplumber', and 're'(regex) parse strucutred data from pdf invoice
The extracted data is then printed and saved into a clean structured CSV format having columns of sections mentioned above.

# Features
- Extracts data from WIX(website builder) structured invoice pdfs
- Detects name, email, phone, and full address block
- parses product name and quantity
- writes results to a csv file ("filling.csv")
- handles missing data gracefully
- Uses regex for dynamic pattern matching

# How to run it

1- clone the repo using the link
2- activate venv by -> source venv/bin/activate
3- install dependencies -> pip install -r requirements.txt
4- run the extractor -> python3 csvTester.py

NOTE: inside csvTester.py change testorder.pdf to any file you wish including its path

# Folders Structure
invoice-extractor/
.
├── csvTester.py
├── extract.py
├── filling.csv
├── main.py
├── __pycache__
├── README.md
├── requirements.txt
├── testorder.pdf
└── venv

