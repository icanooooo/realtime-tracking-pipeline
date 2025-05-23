from helper.generate_helper import generate_users
from helper.to_sql import to_sql

import pandas as pd
import random

def users():

    number = random.randint(25, 50)

    users = generate_users(number)
    users_df = pd.DataFrame(users)

    print(users_df)
    to_sql(users_df, "users")

def main():
    users()
   
if __name__ == "__main__":
    main()
