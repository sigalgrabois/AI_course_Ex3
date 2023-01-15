import matplotlib.pyplot as plt
import seaborn as sns


def watch_data_info(data):
    # This function returns the first 5 rows for the object based on position.
    # It is useful for quickly testing if your object has the right type of data in it.
    print(data.head())

    # This method prints information about a DataFrame including the index dtype and column dtypes, non-null values and memory usage.
    print(data.info())

    # Descriptive statistics include those that summarize the central tendency, dispersion and shape of a dataset’s distribution, excluding NaN values.
    print(data.describe(include='all').transpose())


# Part 1

# This method returns the number of unique users in the train.csv
def get_unique_users(data):
    return len(data['UserId'].unique())
    # return the unique users from the data


# This function returns the number of unique products in the train.csv
def get_unique_products(data):
    return len(data['ProductId'].unique())


# This function returns the number of ratings in the train.csv
def get_number_of_ratings(data):
    return len(data['Rating'])
    # return the number of ratings from the data


# Part 2
# this function returns the maximal number of times that a product was rated
def get_max_number_of_ratings_given_to_a_product(data):
    return data.groupby('ProductId').size().max()


# this function returns the minimal number of times that a product was rated
def get_min_number_of_ratings_given_to_a_product(data):
    return data.groupby('ProductId').size().min()


# PART 3:
# this function returns the maximal number of ratings that a user rated
def get_max_number_of_ratings_given_by_a_user(data):
    return data.groupby('UserId').size().max()


# this function returns the minimal number of ratings that a user rated
def get_min_number_of_ratings_given_by_a_user(data):
    return data.groupby('UserId').size().min()


def print_data(data):
    print(f"number of users are :  {get_unique_users(data)}")
    print(f"number of products ranked are : {get_unique_products(data)}")
    print(f"number of ranking are: {get_number_of_ratings(data)}")
    print(f"minimum number of ratings given to a product : {get_min_number_of_ratings_given_to_a_product(data)}")
    print(f"maximum number of ratings given to a product : {get_max_number_of_ratings_given_to_a_product(data)}")
    print(f"minimum number of products ratings by user : {get_min_number_of_ratings_given_by_a_user(data)}")
    print(f"maximum number of products ratings by user : {get_max_number_of_ratings_given_by_a_user(data)}")
