from helper.to_sql import to_sql, get_sql
from helper.update_helpers import update_orders

def update_data():  
    a = get_sql("orders_history")
    b = get_sql("destinations")
    c = get_sql("station")

    df = update_orders(a, b, c)
    
    to_sql(df, "orders_history") 

if __name__ == "__main__":
    update_data()
