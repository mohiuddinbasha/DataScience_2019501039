library(dplyr)
input <- read.csv('C:/Users/BASHA/Downloads/Compressed/Final exam/BSE_Sensex_Index.csv',header = TRUE)
close <- input[['Close']]
fun <- function(close){
  y <- numeric()
  for (i in 1:(length(close)-1)){
    y <- c(y, (close[i]-close[i+1])/close[i+1])
  }
  y
}
v <- fun(close)
lastvalue <- (v[length(v)]+v[length(v)-1]+v[length(v)-2])/3
v <- append(v,lastvalue)
mean <- mean(v)
std <- sd(v)
fun <- function(v){
  z <- numeric()
  for (i in 1:length(v)){
    z <- c(z, (v[i]-mean)/std)
  }
  z
}
z <- fun(v)
input$sdclose = z
output <- filter(input, sdclose <-3 & sdclose > 3)
head(output)
output[,1]