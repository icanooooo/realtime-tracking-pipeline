from faker import Faker
from datetime import datetime

import random
import time
import pandas as pd

def generate_users(n=10):
    fake = Faker() 

    users = []
    for _ in range(n):
        
        timestamp = time.time_ns() // 1000
        random.seed(timestamp)

        user = {
                "id": random.randint(10000, 100000 - 1), 
                "username": fake.user_name(),
                "email": fake.unique.email(),
                "created_at": datetime.now().isoformat()
            }
        users.append(user)

    users_df = pd.DataFrame(users)
    
    return users_df

def generate_orders(destination_df, users_df, n=1):
    selected_destination = destination_df.sample(n=n)

    selected_user = users_df.sample(n=n)

    orders = [] 

    for i in range(n):
        order = {}

        order['id'] = random.randint(10000, 100000 - 1)
        order['user_id'] = selected_user.iloc[i, selected_user.columns.get_loc('id')]
        order['destination_id'] = selected_destination.iloc[i, selected_destination.columns.get_loc('id')]
        order['order_date'] = datetime.now().isoformat()

        orders.append(order)

    orders_df = pd.DataFrame(orders)

    return orders_df

def generate_hist_orders(orders_df):
    data = orders_df.to_dict(orient='records')

    hist_data = []

    for i in data:
         hist = {
                 'id' : random.randint(10000, 100000 - 1),
                 'orders_id' : i['id'],
                 'status' : 'pending',
                 'location' : 'not yet send',
                 'updated_at' : datetime.now().isoformat()
                }

         hist_data.append(hist)

    hist_df = pd.DataFrame(hist_data)

    return hist_df



