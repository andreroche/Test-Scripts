from csv import reader, writer 

infile = open("data/iris.csv")
csvReader = reader(infile)

outfile = open("data/nicelyformatted.csv", "w")
csvWriter = writer(outfile)

headers = (["Petal Length", "Petal Width", "Sepal Length", "Sepal Width", "Flower Type"])
csvWriter.writerow(headers)

next(csvReader)

for row in csvReader:
    print (row)

infile.close()
outfile.close()

