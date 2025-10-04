set.seed(200818067)

a = sample (3:14 , 1) ; b = sample (3:14 , 1)
x = seq(0,1,0.001)
y = a*b*(x^(a-1))*((1-(x^a))^(b-1))

plot(x,y, xlab = "x" , ylab="f(x)" , type = "l", main="A graph of f(x) with grid lines, for 0 <= x <= 1")

abline(v = 0, lty = 5, col = "red")
abline(v = 1, lty = 5, col = "red")
abline(h = max(y)+0.1, lty = 5, col = "red")

MCI = function(N) {
  
  #set a tally variable for hits under the graph, above y=0
  no_of_hits = 0
  
  for(i in 1:N){
  
  #Generate x and y coords
  x0 = runif(1, 0, 1)
  y0 = runif(1, 0, max(y)+0.1)
  
  #f(x) at x
  f = a*b*(x0^(a-1))*((1-(x0^a))^(b-1))
  
  if(y0 < f){  #if the point is under the curve then
      no_of_hits = no_of_hits + 1
    }
  }
  
  P = no_of_hits / N           #The proportion under the curve
  area_under_curve = P*(1*(max(y)+0.1))      #The total area under
  return(area_under_curve)
}

MCI(1e6)