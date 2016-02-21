from flask import Flask, render_template
from flask.ext.script import Manager
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap()
bootstrap.init_app(app)
manager = Manager(app)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/user/<name>')
def user(name):
	return render_template('user.html',name=name)


if __name__ == '__main__':
	app.run(debug=True,host="127.0.0.1",port=8888)
	 # manager.run()
	# Bootstrap(app)