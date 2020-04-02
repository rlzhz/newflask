import os
import sys

from flask import Flask, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
import click
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = prefix+os.path.join(app.root_path,'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20))
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
@app.route('/')
def index():
    # print(url_for('index'))
    # name = 'zhaohuizhe'
    
    user = User.query.first() #读取用户记录
    movies = Movie.query.all() #读取所以地电影记录
    return render_template('index.html', name=user, movies=movies)

# 注册命令
@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop')
def initdb(drop):
    if drop:
        db.drop.all()
    db.create_all()
    click.echo('初始化数据库。。。')

@app.cli.command()
def forge():
    db.create_all()
    movies = [
        {'title': '哪吒'},
        {'title': '牧马人'}
    ]
    for m in movies:
        print(m)
        movie = Movie(title=m['title'])
        print(movie)
        db.session.add(movie)
    
    db.session.commit()
    click.echo('导入数据')

