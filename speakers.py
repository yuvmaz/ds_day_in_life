from scipy.stats import bernoulli
import pandas as pd
import numpy as np

def get_data():
    np.random.seed(3423)
    yuval = bernoulli.rvs(p=0.78, size=15)
    ido = bernoulli.rvs(p=0.83, size=8)
    yaniv = bernoulli.rvs(p=0.81, size=10)
    
    data = []
    for name,values in zip(('ido','yaniv','yuval'), 
                 (yuval, ido, yaniv)):
        for value in values:
            data.append((name, value))
        
    return pd.DataFrame(data=data, columns=['name', 'value'])