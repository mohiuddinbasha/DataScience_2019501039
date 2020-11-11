data = read.csv("D:/Second Year/DataScience_2019501039/Data Mining/Data Mining Assignments/DM Assignment5/spring2008exams.csv")
q1 = quantile(data$Midterm.2, 0.25, na.rm = TRUE)
q3 = quantile(data$Midterm.2, 0.75, na.rm = TRUE)
interQrtile = q3-q1
interQrtile
data[(data$Midterm.2 > q3 + 1.5 * interQrtile), 3]
data[(data$Midterm.2 > q1 - 1.5 * interQrtile), 3]
boxplot(data$Midterm.2, col="Red", main="Exam Scores", xlab=("Exam 2"),ylab="Exam Score")