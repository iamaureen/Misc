data <- read.csv('hw1_data.csv')
row <- data[1]  #get the first row
nna <- is.na(row) #identify the values NA
sum(nna) #count number of NA
