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


def print_data(data):

    print(f"number of users are :  {None}")
    print(f"number of products ranked are : {None}")
    print(f"number of ranking are: {None}")
    print(f"minimum number of ratings given to a product : {None}")
    print(f"maximum number of ratings given to a product : {None}")
    print(f"minimum number of products ratings by user : {None}")
    print(f"maximum number of products ratings by user : {None}")



