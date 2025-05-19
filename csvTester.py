import csv
from extract import extract_invoice_data

# Extract data from the PDF
data = extract_invoice_data("testorder.pdf")

# Write the extracted data to a CSV file
with open('filling.csv', 'w', newline='') as csvfile:
    fieldnames = [
        'Order number', 'Date', 'Phone Number', 'Email',
        'SKU', 'Quantity',
        'Customer Name', 'Address Line 1', 'City',
        'Zip Code', 'State', 'Country'
    ]

    writer = csv.DictWriter(
        csvfile,
        fieldnames=fieldnames,
        restval='Unavailable',
        extrasaction='ignore'
    )

    writer.writeheader()

    # Write one row per product item
    for sku, quantity in data["items"]:
        writer.writerow({
            'Order number': data["order"],
            'Date': data["date"],
            'Phone Number': data["phone"],
            'Email': data["email"],
            'SKU': sku,
            'Quantity': quantity,
            'Customer Name': data["name"],
            'Address Line 1': data["Address Line 1"],
            'City': data["city"],
            'Zip Code': data["zip Code"],
            'State': data["state"],
            'Country': data["country"]
        })

    # Optional visual separator
    writer.writerow({'Order number': '------- End of Order -------'})

# Print structured data to console for verification
print(data)

