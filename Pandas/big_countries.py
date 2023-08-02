import pandas as pd


def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    # selecting the required columns
    df = world[["name", "population", "area"]]

    # operation to get result
    resdf = df[(df["population"] >= 25000000) | (df["area"] >= 3000000)]

    return resdf
