import random
import numpy as np
import matplotlib.pyplot as plt

def coin_flip():
    return random.randint(0,1)

def monte_carlo(n):
    #n defines the coin flipping times
    Probability = []
    Result = 0
    for i in range(n):
        if coin_flip() == 1:
            Result += 1
        else:
            Result = Result
        Probability.append(Result/(i+1))

    plt.axhline(y = 0.5, color = 'r', linestyle = '-')
    plt.xlabel('Flip')
    plt.ylabel('Probability')
    plt.plot(Probability)
    plt.show(block=False)

    return Probability[-1]

if __name__ == "__main__":
    m = 5
    n = 5000
    Probability_sum = 0
    for i in range(m):
        Probability_sum += monte_carlo(n)
    final_Probability = Probability_sum/m

    print('After {} coin flipping, the probability of head is {}'.format(m*n, final_Probability))
        
