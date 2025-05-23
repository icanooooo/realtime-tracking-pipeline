import random
import pandas as pd

def get_location(location_df, destination_id):
    location_df = location_df[location_df['destination_id'] == destination_id]

    location = location_df.to_dict(orient="records")
    
    return location[0]['destination'], location[0]['station']

def merge_location(destination, station):
    location = pd.merge(destination, station, left_on='station_id', right_on='id', how='left')

    location.drop(columns=['id_y', 'station_id', 'created_at_x', 'created_at_y'], inplace=True)
    location.rename(columns={'id_x':'destination_id',
                             'name_x': 'destination',
                             'name_y':'station'}, inplace=True)
    return location

def update_location(location, location_df, destination_id):
    destination, station = get_location(location_df, destination_id)
    
    locations = ['not yet send', 'on transport', f"{station} station",
                 'on transport to destination', f"{destination} transit area", 'arrived at address']

    next_location = locations[locations.index(location) + 1] 

    return next_location

def update_status(status):
    statuses = ['pending', 'shipped', 'on transit', 'shipped to destination', 'on transit', 'delivered'] 

    next_status = statuses[statuses.index(status) + 1]

    return next_status

def update_order(order):
    print('test')

def update_orders(orders, destination, station):
    number = random.randint(5, 10)

    orders_updated = orders.sample(n=number) 
    orders_updated = orders_updated.to_dict(orient="records")

    location = merge_location(destination, station)

    new_orders = []

    for i in orders_updated:
        order_updated = i
        
        if order_updated['status'] == 'delivered':
            continue

        order_updated['id'] = order_updated['id'] + 1
        order_updated['status'] = update_status(order_updated['status'])
        order_updated['location'] = update_location(order_updated['location'],
                                                    location, order_updated['destination_id']) 

        new_orders.append(order_updated)

    df = pd.DataFrame(new_orders)

    return df
