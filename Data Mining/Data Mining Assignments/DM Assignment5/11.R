data = read.csv("D:/Second Year/DataScience_2019501039/Data Mining/Data Mining Assignments/DM Assignment5/spring2008exams.csv")
exam2mean = mean(data[,2], na.rm=TRUE)
exam2sd = sd(data[,2],na.rm=TRUE)
z = (data[,2] - exam2mean)/exam2sd
sort(z)