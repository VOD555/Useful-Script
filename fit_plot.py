import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
import seaborn.apionly as sns

data = np.loadtxt('msd.xvg')
x = np.zeros(np.shape(data))
x[:,1] = data[:,0]
x = x/1000
regr = linear_model.LinearRegression()
regr.fit(x, data[:,1])

y_hat = np.dot(x, np.array(regr.coef_).T)

fig = plt.figure(figsize=(8,4))
ax = fig.add_subplot(1, 1, 1)

ax.plot(data[:,0],data[:,1], color = 'k', label = 'Data')
ax.plot(data[:,0], y_hat, color='blue', label = 'Fitted line')

ax.legend(loc='best')
ax.set_xlabel(r"time  $t$ (ps)")
ax.set_ylabel("msd (nm)")

sns.despine(offset=10, ax=ax)

plt.tight_layout()

fig.savefig('fit.png')
