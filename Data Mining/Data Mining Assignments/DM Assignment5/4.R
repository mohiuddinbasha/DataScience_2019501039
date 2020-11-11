library(class)
train = read.csv("D:/Second Year/DataScience_2019501039/Data Mining/Data Mining Assignments/DM Assignment4/sonar_train.csv", header = FALSE)
test = read.csv("D:/Second Year/DataScience_2019501039/Data Mining/Data Mining Assignments/DM Assignment4/sonar_test.csv", header = FALSE)

k = test[,1:60]
kmeanfit = kmeans(k,2)
points(kmeanfit$centers,pch=19,col="red",cex=2)
knnfit = knn(kmeanfit$centers,k,as.factor(c(-1,1)))
points(kAll,col=1+1*as.numeric(knnfit),pch=19)
out = test[,61]
1-sum(knnfit==out)/length(out)