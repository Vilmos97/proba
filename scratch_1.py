import numpy as np
import matplotlib.pyplot as plt
import sklearn.model_selection as skms
import sklearn.preprocessing as skpp
import sklearn.pipeline as skpl
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


def generate_polinomial_data(coefficients, fromX, toX, n_samples, noise, random_state=None):
    np.random.seed(random_state)
    X=np.random.uniform(fromX, toX, n_samples)
    Y=np.polyval(coefficients[::-1],X)+noise*np.random.randn(n_samples)
    return X.reshape(-1,1), Y

coeffs=[100,1,0.2]
X,Y=generate_polinomial_data(coeffs, fromX=-5, toX=7, n_samples=500, noise=1, random_state=42)
plt.scatter(X,Y,label="Data", alpha=0.5)
plt.show()

X_train, X_test, Y_train,Y_test=skms.train_test_split(X,Y, test_size=0.2, random_state=42)

def plot_train_test_split(X_train, X_test, Y_train,Y_test):
    plt.scatter(X_train, Y_train, label="Train", alpha=0.5)
    plt.scatter(X_test,Y_test, label="Test", alpha=0.5)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Train-Test Split")
    plt.legend()
    plt.show()
plot_train_test_split(X_train, X_test, Y_train,Y_test)

def create_polynomial_model(degree=1):
    name="Polynomial_" + str(degree)
    model=skpl.make_pipeline(skpp.PolynomialFeatures(degree), LinearRegression())
    return name, model

def create_train_and_evaluate_polynomial_model(X_train, Y_train, X_test,Y_test, degree=15):
    name, model=create_polynomial_model(degree)
    model.fit(X_train, Y_train)
    coefficients_on_train_set=model.named_steps["linearregression"].coef_
    Y_pred=model.predict(X_test)
    mse_on_test_set=mean_squared_error(Y_test, Y_pred)
    return name, model, mse_on_test_set, coefficients_on_train_set
#name, model, mse_on_test_set, coefficients_on_train_set = create_train_and_evaluate_polynomial_model(X_train, Y_train, X_test,Y_test,degree=15)
#print(mse_on_test_set)
def print_coeffs(text, model):
    if 'linear_regression' in model.named_steps.keys():
        linreg = 'linear_regression'
    else:
        linreg = 'linearregression'
    coeffs = np.concatenate(([model.named_steps[linreg].intercept_], model.named_steps[linreg].coef_[1:]))
    coeffs_str = ' '.join(np.format_float_positional(coeff, precision=4) for coeff in coeffs)
    print(text + coeffs_str)


def hyperparameter_search(X_train, Y_train, X_test, Y_test, from_degree=1, to_degree=15):
    degrees=range(from_degree, to_degree+1)
    best_degree, best_mse, best_model=None,float('inf'), None
    d_mse=[]
    for degree in degrees:
        name, model, mse_on_test_set, coefficients_on_train_set = create_train_and_evaluate_polynomial_model(X_train, Y_train, X_test,Y_test,degree=degree)
        d_mse[degree]=mse_on_test_set
        print(f"for degree: {degree}, MSE: {mse_on_test_set}")
        if mse_on_test_set<best_mse:
            best_degree, best_mse, best_model=degree, mse_on_test_set, model
    print(f"best degree: {best_degree}, best MSE: {best_mse}")
    print_coeffs("Coefficients: ", best_model)
    return best_model
best_model=hyperparameter_search(X_train, Y_train, X_test, Y_test, from_degree=1, to_degree=15)

print_coeffs("Coefficients: ", best_model)

