import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(0, 1, 1000000)
mean_data = np.mean(data)
Ns = np.array([10, 100, 1000, 10000, 100000])
means = []

for N in Ns:
    data = np.random.normal(0, 1, N)
    mean_val = np.mean(data)
    means.append(mean_val)

plt.figure(figsize=(10, 6)) #1
plt.plot(Ns, means, marker='o', label='Среднее' ) #2
plt.axhline(0, color='red', linestyle='--', label='Теоретическое среднее (0)') #3
plt.xscale('log') #4
plt.xlabel('Размер выборки (N)') #5
plt.ylabel('Среднее значение') #5
plt.title('Сходимость среднего к 0 (LLM)') # 6
plt.grid(True, alpha=0.3) # 7
plt.legend() # 8
plt.savefig('projects/monte-carlo-engine/results/convergence.png') # 9
plt.show() # 10