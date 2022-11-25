from scipy.stats import binom

import matplotlib.pyplot as plt

num_trials = 10

heads_probability = .5

probs = [binom.pmf(i, num_trials,
heads_probability) for i in
range(11)]

plt.stem(list(range(11)), probs)

plt.show()
import matplotlib.pyplot as plt

from scipy.stats import poisson

rate = 3.3

probs = [poisson.pmf(i, rate) for
i in range(15)]

plt.stem(list(range(15)), probs)

plt.show()
import numpy as np

import seaborn as sns

scale = 1 / 3.3

draws = np.random.exponential(scale, size = 1_000_000)

sns.kdeplot(draws, shade=True, color='xkcd:lightish blue')

