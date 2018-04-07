
print ('--Petal Length-- --Petal Width-- --Sepal length-- --Sepal Width--')

with open("data/iris.csv") as f:
    
    for line in f:
        print ("{:>10} {:>14} {:>16} {:>16}" .format(line.split(',')[0],line.split(',')[1],line.split(',')[2],line.split(',')[3]))



        