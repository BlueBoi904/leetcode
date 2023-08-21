import pandas as pd
import re


# First attempt
def is_valid_email(email: str):
    domain = '@leetcode.com'
    regex_pattern = "^[a-zA-Z][a-zA-Z0-9._-]+$"
    if not email[0].isalpha():
        return False
    elif not email.endswith(domain):
        return False
    elif not re.match(regex_pattern, email):
        return False

    return True


def valid_emails_(users: pd.DataFrame) -> pd.DataFrame:
    rows_to_remove = []
    emails = users['mail']
    for email in emails:
        print(email)

    for idx, email in enumerate(emails):
        if not is_valid_email(email):
            rows_to_remove.append(idx)

    users.drop(rows_to_remove)


def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    pattern = r'^[a-zA-Z][a-zA-Z0-9._-]*@leetcode\.com$'
    valid = users[users['mail'].str.match(pattern)]

    return pd.DataFrame(valid)
