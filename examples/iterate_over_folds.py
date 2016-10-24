"""
This module descibes how to manually train and test an algorithm without using
the evaluate() function.
"""

from recsys import BaselineOnly
from recsys import Dataset
from recsys import evaluate
from recsys import accuracy

# Load the movielens-100k dataset and split it into 3 folds for
# cross-validation.
data = Dataset.load_builtin('ml-100k')
data.split(n_folds=3)

algo = BaselineOnly()

for trainset, testset in data.folds:

    # train and test algorithm.
    algo.train(trainset)
    predictions = algo.test(testset)

    # Compute and print Root Mean Squared Error
    rmse = accuracy.rmse(predictions, verbose=True)