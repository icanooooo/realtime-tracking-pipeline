from helper.generate_helper import generate_users
import pandas as pd

users = generate_users(10)

users_df = pd.DataFrame(users)

print(users_df)
