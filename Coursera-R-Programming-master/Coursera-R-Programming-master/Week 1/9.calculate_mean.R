data <- read.csv('hw1_data.csv')

sub <- subset(data, Month==6, select=Temp) #select rows based on Month==6
mean(sub$Temp)