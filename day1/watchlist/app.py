import os
import sys
import click
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

WIN = sys.platform.startswith('win')

if WIN:
    prefix = 'sqlite:///'

else:
    prefix = 'sqlite:////'
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(
    app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    year = db.Column(db.String(4))


@app.route('/')
def index():
    movies = Movie.query.all()
    return render_template('index.html', movies=movies)


@app.cli.command()
@click.option('--drop', is_flag=True, help='删除创建')
def initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()


@app.cli.command()
def forge():
    name = "zhaohuizhe"
    movies = [{
        "title": "大赢家",
        "year": "2020"
    }, {
        "title": "囧妈",
        "year": "2020"
    }, {
        "title": "战狼",
        "year": "2020"
    }, {
        "title": "心花路放",
        "year": "2020"
    }, {
        "title": "我的父亲母亲", 
        "year": "2020"
    }]
    user = User(name=name)
    db.session.add(user)
    for m in movies:
        movie = Movie(title=m['title'], year=m['year'])
        db.session.add(movie)
    db.session.commit()
    click.echo('完成')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.context_processor
def a():
    user = User.query.first()
    return dict(user=user)
