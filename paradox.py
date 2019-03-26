import random
import matplotlib.pyplot as plt

random.seed(1256)
def heads():
    """using a random number generator this returns either heads or tails"""
    coin = random.choice([0,1])
    if (coin == 0): #tails
        return False
    else: #heads
        return True

def play():
    """performs one iteration of the game. flips coins until their is a success(heads)
and then it returns the number of flips and the amount of money that it earned"""
    count = 1
    while (not heads()):
        count += 1
    cash = 2 ** count
    return count, cash

def simulate(trials):
    """takes the number of trials and runs that many of them keeping track of the total
money earned and the total number of trials. Returns an array of the rolling means, each
one being the total mean of that number of trials so far"""
    maxim = []
    means = []
    total_cash = 0
    total_flip = 0
	
    for i in range(trials): #loops through n trials 
        count, cash = play() 
        maxim.append(count)
        total_flip += count
        total_cash += cash
        means.append(total_cash/(1 + len(means)))
		
    return means, total_flip, total_cash, maxim

trials = input('Enter the number of trials: ')
means = simulate(int(trials))

plt.plot(means[0])

plt.show()
print(max(means[3]))

input()

    


