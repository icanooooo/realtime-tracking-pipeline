from faker import Faker
import random
import time
from datetime import datetime

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

    return users
