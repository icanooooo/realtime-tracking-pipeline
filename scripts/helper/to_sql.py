from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.dialects.postgresql import insert

def to_sql(df, table_name):
    engine = create_engine("postgresql+psycopg2://icanooo:thisisapassword@application_postgres:5432/historical_db")
    metadata = MetaData()

    metadata.reflect(bind=engine)

    my_table = metadata.tables[table_name]

    df = df.to_dict(orient='records')

    stmt = insert(my_table).values(df)
    stmt = stmt.on_conflict_do_nothing(index_elements=['id'])

    with engine.begin() as conn:
        conn.execute(stmt)
