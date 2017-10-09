data <- read.csv('hw1_data.csv')
sub <- subset(data,select=c(Ozone,Temp,Solar.R)) # subset of data based on colm name
sub1 <- subset(sub, Ozone > 31, select=c(Solar.R)) # subset based on condition 1: Ozone>31
sub2 <- subset(sub1, Temp>90, select = c(Solar.R)) # subset based on condition 2: Temp > 90
# print(sub2)
mean(sub2$Solar.R)  #calculate mean
