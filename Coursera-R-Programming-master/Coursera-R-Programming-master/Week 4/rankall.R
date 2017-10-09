rankall<-function(outcome,num="best"){
  
  #read data from the file
  data <- read.csv('outcome-of-care-measures.csv', colClasses = "character")
  
  #get all the unique states, and sort them
  state <- sort(unique(data$State))
  
  #create an empty dataframe for hospital name based on the length=number of states
  hospital <- rep("", length(state))
  
  
  for (i in 1:length(state)) {
    #get data for each state
    statedata<- data[data$State==state[i],]
                     
    if (outcome == 'heart attack') {
      ddata <- as.numeric(statedata[,11])
    } else if (outcome == 'heart failure') {
      ddata <- as.numeric(statedata[,17])
    } else if (outcome == 'pneumonia') {
      ddata <- as.numeric(statedata[,23])
    } else {
      stop("Invalid Outcome")
    }
    
    ranked_data <- rank(ddata, na.last=NA)
    
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
    
    if (is.na(row)) {
      hospital[i] <- NA
    } else {
      hospital[i] <- statedata$Hospital.Name[order(ddata, statedata$Hospital.Name)[row]]
    }
    
  }
  
  return(data.frame(hospital=hospital, state=state))
  
  
}

#r <- rankall("heart attack", 4)
#as.character(subset(r, state == "HI")$hospital)