alpha = a
Lambda = b

#y = seq(0,10000,0.01)

Fy = (19/5) * (8^11*(((19/5)*y)^10)*exp(-88)) / (10*9*8*7*6*5*4*3*2)
  

hist(Fy, prob=TRUE)


##




x=seq(0,1,0.0001)

fx = (8^11 * x^10 * exp(-8*x)) / factorial(10)

fy = (19/5) * (8^11*(((19/5)*x)^10)*exp(-8*(19/5)*x)) / factorial(10)

Fy = rep(0,length(fy))
for(i in 2:length(fy)){
  Fy[1] = fy[1]
  Fy[i] = fy[i]+Fy[i-1]
}

Ex = sum(x*fx)
Ey = Ex*3.8 
x[ sum(Fy < Ey) ]

plot(x,Fy, type="l", ylab="Accumulative y")

