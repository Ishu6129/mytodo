from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import request
from flask import jsonify
from flask import redirect

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///sample_todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class Todo(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(200),nullable=False)
    desc=db.Column(db.String(500),nullable=False)
    date_created=db.Column(db.DateTime,default=db.func.current_timestamp())
    
    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"
    

    
@app.route('/',methods=['GET','POST'])
def main():
    if request.method=='POST':
        title=request.form['title']
        desc=request.form['desc']
        todo=Todo(title=title,desc=desc)
        db.session.add(todo)
        db.session.commit()
        allTodo=Todo.query.all()
        return redirect('/')
    allTodo=Todo.query.all()
    return render_template('index.html',allTodo=allTodo)

@app.route('/delete/<int:sno>',methods=['GET','POST'])
def delete(sno):
    todo=Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')

@app.route('/update/<int:sno>',methods=['GET','POST'])
def update(sno):
    if request.method=='POST':
        title=request.form['title']
        desc=request.form['desc']
        todo=Todo.query.filter_by(sno=sno).first()
        todo.title=title
        todo.desc=desc
        db.session.commit()
        return redirect('/')
    todo=Todo.query.filter_by(sno=sno).first()
    return render_template('update.html',todo=todo)


if __name__ == "__main__":
    app.run(debug=True,port=5000)
