import pandas as pd


def main():

    # Pandas Series data structure
    new_object = pd.Series([9, 3, 11, 0], index=["a", "b", "c", "d"])

    print(new_object.get("b"))
    print(new_object["a"])  # same as

    # print(new_object.index)
    # print(new_object.values)

    print(new_object[new_object > 3])
    print(new_object)

    # Think of series as a basic Python dictionary, and can be converted and back
    python_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
    pandas_series = pd.Series(python_dict)

    covert_python_dict = pandas_series.to_dict()
    print(pandas_series)
    print(covert_python_dict)


if __name__ == "__main__":
    main()
