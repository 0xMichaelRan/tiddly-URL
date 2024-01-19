import os
from flask import current_app
from flask_migrate import Migrate
from app import create_app
from app import db
from app.models import *

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)


@app.cli.command()
def init_db():
    current_app.logger.info('Database initilize begin...')
    db.drop_all()
    db.create_all()
    current_app.logger.info('initialize database done!')

if __name__ == '__main__':
    app.run(ho='0.0.0.0',port='80',debug=True)
