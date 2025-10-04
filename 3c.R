LN = function(N, mu, sigma){
  return(exp(rnorm(N , mean = mu, sd = sigma ) ))
}

sigma = 2
mu = seq(0,5,0.01)
y = rep(0,length(mu))
N = 1000

for(i in 1:length(mu)){
  y[i] = log( median( LN(N, mu[i], sigma )))
}

plot(mu,y, xlab="Mean / μ", ylab="Log of sample median", pch="X", main="The log of the sample median from samples 
  of the log-normal distribution for various
  means μ in range (0,5), σ = 2")

