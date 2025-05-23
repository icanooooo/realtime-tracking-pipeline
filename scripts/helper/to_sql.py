from sqlalchemy import create_engine, MetaData, Table, text
from sqlalchemy.dialects.postgresql import insert

import pandas as pd

def get_engine(host):
    engine = create_engine(f"postgresql+psycopg2://icanooo:thisisapassword@{host}:5432/historical_db")
    
    return engine

def to_sql(df, table_name, host="application_postgres"):
    engine = get_engine(host) 
    metadata = MetaData()

    metadata.reflect(bind=engine)

    my_table = metadata.tables[table_name]

    df = df.to_dict(orient='records')

    stmt = insert(my_table).values(df)
    stmt = stmt.on_conflict_do_nothing(index_elements=['id'])

    with engine.begin() as conn:
        conn.execute(stmt)

def get_sql(table, host="application_postgres"):
    engine = get_engine(host)

    with engine.connect() as connection:
        result = connection.execute(text(f"SELECT * FROM {table}"))

        rows = result.fetchall()
        headers =  result.keys()

        df = pd.DataFrame(rows, columns=headers)

        return df
