library(rpart)

train = read.csv("D:/Second Year/DataScience_2019501039/Data Mining/Data Mining Assignments/DM Assignment4/sonar_train.csv", header = FALSE)
test = read.csv("D:/Second Year/DataScience_2019501039/Data Mining/Data Mining Assignments/DM Assignment4/sonar_test.csv", header = FALSE)
x = train[,1:60]
y = as.factor(train[,61])
x_test = test[,1:60]
y_test = as.factor(test[,61])
error = matrix(data=NA,nrow=6,ncol=3)
for(var in 1:6) {
  error[var,1] = var
  fit<-rpart(y~.,x,control = rpart.control(minsplit = 0,minbucket = 0,cp = -1,maxcompete = 0,xval = 0,maxdepth = var))
  error[var,2] = sum(y!=predict(fit,x,type="class"))/length(y)
  error[var,3] = sum(y_test!=predict(fit,x_test,type="class"))/length(y_test)
}
value = error[which.min(error[,3]),3]
round(value,3)
depth = error[which.min(error[,3]),1]
depth
