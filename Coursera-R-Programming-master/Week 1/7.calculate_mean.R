data <- read.csv('hw1_data.csv')
row <- data[1]  #get the first row
nna <- is.na(row) #identify which of the values are NA
y <- row[!nna] #exclude NA
mean(y) #take mean
