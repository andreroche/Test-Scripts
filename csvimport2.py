from csv import reader

infile = open("data/iris.csv")
csvReader = reader(infile)



for row in csvReader:
    print (row)

infile.close()

