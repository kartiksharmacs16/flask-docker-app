from operator import add
from flask import Flask , render_template , request , redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    Sno = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(200), nullable=False)
    Description = db.Column(db.String(200), nullable=False)
    Date = db.Column(db.DateTime, default=datetime.utcnow)

def __repr__(self) -> str:
    return f"{self.Sno} - {self.title}"

@app.route("/", methods = ['GET', 'POST'])
def hello():
    if request.method == "POST":
        name = request.form['title']
        desc = request.form['desc']
        todo = Todo(Title = name ,Description= desc)
        db.session.add(todo)
        db.session.commit()
    alltodo = Todo.query.all()
    return render_template('index.html', alltodo = alltodo)

@app.route("/products")
def products():
    return "This is a products page!"

@app.route("/update/<int:sno>" , methods = ['GET', 'POST'])
def update(sno):
    if request.method == "POST":
        name = request.form['title']
        desc = request.form['desc']
        todo = Todo.query.filter_by(Sno=sno).first()
        todo.Title = name
        todo.Description = desc
        db.session.add(todo)
        db.session.commit()
        return redirect("/")

    todo = Todo.query.filter_by(Sno=sno).first()
    return render_template('update.html', todo = todo)
    

@app.route('/delete/<int:sno>')
def delete(sno):
    todo = Todo.query.filter_by(Sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(port = 5000,host="0.0.0.0")
