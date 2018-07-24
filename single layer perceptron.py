import random as r
import numpy as np
import matplotlib.pyplot as plt


real_f = float(150)
real_c = float(50)
real_k = float(100)
real_prices = np.array([real_f,real_c,real_k])

fish = float(50)

chips = float(50) 
ketchup = float(50)
rand_prices = np.array([fish,chips,ketchup])

lr = 0.001

hundred_prices = []

for t in range(100):
    order = np.array([r.randint(0,10),r.randint(0,10),r.randint(0,10)])
    tot_price = sum(order*real_prices)

    hundred_prices.append(rand_prices.copy())

    pred_price = sum(order*rand_prices)
    cur_res_err = tot_price - pred_price
    # print("New order,",t," residual error:",cur_res_err)

    if -0.001 < cur_res_err < 0.001:
        print("check the predicted prices",rand_prices)
        # wait = input("PRESS ENTER TO CONTINUE.")
    
    while cur_res_err > 1.0e-4 or cur_res_err < -1.0e-4:
        for i in range(len(rand_prices)):
            #update the weights (i.e predicted prices)
            change = lr*order[i]*cur_res_err
            #print("change: ",change)
            rand_prices[i] = rand_prices[i] + change
        #print("current predicted prices:",rand_prices)
        pred_price = sum(order*rand_prices)
        #print("new predicted tot price:",pred_price,"real:",tot_price,end=" ")
        cur_res_err = tot_price - pred_price
        #print("Residual error:",cur_res_err)
    #wait = input("PRESS ENTER TO CONTINUE.")

print(hundred_prices,sep="\n")
plt.plot(hundred_prices)
plt.title("Predicted prices")
plt.legend(["fish","chips","ketchup"])
plt.show()
