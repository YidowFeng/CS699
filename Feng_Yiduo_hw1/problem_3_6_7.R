#problem 3

#(1). Calculate the mean, median, and standard deviation (sample) of the attribute A5.
f <- read.csv(file="C:/Users/Yidow/Desktop/Feng_Yiduo_hw1/a1.csv")
head(f)
mean(f[,5])
median(f[,5])
sd(f[,5])

#(2). Determine Q1, Q2, and Q3 of A5.
quantile(f[,5])

# (3). Detect outliers using the IQR method, which we discussed in the class, and show the 
# A5 values of the detected outliers. When detecting outliers, use only the A5 values. 

# (4). Plot the boxplot of the attribute A5. In your boxplot, you need to show outliers 
# separately.
boxplot(f[,5])

#Problem 6
abs(43-25)+abs(14-20)+abs(32-15)+abs(21-14)

sqrt(abs(43-25)^2+abs(14-20)^2+abs(32-15)^2+abs(21-14)^2)

#Problem 7
sqrt(abs(0.33-1)^2+abs(0.5-0)^2+abs(0.5-1)^2+abs(0-1)^2)




