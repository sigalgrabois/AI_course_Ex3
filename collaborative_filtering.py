import time
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import pairwise_distances
from scipy.spatial.distance import pdist


class Recommender:
    def __init__(self, strategy='user'):
        self.user_item_matrix = None
        self.strategy = strategy
        self.similarity = np.NaN

    def fit(self, matrix):
        " * ** YOUR CODE HERE ** * "
        self.user_item_matrix = matrix
        print(self.user_item_matrix)
        mean_user_rating = matrix.mean(axis=1).to_numpy().reshape(-1, 1)
        mean_user_rating.round(2)
        matrix_diff = (matrix - mean_user_rating)
        matrix_diff[np.isnan(matrix_diff)] = 0
        matrix_diff = matrix_diff.round(2) + 0.001

        if self.strategy == 'user':
            # User - User based collaborative filtering
            start_time = time.time()
            self.similarity = 1 - pairwise_distances(matrix_diff, metric='cosine')
            print(self.similarity.shape)
            print(pd.DataFrame(self.similarity).round(2))
            pd.DataFrame(self.similarity.dot(matrix_diff)).round(2)

            self.pred = mean_user_rating + self.similarity.dot(matrix_diff) / np.array(
                [np.abs(self.similarity).sum(axis=1)]).T  # self.pred should contain your prediction metrix.

            time_taken = time.time() - start_time
            print('User Model in {} seconds'.format(time_taken))

            return self

        elif self.strategy == 'item':
            # Item - Item based collaborative filtering
            start_time = time.time()
            self.similarity = 1 - pairwise_distances(matrix_diff.T, metric='cosine')
            print(self.similarity.shape)
            print(pd.DataFrame(self.similarity).round(2))
            pd.DataFrame(self.similarity.dot(matrix_diff.T)).round(2)

            self.pred = matrix_diff.T + self.similarity.dot(matrix_diff.T) / np.abs(self.similarity).sum(axis=1,
                                                                                                         keepdims=True)

            # self.pred should contain your prediction metrix.
            # self.pred should contain your prediction metrix.

            time_taken = time.time() - start_time
            print('Item Model in {} seconds'.format(time_taken))

            return self

    def recommend_items(self, user_id, k=5):
        # k is the number of recommendations
        # we will return in this function a list of k recommended items for the user
        # each item is represented by its product id.
        # if the id is not in the user_item_matrix, return None
        if user_id not in self.user_item_matrix.index:
            return None

        " * ** YOUR CODE HERE ** * "
        if self.strategy == 'user':
            # User - User based collaborative filtering
            user_index = np.where(self.user_item_matrix.index == user_id)[0][0]
            user_pred = self.pred[user_index]
            user_pred = pd.Series(user_pred, index=self.user_item_matrix.columns)
            user_pred = user_pred.sort_values(ascending=False)
            return user_pred.index[:k]


        elif self.strategy == 'item':

            # Item - Item based collaborative filtering

            user_ratings = self.user_item_matrix.loc[user_id]

            similar_items = self.similarity.dot(user_ratings)
            similar_items = pd.Series(similar_items, index=self.user_item_matrix.columns)

            similar_items = similar_items.sort_values(ascending=False)

            return similar_items.index[:k]
