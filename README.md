# mini-project---single-layer-perceptron
I was bored and wanted to hard-code the famous fish-chips-ketchup perceptron model.

Predicted prices start at 50 for each.Real prices are:
fish = 150
chips = 50
ketchup = 100

Iterates 100 times for 100 different orders. Within each order minimizes residual error (Actual price-predicted price)
by learning rate (0.001) x number of item orders x current residual error

Finally plots the final predictions of each order. Note that as new orders come, the predicted prices converges to the actual prices.


