import pandas as pd
import numpy as np

data = {"state": ["Ohio", "Ohio", "Ohio", "Nevada", "Nevada", "Nevada"],
        "year": [2000, 2001, 2002, 2001, 2002, 2003],
        "population": [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}

frame = pd.DataFrame(data)
# print(frame.head())
# print(frame.tail())

new_frame = pd.DataFrame(data, columns=["year", "state", "population", "debt"])
# print(new_frame)

# print(frame["population"])
# print(frame.state)

# print(new_frame.iloc[1, 2])

# print(new_frame)

new_frame['debt'] = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6])
# print(new_frame

# print(new_frame)


dummy_arr = [3, 4, 5, 6, 76]
city_arr = ["chicago", "New York", "Houston", "Denver", "San Francisco"]
del_arr = [100, 200, 300, 400, 500]

dummy_dict = {"chicago": 1, "New York": 2,
              "Houston": 3, "Denver": 4, "San Francisco": 5}
val = pd.Series(dummy_arr, index=["one", "two", "three", "four", "five"])

city_val = pd.Series(city_arr)


# print(city_val)


new_dataFrame = pd.DataFrame(dummy_arr, index=city_arr, columns=["population"])
# print(new_dataFrame)

# This is how to add a new coloumn to the dataframe
new_dataFrame["Delegates"] = del_arr
# print(new_dataFrame)


# This is how to delete a new coloumn to the dataframe
new_dataFrame["ErrorColoumn"] = "oops"
# print(new_dataFrame)

del new_dataFrame["ErrorColoumn"]
# print(new_dataFrame)


new_Series = new_dataFrame["Delegates"].copy()
# print(new_dataFrame)

# print(new_Series)


# YOU CAN TRANSPOSE A DATA FRAME JUST LIKE IN NUMPY WITH A T
print(new_dataFrame.T)

# CONVERT TO NUMPY ARRAY
numpy_arr = new_dataFrame.to_numpy()
print(numpy_arr)
