andy <- read.csv("Andy.csv")
head(andy) #returns the first part of the vector/matrix/table (here: andy)

#how many rows are there in Day Colmn
length(andy$Day)

#find the dimension of the dataframe
dim(andy)

#gives the name of the column
names(andy)

#starting weight for andy
andy[1, "Weight"]

#ending weight for andy
andy[30, "Weight"]

#subset of the 'Weight' column where the data where 'Day' is equal to 30.
andy[which(andy$Day==30), "Weight"]
#or, similar thing using subset function
subset(andy$Weight, andy$Day==30)

#lists all the files that are in this folder
files <- list.files(getwd())
files[7]
#read particular file based on the index 
head(read.csv(files[7])) #reads data from steve.csv

#adding two csv files/two source of data (here: andy and david)
andy_david <- rbind(andy, read.csv(files[2]))
head(andy_david)
tail(andy_david)

#create a subset of the data frame that shows us just the 25th day for 
#Andy and David.
day_25 <- andy_david[which(andy_david$Day == 25), ]
day_25

#calculates the median for all weight values
median(andy_david$Weight)
#if any of the values where NA, then the answer would have been NA
#so in that case, first NA will have to be removed
#median(dat$Weight, na.rm=TRUE)
























