library(rpart)
library(rpart.plot)
data = read.csv("C:/Users/BASHA/Downloads/Compressed/Final exam/lenses.data.csv", header = FALSE, col.names = c("index", "age", "spectacle_prescription", "astigmatic", "tear_production_rate", "Class"))
data$index <- NULL
y<-as.factor(data[,5])
x<-data[,1:4]
model1<-rpart(y~.,x, parms = list(split = 'information'),ontrol=rpart.control(minsplit=0,minbucket=0,cp=-1, maxcompete=0, maxsurrogate=0, usesurrogate=0, xval=0,maxdepth=5))
rpart.plot(model1)
gain <- sum(y==predict(model1,x,type="class"))/length(y)
gain #1
error <- 1-sum(y==predict(model1,x,type="class"))/length(y)
error #0