x = c(90,703,68,146,840,272,580,164,63,267,111,102,379,272,610,439,111,119,6,137)
lambda = 1 / mean(x)

y = rexp(1e6)

sim = 2*y*lambda*exp(-lambda*y^2)

hist(sim)