import csv
import json

def extract_default_url(json_str):
    try:
        data = json.loads(json_str)
        for variant in data["variants"]:
            if variant["identifier"] == "default":
                return variant["url"]
    except json.JSONDecodeError:
        return None
    return None

# Open the source CSV file and a new CSV file for writing
with open('SEC_23-10-2023.csv', 'r', newline='', encoding='utf-8') as infile, open('output.csv', 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile, delimiter=';')
    writer = csv.writer(outfile, delimiter=';')

    # Write the header row to the output file
    writer.writerow(["sku", "brand", "image", "title", "description", "price", "category"])

    # Iterate over each row in the source file
    for row in reader:
        # Extract image URL
        url = extract_default_url(row[2])

        # Write data to new file
        if url:
            writer.writerow([row[0], row[1], url, row[3], row[4], row[9], row[10]])

print("Processing completed!")