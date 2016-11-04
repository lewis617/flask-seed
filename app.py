from flask import Flask, render_template
from flask_assets import Environment, ManageAssets
from flask_script import Manager
import os

app = Flask(__name__)

# config
app.config.debug = os.getenv('ENV_MODE', 'DEV') != 'PROD'

# flask-assets
assets = Environment(app)
assets.debug = app.debug

# flask script
manager = Manager(app)
manager.add_command("assets", ManageAssets(assets))


@app.route('/')
def hello_world():
    return render_template('home/index.html')


if __name__ == '__main__':
    manager.run()
