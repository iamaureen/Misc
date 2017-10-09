best <- function(state, outcome){
  
  data <- read.csv('outcome-of-care-measures.csv', colClasses = "character")
  #create small subset of data with the required values
  #colNum from conames(data)->lists the colname with their index
  sub_data <-as.data.frame(cbind(data[,2], #hospital
                                 data[,7], #state
                                 data[,11], #heart attack
                                 data[,17], #heart failure
                                 data[,23]), #pneumonia
                           stringsAsFactors = FALSE)
                           
  
  #assign col names to the new sub data
  colnames(sub_data) <- c("hospital", "state", "heart attack", "heart failure", "pneumonia")
  
  #check that state and outcome are valid
  if(!state %in% sub_data[, "state"]){
    stop('Invalid State')
  }
  else if(!outcome %in% c("heart attack", "heart failure", "pneumonia")){
    stop('Invalid Outcome')
  }
  
  st <- which(sub_data[,'state']==state)
  d1 <- sub_data[st, ]    # extracting data for the called state
  d2 <- as.numeric(d1[,eval(outcome)]) #extracting data for the given outcomes
  min_val <- min(d2, na.rm = TRUE) #get the minimum value
  d3 <- d1[,'hospital'][which(d2==min_val)] #get the hospital name based on min_val
  result <- d3[order(d3)] #if tie, it would return the hospital name which appears first, thats why we are using order method
  
  return(result)
  
}