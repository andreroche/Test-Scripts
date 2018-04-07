from csv import reader, writer 

infile = open("data/iris.csv")
csvReader = reader(infile)

outfile = open("data/nicelyformatted.csv", "w")
csvWriter = writer(outfile)

headers = (["Petal Length", "Petal Width", "Sepal Length", "Sepal Width", "Flower Type"])
csvWriter.writerow(headers)

next(csvReader)

for row in csvReader:
    newRow = [row[0], row[1], row[2], row[3], row[4]]
    csvWriter.writerow(newRow)

    print (row)

    

infile.close()
outfile.close()

