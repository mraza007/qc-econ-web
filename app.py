from flask import Flask, render_template
from flask_flatpages import FlatPages,pygmented_markdown, pygments_style_defs
from flask_frozen import Freezer
import sys
import pygments, markdown

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite', 'fenced_code', 'tables']
# FREEZER_RELATIVE_URLS = True

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)

app.config['SESSION_COOKIE_SECURE'] = False

@app.route('/pygments.css')
def pygments_css():
    return pygments_style_defs('tango'), 200, {'Content-Type': 'text/css'}

@freezer.register_generator
def url_generator():
    yield('/')
    yield('/programs')

@app.route('/')
def index():
    return render_template('index4.html', pages=pages)

@app.route('/programs/')
def programs():
	return render_template('index6.html')

@app.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(port=8000)