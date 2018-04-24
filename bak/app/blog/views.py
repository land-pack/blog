from flask import render_template
from . import blog


@blog.route('/')
@blog.route('/index')
def index():
    return render_template('index.html')
