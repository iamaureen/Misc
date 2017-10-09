rankhospital <- function(state, outcome, num='best'){
  
  #read data from the file
  data <- read.csv('outcome-of-care-measures.csv', colClasses = "character")
  
  #check if state is valid or not
  if(!state %in% data$State){
    stop('Invalid State')
  }
  
  #load data for the specific state
  data<-data[data$State==state,]
  
  #load data specific to the outcome
  if(outcome=='heart attack'){
    ddata <-as.numeric(data[,11])
  }else if(outcome=='heart failure'){
    ddata <-as.numeric(data[,17])
  }else if(outcome=='pneumonia'){
    ddata <-as.numeric(data[,23])
  }else{
    stop('Invalid Outcome')
  }
  
  #rank-- Returns the sample ranks of the values in a vector.
  ranked_data <-rank(ddata,na.last = NA) #NA values are removed
  
  
  if(is.numeric(num)){
    row <- num
  }
  else if(num=='best'){
    row<-1
  }else if(num=='worst'){
    row<-length(ranked_data) #select the last row
  }
  else{
    return(NA)
  }
  
  result<-data$Hospital.Name[order(ddata, data$Hospital.Name)[row]]
  return(result)
  
}