input <- read.csv("C:/Users/BASHA/Downloads/Compressed/Final exam/Liver_data.csv",header=FALSE)
set.seed(200)
var <- kmeans(scale(input[,-7]), 4, nstart = 30,iter.max=15)
fviz_cluster(var, data = input[, -7],
             geom = "point",
             ellipse.type = "convex",
             ggtheme = theme_bw()
)