import scratch_1 as sc

coeffs=[100,1,0.2]
X,Y=sc.generate_polinomial_data(coeffs, fromX=-5, toX=7, n_samples=500, noise=1, random_state=42)
X_train, X_test, Y_train,Y_test=sc.train_test_split(X,Y, test_size=0.2, random_state=42)
name, model, mse_on_test_set, coefficients_on_train_set=sc.create_train_and_evaluate_polynomial_model(X_train, Y_train, X_test,Y_test,degree=15)