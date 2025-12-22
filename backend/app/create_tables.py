# create_tables.py

from .database import Base, engine  # relative import
from . import models  # import all your models

# Create tables in PostgreSQL
Base.metadata.create_all(bind=engine)

print("Tables created successfully!")
