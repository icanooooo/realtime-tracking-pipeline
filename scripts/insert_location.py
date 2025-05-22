from helper.to_sql import to_sql
import pandas as pd


def create_station(region_df):
    station = region_df[['Station', 'City']].copy()
    station.drop_duplicates(inplace=True)
    station.reset_index(drop=True, inplace=True)
    station.reset_index(inplace=True)
    station.rename(columns={'index': 'id', 'Station':'name', 'City':'city'}, inplace=True) 
    station['created_at'] = pd.Timestamp.now()
    station['id'] = station['id'] + 1

    return station

def edit_region(region, station_df):
    region.drop(columns=['City', 'Unnamed: 0'], inplace=True)
    region.rename(columns={'index': 'id', 'kelurahan':'name'}, inplace=True)

    region = region.merge(station_df, left_on='Station', right_on='name', how='left')

    region.rename(columns={'name_x':'name',
                           'id_x': 'id', 
                           'id_y': 'station_id'}, inplace=True)
    region.drop(columns=['city', 'name_y', 'Station'], inplace=True)
    region['created_at'] = pd.Timestamp.now()
    region['id'] = region['id'] + 1

    return region

def main():
    region = pd.read_csv("destination_region.csv")
    region.reset_index(inplace=True)

    station = create_station(region)

    region = edit_region(region, station)

    to_sql(station, "station")
    to_sql(region, "destinations")

if __name__ == "__main__":
    main()
