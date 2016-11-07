from flask import Flask, render_template
from flask_script import Manager
from jac.contrib.flask import JAC, get_template_dirs
import os
import sys
import shutil

app = Flask(__name__)

# config
app.debug = os.getenv('ENV_MODE', 'DEV') != 'PROD'

# jac
app.config['COMPRESSOR_DEBUG'] = app.debug
app.config['COMPRESSOR_OUTPUT_DIR'] = '%s/static/dist' % sys.path[0]
app.config['COMPRESSOR_STATIC_PREFIX'] = '/static/dist'
jac = JAC(app)

# flask script
manager = Manager(app)


@manager.command
def jac():
    env = app.jinja_env

    if os.path.exists(env.compressor_output_dir):
        print('Deleting previously compressed files in {output_dir}'
              .format(output_dir=env.compressor_output_dir))
        shutil.rmtree(env.compressor_output_dir)
    else:
        print('No previous compressed files found in {output_dir}'
              .format(output_dir=env.compressor_output_dir))

    template_dirs = [sys.path[0] + '/' + x for x in get_template_dirs(app)]

    print('Compressing static assets into {output_dir}'
          .format(output_dir=env.compressor_output_dir))
    compressor = env.extensions['jac.extension.CompressorExtension'].compressor
    compressor.offline_compress(env, template_dirs)

    print 'Finished.'


@app.route('/')
def hello_world():
    return render_template('home/index.html')


if __name__ == '__main__':
    manager.run()
