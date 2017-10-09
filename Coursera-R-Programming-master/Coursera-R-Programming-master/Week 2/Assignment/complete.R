complete <- function(directory, id=1:332){
  files_list <- list.files(directory, full.names = TRUE)
  
  all_data <- data.frame()
  
  for(i in id){
    #since count complete cases on each files alone, we can read file one by one
    no_na_data <- complete.cases(read.csv(files_list[i]))
    #count all the complete values
    count <- sum(no_na_data)
    #dataframe for each file
    temp <- data.frame(i, count)
    #add up the counts of all the files
    all_data <- rbind (all_data, temp)
  }
  colnames(all_data) <- c("id", "nobs")
  all_data
}

#sample test cases
# complete("specdata", 1)
# complete("specdata", c(2, 4, 8, 10, 12))
# complete("specdata", 30:25)
