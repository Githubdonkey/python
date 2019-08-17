import csv
from pathlib import Path

data_folder1 = Path("C:\\Users\\tom\Desktop\\python\\my-python-project")

file_to_open = data_folder1 / "employee_birthday.csv"

with open(file_to_open) as csv_file:
	csv_reader = csv.DictReader(csv_file, delimiter=',')
	line_count = 0
	for row in csv_reader:
		if line_count == 0:
			print(f'Column names are {", ".join(row)}')
			line_count += 1
		print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
		line_count += 1
	print(f'Processed {line_count} lines.')