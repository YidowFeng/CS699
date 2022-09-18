#problem 3
df <- read.csv(file = 'C:/Users/Yidow/Desktop/Feng_Yiduo_hw2/a2-p3.csv')
conTable_14 <- table(df[,c("A1","A4")])
print(conTable_14)
conTable_24 <- table(df[,c("A2","A4")])
print(conTable_24)