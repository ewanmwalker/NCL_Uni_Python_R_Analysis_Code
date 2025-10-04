x = rbeta(1000, 9, 6)

Q2 = function(N = 1000){
  X = rbeta(1000, 9, 6)
  Y = rexp(N, 1/X)
  results = matrix(ncol = 2, nrow = N)
  results[,1] = X
  results[,2] = Y
  return(results) }

test = Q2()
plot(test[,1], test[,2])
