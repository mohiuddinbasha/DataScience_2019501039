library(class)
train = read.csv("D:/Second Year/DataScience_2019501039/Data Mining/Data Mining Assignments/DM Assignment4/sonar_train.csv", header = FALSE)
test = read.csv("D:/Second Year/DataScience_2019501039/Data Mining/Data Mining Assignments/DM Assignment4/sonar_test.csv", header = FALSE)
data = test[,1:2]
plot(data,pch=19,xlab=expression(data[1]),ylab=expression(data[2]))
fit = kmeans(data, 2)
fit
points(fit$centers,pch=19,col="blue",cex=2)
c(-1,1)
knnfit = knn(fit$centers,data,as.factor(c(-1,1)))
points(data,col=1+1*as.numeric(knnfit),pch=19)
out = test[,61]
1-sum(knnfit==out)/length(out)