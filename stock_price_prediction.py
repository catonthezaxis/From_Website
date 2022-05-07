import matplotlib.pyplot as plt
import numpy as np

dt = 1/365.0
S0 = 60
mu = 0.05
sigma = 0.3

ndays_total = 90
NTRIALS = 10000
S_prediction = []

#np.random.seed(0)

for nday in range(ndays_total):
    S_SUB = 0
    for j in range(NTRIALS):
        n = np.random.normal(0, np.sqrt(dt),nday + 1)
        S = S0
        for i in range(nday+1):
            dS = mu*S*dt + sigma*S*n[i]
            S += dS
        S_SUB += S
    S_prediction.append(S_SUB/NTRIALS)


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(S_prediction,'ro-')
ax.set_xlabel('day')
ax.set_ylabel('stock price')
plt.show()
        