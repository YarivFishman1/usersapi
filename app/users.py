from fastapi import FastAPI
from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine, select

app = FastAPI()


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    password: str

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.on_event('shutdown')
def on_shutdown():
    pass


@app.get('/users/')
def get_users():
    with Session(engine) as session:
        users = session.exec(select(User)).all()
        return users


@app.get('/users/{user_id}')
def get_user(user_id: int):
    with Session(engine) as session:
        statement = select(User).where(User.id == user_id)
        user = session.exec(statement).one()
        return user


@app.post('/users/', status_code=201)
def add_user(user: User):
    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user


@app.put('/users/{user_id}')
def update_user(user_id: int, user: User):
    with Session(engine) as session:
        session.add(user)
        session.commit()


@app.delete('/users/{user_id}')
def delete_user(user_id: int):
    with Session(engine) as session:
        statement = select(User).where(User.id == user_id)
        user = session.exec(statement).one()
        session.delete(user)
        session.commit()
