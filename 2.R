d = 7
sig = 1 + (d/2.5)
N = 10000

#Inverse CDF
x = seq(0,0.99999,0.00001)
y = sqrt(-2*sig^2*log(1-x))

#Sample the inverse CDF
Sx = sample(y,N, replace = FALSE)

#Plot the density of the sample
hist(Sx, prob=TRUE, main="Inverse CDF method given fX(x)", xlab="x", 
     ylab="Density")

#Superimposing a red curve of the PDF
x0 = seq(0,18,0.001)
y0 = x0/(sig^2)*exp((-x0^2)/(2*sig^2))
lines(x0, y0, type="l", col="red")

# Check the expectation with the source
# Equally likely values so use mean
mean(y) #calculated
1.2533*sig #source

# Check the variance with the source
var(y) #calculated
0.4292*sig^2 #source