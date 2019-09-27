import nltk
from .dataset import Dataset

##load data
root_dir = './data'
data = Dataset(root_dir + '/spam_not_spam.csv')

