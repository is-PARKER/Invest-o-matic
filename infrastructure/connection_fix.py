import typing

def replace_postgres(db_url: str ):
    fixed_db_url = db_url.replace("postgres", "postgresql+psycopg2")

    return fixed_db_url



