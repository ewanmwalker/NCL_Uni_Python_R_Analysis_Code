x = rbeta(1e6, 9, 6)
y = rnorm(1e6, mean = 0, sd = 3*x+1/2)

z = c(x,y)

length(z[2*x+3*y>3])/1e6
