source("complete.R")
corr <- function(directory, threshold = 0){
  
  #read all the files from the directory
  files_list <- list.files(directory, full.names = TRUE)
  
  #read all the files, count na values
  complete_data <- complete(directory)  
  
  #get those files, which has greater nobs than the threshold, discard rest
  data <- complete_data[complete_data$nobs > threshold, ]
  
  corr_result <- numeric(0)
  
  #for each id that passed threshold
  for(id in data$id){
    #read those files by id
    file <- read.csv(files_list[id])
    
    #check for valid rows, which is not na
    rows <- !is.na(file$sulfate) & !is.na(file$nitrate)
    
    #create dataframe based on that rows
    subset_valid_rows <- file[rows,]
    
    #calculate correlation
    corr_result <- c(corr_result, cor(subset_valid_rows$sulfate, subset_valid_rows$nitrate))
  }
  
  corr_result
}