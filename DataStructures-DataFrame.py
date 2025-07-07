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

print(new_frame)

new_frame['debt'] = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6])
# print(new_frame

print(new_frame)
