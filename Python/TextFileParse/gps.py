import csv

#read file content
content = open("gps.txt", "r")

#create a CSV reader object
csvReader = csv.reader(content) #This object is kind of like a cursor. You can use the next() method to go to the next line,
                                #but you can also use it with a for loop to iterate through all the lines of the file.

header = next(csvReader)

#print(header)

latIndex = header.index("lat")
lonIndex = header.index("long")

# dialogueList = []
# dialogueList.append([])

coordList = []

for row in csvReader:
    lat = row[latIndex]
    lon = row[lonIndex]
    coordList.append([lat,lon])

# Print the coordinate list
print (coordList)