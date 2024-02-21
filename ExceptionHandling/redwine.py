import csv

file_path = "E:\PES\SEM2\Refer\ML\ML_Datasets-20230613T052137Z-001\ML_Datasets\Redwine.csv"

# Read the CSV data
with open(file_path, "r", newline="") as df:
    cr = csv.reader(df, delimiter=",")
    header = next(cr)  # Read and store the header row
    data = list(cr)    # Read the remaining data rows into a list

# Split the first line by semicolons and remove double quotes
header = header[0].replace('";"', ',').replace('"', '')

# Process the rest of the lines
csv_data = []
for row in data:
    csv_data.append(row[0].replace(';', ','))

# Write the processed data to a new CSV file
output_file = "redwine_processed.csv"
with open(output_file, "w", newline="") as f:
    f.write(header + "\n")  # Write the header
    for row in csv_data:
        f.write(row + "\n")  # Write each processed row

print(f"Processed CSV data has been saved to '{output_file}'")
