from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index/')
def index():
    print(url_for('index'))
    name = 'zhaohuizhe'
    movies = [
        {'title': '哪吒'},
        {'title': '牧马人'}
    ]
    return render_template('index.html', name=name, movies=movies)