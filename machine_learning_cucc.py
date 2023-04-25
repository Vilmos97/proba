import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def fit_linear_regression(x,y):
    lr=LinearRegression()
    lr.fit(x.reshape(-1,1),y)
    return lr

def generate_synthetic_data(x, coefficients, seed=42, noise_std=1):
    np.random.seed(seed)
    y=np.polyval(coefficients[::-1,x])+np.random.normal(0,noise_std, len(x))
    return x, y
def visualize_data_and_fit (x,y,model):
    plt.scatter(x,y)
    plt.xlabel("feature(x)")
    plt.ylabel("target(y)")
    plt.title("Synthetic data with polynomial relationship and noise")
    x_pred = np.linspace(min(x),max(x),len(x)).reshape(-1,1)
    y_pred=model.predict(x_pred)
    plt.plot(x_pred,y_pred, color='red', label='Linear Regression fit')
    plt.legend
    plt.show()
def main():
    coefficients=[1,0.02,-0.02,0.014]
    x_values=np.linspace(-10,10,100)
    x,y=generate_synthetic_data(x_values, coefficients)
    lr=fit_linear_regression(x,y)
    visualize_data_and_fit(x,y,lr)