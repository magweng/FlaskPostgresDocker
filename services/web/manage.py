from flask.cli import FlaskGroup
from datetime import datetime as dt
from project import app, db
from project.models import LogMessage
from project.routes import *

cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command("seed_db")
def seed_db():   
    db.session.add(LogMessage(datetime=dt.now(), message="This is a test"))
    db.session.commit()

if __name__ == "__main__":
    cli()
