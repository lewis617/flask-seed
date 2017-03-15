#!/usr/bin/env python
import os
import sys
from app import create_app
from flask_script import Manager
from jac.contrib.flask import get_template_dirs
import shutil

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
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


if __name__ == '__main__':
    manager.run()
