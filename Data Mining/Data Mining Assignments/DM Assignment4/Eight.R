library(class)
train = read.csv("D:/Second Year/DataScience_2019501039/Data Mining/Data Mining Assignments/DM Assignment4/sonar_train.csv", header = FALSE)
test = read.csv("D:/Second Year/DataScience_2019501039/Data Mining/Data Mining Assignments/DM Assignment4/sonar_test.csv", header = FALSE)
K = test[,1:2]
plot(K,pch=19,xlab=expression(K[1]), ylab=expression(K[2]))
kmeanfit = kmeans(K,2)
points(kmeanfit$centers,pch=19,col="red",cex=2)
knnfit = knn(kmeanfit$centers,K,as.factor(c(-1,1)))
points(K,col=1+1*as.numeric(knnfit),pch=19)
var = test[,61]
1-sum(knnfit==var)/length(var)

#8b
#We can choose any of value as K but if we choose the K as odd value then we get ambiguity and the error may increase. 
#So we should have the odd number of clusters for even number of class in order to reduce the
#ambiguity in making the decision for the clusters