add2 <- function(x,y){
  x+y
}

#in the console -> add2(3,5)

#takes a vector as an input
#outputs value above 10
above10 <- function(x){
  use <- x>10
  x[use]
} 

#x <- c(1,2,11)
#above10(x)

#outputs value above n
aboveN <- function(x,n){
  use <- x>n
  x[use]
}

# x <-1:20
#aboveN(x,3)
#if n is not specified, it will give us error. 
#but if we use default value n=10, then if 
#nothing is specified it will automatically use n =10;


#y is a dataframe or matrix
column_mean <- function(y){
  nc <-ncol(y) # returns number of col
  means <- numeric(nc) #initialize a vector that will contain the mean of each coloumn
  for(i in 1:nc){
    means[i] <-mean(y[,i])
  }
}

#same function, but now it handles NA
column_mean <- function(y, removeNA = TRUE){
  nc <-ncol(y) # returns number of col
  means <- numeric(nc) #initialize a vector that will contain the mean of each coloumn
  for(i in 1:nc){
    means[i] <-mean(y[,i], na.rm = removeNA) #mean has a default parameter to ignore remove
  }
}
#column_mean(y) #automatically remove NA
#column_mean(y,false) #doesnt remove NA
  