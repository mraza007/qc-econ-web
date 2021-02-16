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
    yield('/faculty')

@app.route('/')
def index():
    return render_template('main.html', pages=pages)

@app.route('/whyqc')
def whyqc():
    return render_template('why-qc.html')

@app.route('/programs/')
def programs():
	return render_template('programs.html')

@app.route('/finance/')
def finance_bba():
    return render_template('programs/finance.html')

@app.route('/ib/')
def ib():
    return render_template('programs/ib.html')

@app.route('/policy/')
def policy():
    return render_template('programs/policy.html')

@app.route('/actuary/')
def actuary():
    return render_template('programs/actuary.html')

@app.route('/quant/')
def quant():
    return render_template('programs/quant.html')

@app.route('/econ/')
def econ():
    return render_template('programs/econ.html')

@app.route('/accounting/')
def accounting():
    return render_template('programs/accounting.html')

@app.route('/tax/')
def tax():
    return render_template('programs/tax.html')

@app.route('/risk/')
def risk():
    return render_template('programs/risk.html')

@app.route('/msaccounting/')
def msaccounting():
    return render_template('programs/ms-accounting.html')

@app.route('/p/')
def p():
    return render_template('programs-1.html')

@app.route('/faculty/')
def faculty():
    return render_template('faculty.html')

@app.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(port=8000)