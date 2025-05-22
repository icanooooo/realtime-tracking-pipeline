from faker import Faker
import random
from datetime import datetime

def generate_users(n=10):
    fake = Faker() 

    users = []
    for _ in range(n):
        user = {
                "username": fake.user_name(),
                "email": fake.unique.email(),
                "created_at": datetime.now().isoformat()
            }
        users.append(user)

    return users
