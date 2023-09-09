import json

FILE_PATH = "YCombTest/combined_companies_data.json"

# Load JSON data from the file
with open(FILE_PATH, "r") as file:
    data_array = json.load(file)

company_names = []
for data in data_array:
    company_name = data.get("name")
    company_names.append(company_name)

# Print the list of company names
print("List of company names:")
for i, name in enumerate(company_names, 1):
    print(f"{i}. {name}")

# Write company names to a new JSON file
output_file = "final_company_list.json"
with open(output_file, "w") as outfile:
    json.dump(company_names, outfile)

print(f"Company names written to '{output_file}'.")