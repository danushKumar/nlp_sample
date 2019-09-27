import pandas as pd
import numpy as np

class Dataset(object):
     
    def __init__(self, path):
        self.data = pd.read_csv(path)
        self.train_data = split(self.data) 

    def split(self, data = self.data, train_size = 70):
        data_clone = data.copy()
        data_size = data.shape(0)
        split_size = data_size / (train_size / 100)
        train_data = data_clone[: slipt_size]
        test_size = data_clone[split_size :] 
        
        return train_data, test_data 