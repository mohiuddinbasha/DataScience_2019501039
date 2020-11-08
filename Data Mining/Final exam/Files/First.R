input <- read.csv("C:/Users/BASHA/Downloads/Compressed/Final exam/BSE_Sensex_Index.csv")
yOpen <- numeric()
yHigh <- numeric()
yLow <- numeric()
yClose <- numeric()
yVolume <- numeric()
yAdj.Close <- numeric()
  
for (i in 1:(length(input[,1])-1)){
  yOpen <- c(yOpen, ((input[,2])[i]-(input[,2])[i+1])/(input[,2])[i+1])
  yHigh <- c(yHigh, ((input[,3])[i]-(input[,3])[i+1])/(input[,3])[i+1])
  yLow <- c(yLow, ((input[,4])[i]-(input[,4])[i+1])/(input[,4])[i+1])
  yClose <- c(yClose, ((input[,5])[i]-(input[,5])[i+1])/(input[,5])[i+1])
  yVolume <- c(yVolume, ((input[,6])[i]-(input[,6])[i+1])/(input[,6])[i+1])
  yAdj.Close <- c(yAdj.Close, ((input[,7])[i]-(input[,7])[i+1])/(input[,7])[i+1])
}
yOpen <- append(yOpen,(yOpen[15446]+yOpen[15445]+yOpen[15444])/3)
yHigh <- append(yHigh,(yHigh[15446]+yHigh[15445]+yHigh[15444])/3)
yLow <- append(yLow,(yLow[15446]+yLow[15445]+yLow[15444])/3)
yClose <- append(yClose,(yClose[15446]+yClose[15445]+yClose[15444])/3)
yVolume <- append(yVolume,(yVolume[15446]+yVolume[15445]+yVolume[15444])/3)
yAdj.Close <- append(yAdj.Close,(yAdj.Close[15446]+yAdj.Close[15445]+yAdj.Close[15444])/3)

input$sdOpen = yOpen
input$sdHigh = yHigh
input$sdLow = yLow
input$sdClose = yClose
input$sdVolume = yVolume
input$sdAdj.Close = yAdj.Close

library(dplyr)
sample1 <- sample_n(input, 1000, replace=TRUE)
sample2 <- sample_n(input, 3000, replace=TRUE)

listVar <- list(open = sample1$sdOpen, high = sample1$sdHigh, low = sample1$sdLow, close = sample1$sdClose, volume = sample1$sdVolume, adj.close = sample1$sdAdj.Close)
mns1 <- sapply(listVar, mean, na.rm = T)
mxs1 <- sapply(listVar, max, na.rm = T)
qns1 <- sapply(listVar, quantile,probs=0.25, na.rm = T)

listVar1 <- list(open = sample2$sdOpen, high = sample2$sdHigh, low = sample2$sdLow, close = sample2$sdClose, volume = sample2$sdVolume, adj.close = sample2$sdAdj.Close)
mns2 <- sapply(listVar1, mean, na.rm = T)
mxs2 <- sapply(listVar1, max, na.rm = T)
qns2 <- sapply(listVar1, quantile,probs=0.25, na.rm = T)

listIn <- list(open = input$sdOpen, high = input$sdHigh, low = input$sdLow, close = input$sdClose, volume = input$sdVolume, adj.close = input$sdAdj.Close)
mnin <- sapply(listIn, mean, na.rm = T)
mxin <- sapply(listIn, max, na.rm = T)
qnin <- sapply(listIn, quantile,probs=0.25, na.rm = T)
mnin
mxin
qnin


#Mean difference
abs(mns1-mnin)
#Max difference
abs(mxs1-mxin)
#Quantile difference
abs(qns1-mxin)

#Mean difference
abs(mns2-mnin)
#Max difference
abs(mxs2-mxin)
#Quantile difference
abs(qns2-qnin)

boxplot(input$Open, input$High, input$Low, input$Close,
        main = "Boxplot",
        at = c(1,2,4,5),
        names = c("Open","High","Low","Close"),
        las = 2,
        col = c("blue","orange"),
        border = "black",
        horizontal = TRUE,
        notch = TRUE
      )

hist(input$Close, ylim=c(0,2000), col="red",main="BSE Sensex Close",xlab="Close Values")
