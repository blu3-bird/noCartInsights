import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from  sqlalchemy import text

load_dotenv()

# loading env variables from .env file
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')

db_url = (f"postgresql+psycopg://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")


engine = create_engine(db_url)

# Testing connection
with engine.connect() as connection:
    results = connection.execute(
        text("Select 1")
    )
    print(results.scalar())

