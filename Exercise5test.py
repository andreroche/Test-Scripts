


# The next part of the program reads from the existing file and writes to a new CSV file - CSV library learned from pages 399-401 in 'Python for Everyone', 2nd edition, published by Wiley.

from csv import reader, writer 

infile = open("data/iris.csv")
csvReader = reader(infile)

outfile = open("data/nicelyformatted.csv", "w")
csvWriter = writer(outfile)

headers = (["Petal Length", "Petal Width", "Sepal Length", "Sepal Width"])
csvWriter.writerow(headers)

next(csvReader)

for row in csvReader:

    newRow = [row[0], row[1], row[2], row[3]]
    csvWriter.writerow(newRow)
    

infile.close()
outfile.close()



import csv
with open("data/nicelyformatted.csv", newline='') as f:
    reader = csv.reader(f, delimiter = ',', quoting = csv.QUOTE_NONE)
    for row in reader:
        print(row)
