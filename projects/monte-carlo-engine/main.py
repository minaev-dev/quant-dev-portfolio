import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

def simulate_convergence(Ns, mu=0, sigma=1):
    means = []
    for N in Ns:
        data = np.random.normal(mu, sigma, N)
        means.append(np.mean(data))
    return means

Ns = [10, 100, 1000, 10000, 100000]
means = simulate_convergence(Ns)

plt.figure(figsize=(10, 6)) 
plt.plot(Ns, means, marker='o', label='Среднее' ) 
plt.axhline(0, color='red', linestyle='--', label='Теоретическое среднее (0)') 
plt.xscale('log') 
plt.xlabel('Размер выборки (N)') 
plt.ylabel('Среднее значение') 
plt.title('Сходимость среднего к 0 (закон больших чисел)') 
plt.grid(True, alpha=0.3) 
plt.legend() 
plt.savefig('projects/monte-carlo-engine/results/convergence.png') 
plt.show() 