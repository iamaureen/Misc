
# Open the file with read only permit
f = open('dialogue_v2.txt', "r")
# use readlines to read all lines in the file
# The variable "lines" is a list containing all lines in the file
#lines = f.readlines()
#print(lines)

#removes \n from the end
#lines = [line.rstrip('\n') for line in open('dialogue.txt', "r")]
#print(lines)

dictionary = {'start' : 'Hey All'}

#created dictionary from the textfile
while True:
    # read line
    line = f.readline()

    # check if line is not empty
    if not line:
        break

    #strip out the \n at the end
    l1=line.rstrip('\n')

    #split by ":"
    l2=l1.split(":")
    #print(l2) #print(l2[0])

    if l2[0] == 'human':
        key = l2[1]
    else:
        pair = l2[1];
        dictionary[key] = pair

#print(dictionary)

#loop through dictionary
for k, v in dictionary.items():
        print(k, v)
# close the file after reading the lines.
f.close()