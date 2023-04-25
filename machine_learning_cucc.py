import numpy as np
import matplotlib.pyplot as plt

def generate_synthetic_data(x, coefficients, seed=42, noise_st=1):
    np.random.seed(seed)
    y=np.polyval(coefficients[::-1,x])+np.random.normal(0,noise_std, len(x))
    return x, y
def visualize_data (x,y):
    plt.scatter(x,y)
    plt.xlabel("feature(x)")
    plt.ylabel("target(y)")
    plt.title("Synthetic data with polynomial relationship and noise")
    plt.show()
def main():
    coefficients=[1,0.02,-0.02,0.014]
    x_values=np.linspace(-10,10,100)
    x,y=generate_synthetic_data(x_values, coefficients)
    visualize_data(x,y)