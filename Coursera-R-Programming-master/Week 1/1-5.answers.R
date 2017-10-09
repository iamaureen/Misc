#loading data file
data <- read.csv('hw1_data.csv')


#In the dataset provided for this Quiz, what are the column names of the dataset?
colnames(data)

#Extract the first 2 rows of the data frame and print them to the console.
data[1:2, ]
#or
head(data,2)

#How many observations (i.e. rows) are in this data frame?
nrow(data)

#Extract the last 2 rows of the data frame and print them to the console.
data[152:153, ]
#or
tail(data,2)

#What is the value of Ozone in the 47th row?
Oz <- data[1]
Oz
data$Oz[47]