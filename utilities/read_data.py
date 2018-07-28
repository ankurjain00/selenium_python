import csv

data = {}

def getCSVData(csvFile, *args):
	list = []
	with open(csvFile, "r") as infile:
		reader = csv.DictReader(infile)

		for row in reader:
			for column in args:
				data[row[column]] = row
				list.append(row[column])
	return list

