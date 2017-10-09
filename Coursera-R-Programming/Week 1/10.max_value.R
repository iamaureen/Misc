data <- read.csv('hw1_data.csv')

sub <- subset(data, Month==5, select=c(Ozone))
max(sub,na.rm=TRUE)