from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

session_maker = sessionmaker(
    bind=create_engine(
        "postgresql://postgres:postgresdb2022@localhost:5432/wedevLearning"
    ),
)
