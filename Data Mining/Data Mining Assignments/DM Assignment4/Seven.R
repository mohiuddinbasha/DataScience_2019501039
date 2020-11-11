library(party)
library(randomForest)
train = read.csv("D:/Second Year/DataScience_2019501039/Data Mining/Data Mining Assignments/DM Assignment4/sonar_train.csv",header=FALSE)
test = read.csv("D:/Second Year/DataScience_2019501039/Data Mining/Data Mining Assignments/DM Assignment4/sonar_test.csv",header=FALSE)
out = randomForest(nativeSpeaker ~ age + shoeSize + score, data = readingSkills)
out