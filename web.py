import sqlalchemy
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    rank = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    def __repr__(self):
        return self.name


class Teacher(db.Model):
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name1 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    password = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    def __repr__(self):
        return self.name1


@app.route('/')
def index():
    teachers = Teacher.query.order_by(Teacher.name1).all()
    users = User.query.order_by(User.rank).all()
    return render_template('base.html', data=users, a=teachers)


@app.route('/kabinet', methods=['POST', 'GET'])
def kabinet():
    if request.method == 'POST':
        name1 = request.form['name1']
        password = request.form['password']
        teacher = Teacher(name1=name1, password=password)
        try:
            db.session.add(teacher)
            db.session.commit()
            return redirect('/')
        except:
            return 'ошибка'
    else:
        return render_template('kabinet.html')


@app.route('/ticket')
def ticket():
    return render_template('ticket.html')


@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        rank = request.form['rank']
        user = User(name=name, rank=rank)
        try:
            db.session.add(user)
            db.session.commit()
            return redirect('/')
        except:
            return 'ошибка'
    else:
        return render_template('add.html')


if __name__ == '__main__':
    app.run(debug=True)