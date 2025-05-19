import pdfplumber
import re

def extract_invoice_data(filepath):
    with pdfplumber.open(filepath) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            print(text)  # Optional: remove or toggle for debugging

            # Extract core fields
            order_number = re.search(r"#(\d+)", text)
            date = re.search(r"on\s+([A-Za-z]+\s+\d{1,2},\s+\d{4})", text)
            phone = re.search(r"\b(\d{10,15})\b", text)
            email = re.search(r"\b\S+@\S+\.\S+\b", text)

            # Address extraction
            lines = text.split("\n")
            address_block = []
            for i, line in enumerate(lines):
                if "Shipping Address" in line:
                    address_block = lines[i+1:i+4]
                    break

            # Handle edge cases safely
            name_line = address_block[0] if len(address_block) > 0 else "N/A"
            address_line1 = address_block[1] if len(address_block) > 1 else "N/A"
            city_country = address_block[2] if len(address_block) > 2 else "N/A"

            # Clean duplicated name
            name_parts = name_line.split()
            name = " ".join(name_parts[:2]) if name_parts else "N/A"

            # Match address details (city, state, zip, country)
            match_address = re.search(r"^(.*?),\s+([A-Za-z]+)\s+(\d{5}),\s+([A-Za-z\s]+)", city_country)
            if match_address:
                city = match_address.group(1).strip()
                state = match_address.group(2).strip()
                zipCode = match_address.group(3).strip()
                country = match_address.group(4).strip()
            else:
                city = state = zipCode = country = "N/A"

            # Product parsing
            sku_qty_pairs = []
            for line in text.split('\n'):
                if " x " in line:
                    quantity = re.search(r"x\s*(\d+)", line)
                    if quantity:
                        quantity = quantity.group(1)
                        product = line.split(" x ")[0].rsplit('$', 1)[0].strip()
                        sku_qty_pairs.append((product, quantity))

            #  debugging output
            # print({
            #     "order": order_number.group(1) if order_number else "N/A",
            #     "date": date.group(1) if date else "N/A",
            #     "phone": phone.group(1) if phone else "N/A",
            #     "email": email.group(0) if email else "N/A",
            #     "items": sku_qty_pairs,
            #     "address": address_block,
            #     "name": name,
            #     "Address Line 1": address_line1,
            #     "city": city,
            #     "zip Code": zipCode,
            #     "state": state,
            #     "country": country
            # })

            return {
                "order": order_number.group(1) if order_number else "N/A",
                "date": date.group(1) if date else "N/A",
                "phone": phone.group(1) if phone else "N/A",
                "email": email.group(0) if email else "N/A",
                "items": sku_qty_pairs,
                "address": address_block,
                "name": name,
                "Address Line 1": address_line1,
                "city": city,
                "zip Code": zipCode,
                "state": state,
                "country": country
            }

# TODO: Process all PDF pages if invoices span multiple pages
# TODO: Consider wrapping logs in a debug flag for cleaner production use

