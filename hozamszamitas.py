import numpy as np
import matplotlib.pyplot as plt
#kovarianciamátrix
def calc_covar (rho, sigma, sigma2):
    cov_matrix=np.zeros((2,2))
    cov_matrix[0,0]=sigma*sigma
    cov_matrix[1,0]=rho*sigma*sigma2
    cov_matrix[0,1]=cov_matrix[1,0]
    cov_matrix[1,1]=sigma2*sigma2
    return cov_matrix
calc_covar(0.14, 0.05,0.1)

#portfólióhozam
def portfolio(mean,cov,size):
    return np.random.multivariate_normal(mean,cov,size)

corr=0.1
covmat=calc_covar(0.14, 0.05,0.1)
means=[0.15,0.05]
nsim=1000
rets=portfolio(means,covmat,nsim)
plt.scatter(rets,rets)
plt.show()






