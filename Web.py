import sqlalchemy
from flask import Flask, render_template
from data import db_session
from data.db_session import SqlAlchemyBase
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    rank = sqlalchemy.Column(sqlalchemy.String, nullable=True)


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/kabinet')
def kabinet():
    return render_template('kabinet.html')


@app.route('/ticket')
def ticket():
    return render_template('ticket.html')


@app.route('/add')
def add():
    return render_template('add.html')


if __name__ == '__main__':
    db_session.global_init("db/menu.db")
    app.run(debug=True)

