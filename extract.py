import pdfplumber
import re

def extract_invoice_data(filepath):
    with pdfplumber.open(filepath) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            print(text)

            order_number = re.search(r"#(\d+)", text)
            date = re.search(r"on\s+([A-Za-z]+\s+\d{1,2},\s+\d{4})", text)
            phone = re.search(r"\b(\d{10,15})\b", text)

            sku_qty_pairs = []
            for line in text.split('\n'):
                if " x " in line:
                    quantity = re.search(r"x\s*(\d+)", line)
                    if quantity:
                        quantity = quantity.group(1)
                        product = line.split(" x ")[0].rsplit('$',1)[0].strip()
                        sku_qty_pairs.append((product, quantity))

            return {
                "order": order_number.group(1) if order_number else "N/A",
                "date": date.group(1) if date else "N/A",
                "phone": phone.group(1) if phone else "N/A",
                "items": sku_qty_pairs
            }

