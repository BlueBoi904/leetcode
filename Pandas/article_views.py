import pandas as pd


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    views = views[views["author_id"] == views["viewer_id"]]
    views = views[["author_id"]].sort_values(by="author_id")
    views.drop_duplicates(subset="author_id", inplace=True)
    views.rename(columns={"author_id": "id"}, inplace=True)
    return views
