import csv
from extract import extract_invoice_data

# Extract data from the PDF
data = extract_invoice_data("testorder.pdf")

# Write the extracted data to CSV
with open('filling.csv', 'w', newline='') as csvfile:
    fieldnames = ['Order number', 'Date', 'Phone Number', 'SKU', 'Quantity']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, restval='Unavailable', extrasaction='ignore')

    writer.writeheader()

    for sku, quantity in data["items"]:
        writer.writerow({
            'Order number': data["order"],
            'Date': data["date"],
            'Phone Number': data["phone"],
            'SKU': sku,
            'Quantity': quantity
        })

    # Add a visual break between orders
    writer.writerow({'Order number': '------- End of Order -------'})

# Optional: Print the data for verification
print(data)

# TODO: create and match the new field that will be extracted from the invoice from extract.py
