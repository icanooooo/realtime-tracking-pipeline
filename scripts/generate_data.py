from helper.generate_helper import generate_users, generate_orders, generate_hist_orders
from helper.to_sql import to_sql, get_sql

import pandas as pd
import random

def users():

    number = random.randint(25, 50)

    users_df = generate_users(number)

    print(users_df)
    to_sql(users_df, "users")

def orders():
    number = random.randint(10, 24)
    df_destination, df_users = get_sql("destinations"), get_sql("users")

    orders_df = generate_orders(df_destination,df_users, number)

    to_sql(orders_df, "orders")

def hist_orders():
    orders = get_sql("orders")
    
    hist_df = generate_hist_orders(orders)

    to_sql(hist_df, "orders_history")


def main():
    users()

    orders()

    hist_orders()
   
if __name__ == "__main__":
    main()
