from sqlalchemy import create_engine, Field, Session, SQlModel, select,engine

def create_db():
    SQlModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield Session
