pollutantmean <- function(directory, pollutant, id = 1:332){
  
  files_list <- list.files(directory, full.names = TRUE)
  #length(files_list)
  
  all_data <- data.frame()
  
  for(i in id){
    all_data <- rbind(all_data, read.csv(files_list[i]))
  }
  
  mean_value <- mean(all_data[,pollutant], na.rm = TRUE)
  #round 3 digits after decimal point
  ans <- round(mean_value, 3)
  ans
}

#sample test cases
#pollutantmean("specdata", "sulfate", 1:10)  -> 4.064
#pollutantmean("specdata", "nitrate", 70:72)  -> 1.706
#pollutantmean("specdata", "nitrate", 23)  -> 1.281




