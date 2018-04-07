# André Roche  - Fisher's Iris Data Set. 11-Mar-2018. Info available at https://en.wikipedia.org/wiki/Iris_flower_data_set

# Constants or variable constants learned on chapter 2 (sections 2.1.1 - 2.1.4) pages 28-33 in 'Python for Everyone', 2nd Edition, Wiley.
PetalL = '--Petal Length--'    # Assign Constant Variable (or just a constant!). PetalL is assigned the value or string '--Petal length--' 
PetalW = '--Petal Width--'     # Same as above but for PetalW.
SepalL = '--Sepal Length--'    # Same as above but for SepalL.
SepalW = '--Sepal Width--'     # Same as above but for SepalW.


# Format method learned from course notes and Learning Python 5th Edition, O'Riley, Pages 222-225. 
print('{0} {1} {2} {3}'.format(PetalL,PetalW, SepalL, SepalW)) # Print to screen constants 0-3 (or 1-4) using the .format method to specify the format.

# Please create a file 'iris.csv' in a folder 'data' in the working directory if not already done so in order for the Input/Output to function.                                                            
with open("data/iris.csv") as f: # The 'with' statement opens the file with the given name, sets outfile and closes the file when the statement is finished.
    for line in f: # The for loop will read each line in the file (the infile) and next line will instruct program to print data to screen.
        print ("{:>10} {:>14} {:>16} {:>16}" .format(line.split(',')[0],line.split(',')[1],line.split(',')[2],line.split(',')[3])) # Right space justifications for table format and format command for data display.


# The next part of the program reads from the existing file and writes to a new CSV file with better formatting- CSV module learned from pages 399-401 in 'Python for Everyone', 2nd edition, published by Wiley.

from csv import reader, writer # Create a CSV reader and writer using the reader and writer function.

infile = open("data/iris.csv") # Open the file in working directory/data/ called 'iris.csv'.
csvReader = reader(infile) # Create a CSV reader using the reader function. 

outfile = open("data/nicelyformatted.csv", "w") # Create a new file using the open function.
csvWriter = writer(outfile) # Create a CSV writer using the writer function.

headers = (["Petal Length", "Petal Width", "Sepal Length", "Sepal Width"]) # This line adds column headers to the new CSV file.
csvWriter.writerow(headers) # Add/write a row of headers using the writerow method - these are the strings passed in the line above. 

next(csvReader) # Skip the row of column headers in the reader.

for row in csvReader: # For loop to read /iterate through the data in the reader object. 

    newRow = [row[0], row[1], row[2], row[3]] # defining the columns and order that will be output to the new file(I could filter this if required for some reason).
    csvWriter.writerow(newRow) # Add/write new rows using the write method in the format stated in the line above.


infile.close() # Close the input file / the file that is being read.
outfile.close() # Close the newly created file / the file that is being written to. 