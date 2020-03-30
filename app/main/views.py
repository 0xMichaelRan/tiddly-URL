from flask import current_app, flash, redirect, url_for, render_template
from .. import db
from . import main


@main.route('/', methods=['GET'])
def index():
    return render_template("index.html")