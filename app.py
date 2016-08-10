from flask import Flask, render_template
from flask_script import Manager
from jac_init import jac_init

app = Flask(__name__)
manager = Manager(app)
jac_init(app, manager)


@app.route('/')
def hello_world():
    return render_template('home/index.html')


if __name__ == '__main__':
    manager.run()
