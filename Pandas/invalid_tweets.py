import pandas as pd


def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    df = tweets[tweets["content"].str.len() > 15]

    # Select only the 'tweet_id' column from the invalid tweets DataFrame
    result_df = df[["tweet_id"]]

    return result_df
