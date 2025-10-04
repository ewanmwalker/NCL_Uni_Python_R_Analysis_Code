n = 1000

invcdf = function(n){
  U = runif(n)
  ans = c(0,n)
  cdf = asin(2*U)
  return(cdf)
}

hist(invcdf(1000), col="purple", prob=TRUE, xlab="Wind direction from facing forward", ylab="density", 
main="Histogram of wind directions using inverse cdf")

curve(cos(x)/2, add = TRUE, lty = 5)