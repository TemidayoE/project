from dotenv import load_dotenv
import os


load_dotenv(".env")


SQLALCHEMY_DATABASE_URL: str = os.getenv('SQLALCHEMY_DATABASE_URL')

database_url = SQLALCHEMY_DATABASE_URL

print(database_url)


