import csv

#read file content
content = open("dialogue.txt", "r")

#create a CSV reader object
csvReader = csv.reader(content) #This object is kind of like a cursor. You can use the next() method to go to the next line,
                                #but you can also use it with a for loop to iterate through all the lines of the file.

header = next(csvReader)

#print(header)

humanIndex = header.index("human")
cozmoIndex = header.index("cozmo")

# dialogueList = []

#humanString
x = "I do not know how to do it"

for row in csvReader:
    human = row[humanIndex]
    cozmo = row[cozmoIndex]

    if x == human:
        print (cozmo)

    # dialogueList.append([human, cozmo])


# print(dialogueList)

