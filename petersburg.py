import random
import math
import matplotlib.pyplot as plt

class ParadoxPetersburg():
    
    def __init__(self, trials):
        self.trials = trials
        self.plays = 0
        self.means = []
        self.cumulativeValue = 0
        self.maxFlip = [0,0]
        
    def flip(self):
        heads = random.choice([True, False])
        return heads

    def play(self):
        numFlip = 1 # there will always be at least one flip
        while(not self.flip()):
            numFlip += 1
        if numFlip > self.maxFlip[0]:
            self.maxFlip[0] = numFlip
            self.maxFlip[1] = self.plays
        return numFlip

    def simulate(self):
        for i in range(self.trials):
            self.plays += 1
            numFlips = self.play()
            value = 2**numFlips #amount of money from one play
            self.cumulativeValue += value
            self.means.append(self.cumulativeValue / self.plays) #adds to the list of means the mean thusfar

    def getTrials(self):
        print(self.trials)
        
    def getCumulativeValue(self):
        print(self.cumulativeValue)
        
    def getMax(self):
        print(self.maxFlip)
        
    def graphMeans(self):
        plt.plot(self.means)
        plt.plot(self.maxFlip[1], 0, 'r+')
        plt.show()

    def probabilityOfValue(self):
        value = input('You would like to know the probability of winning how much $')
        numFlips = math.log(int(value), 2)
        prob = 0.5**numFlips
        print('The p.value for ${} is {}'.format(value, prob))

t=input('how many simulations? ')
s1 = ParadoxPetersburg(int(t))
s1.simulate()
s1.getMax()
s1.graphMeans()
s1.probabilityOfValue()
input('...')
            
