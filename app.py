from flask import Flask, render_template, request,redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/chow/blog/LearningWeb/blog.db'

db = SQLAlchemy(app)

class Blogpost(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(50))
	subtitle = db.Column(db.String(50))
	author = db.Column(db.String(20))
	date_posted = db.Column(db.DateTime)
	content = db.Column(db.Text)


@app.route('/')
def index():
	posts = Blogpost.query.all()
	return	render_template('index.html', posts=posts)


@app.route('/about')
def about():
	return	render_template('about.html')



@app.route('/post/<int:post_id>')
def post(post_id):
	post = Blogpost.query.filter_by(id=post_id).one()
	return	render_template('post.html', post=post)

@app.route('/contact')
def contact():
	return	render_template('contact.html')

@app.route('/add')
def add():
	return	render_template('add.html')



@app.route('/application')
def application():
	return	render_template('application.html')


@app.route('/application/results')
def results():
	return	render_template('results.html')



@app.route('/appost', methods =['POST', 'GET'])
def appost():
	#if request.method == 'POST':
   	#Invest = request.form['Invest']
      #  print(result)
	#return "thank you for filling out this form"
	#return '<h1>DDD:{}</h1>'.format(Invest)
	return redirect(url_for('results'))




@app.route('/addpost', methods =['POST'])
def addpost():
	title = request.form['title']
	subtitle = request.form['subtitle']
	author = request.form['author']
	content =request.form['content']
	
	#return '<h1>Title: {} Subtitle: {} Author: {} Content: {} </h1>'.format(title, subtitle, author, content)
	post = Blogpost(title =title, subtitle=subtitle, author=author, content=content, date_posted=datetime.now())
	db.session.add(post)
	db.session.commit()

	return	redirect(url_for('index'))




if __name__ == '__main__':
	app.run(debug=True)