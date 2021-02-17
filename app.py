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


professors = {
    'econ': [

    {   
        'id':'1',
        'name': 'Clive Belfield',
        'title': 'Economics',
        'image': 'https://qcsocialsciences.org/wp-content/uploads/2021/01/Clive_Belfield-300x300.jpg',
        'link':  'http://belfield2.wix.com/cbhome',
        'bio': 'Clive Belfield is a professor of economics at Queens College, City University of New York. He received his PhD in economics from the University of Exeter in England. He is also Principal Economist at the Center for Benefit-Cost Studies in Education, Teachers College, Columbia University. Professor Belfield has authored three books and numerous articles on the economics of education; he has served as a consultant to the World Bank, the U.S. Department of Education, and the British Government, as well as nonprofit foundations and education think tanks; and he has been an expert witness in state constitutional court cases on educational adequacy.'
    },
    {   
        'id':'2',
        'name': 'Leticia Arroyo Abad',
        'title': 'Economics',
        'image': 'https://qcsocialsciences.org/wp-content/uploads/2021/01/Abad.jpg',
        'link': 'http://www.arroyoabad.com/',
        'bio': 'Leticia Arroyo Abad is an associate professor in the Department of Economics at Queens College. Her primary research expertise is the study of globalization and inequality both within and across nations, with a focus on the Americas. Before getting her Ph.D. at the University of California, Davis, Leticia worked as a macroeconomic analyst for an Argentine consultancy where she was charged with forecasting the effect of policy changes on economic conditions. She also analyzed specific industry portfolios, after which she worked at Inter – American Development and Bank and the Argentine Department of Industry'
    },  
    {   
        'id':'3',
        'name': 'Cara Marshall',
        'title': 'Economics',
        'image':'https://qcsocialsciences.org/wp-content/uploads/2021/01/Marshall-2-261x300.jpg',
        'link': 'http://www.qc-econ-bba.com/facultypages/marshall/',
        'bio': 'Cara Marshall is a tenured Lecturer at Queens College of the City University of New York and the Director of Queens College’s Graduate Program in Risk Management.  Dr. Marshall teaches in the areas of risk management, portfolio management, financial modeling, Microsoft Excel and VBA programming, Python programming, risk measurement, and corporate finance. Professor Marshall Cara has also worked as a consultant and conducted training at leading investment banks, asset management firms, hedge funds, and government agencies.  Specifically, some of the firms where Cara has trained employees include: Goldman Sachs, Deutsche Bank, JPMorgan Chase, Citi, Morgan Stanley, Bank of America, Wells Fargo, Barclays, Lazard, Bank of China, Prudential, HSBC, Fidelity, RBC, FHFA, and U.S. Department of the Treasury.'
    },
    {
        'id':'4',
        'name': 'Joan Nix',
        'title': 'Economics',
        'image': 'https://qcsocialsciences.org/wp-content/uploads/2021/01/Nix.jpg',
        'link':'https://www.joannix.org/',
        'bio':'Joan Nix is an Associate Professor of Economics at Queens College of CUNY and a Deputy Chair of the BBA program. Joan Nix received her Ph.D in Economics from NYU. Her research interests span behavioral economics, corporate culture as behavioral risk management, regulatory capture, net neutrality, the economics of crypto assets, common ownership, and wavelet methodology. Recent research has been published In Economic Modelling, and chapters in books on Wavelets. She received the President’s award for teaching excellence based largely on letters of nomination from former students.  She continues to enjoy contact with current and former students.'
    },
    {
        'id':'5',
        'name': 'Francisco Peñaranda',
        'title': 'Economics',
        'image':'https://qcsocialsciences.org/wp-content/uploads/2021/01/Panaranda.jpg',
        'link':'http://sites.google.com/site/fpenaranda15/?',
        'bio': 'Francisco Peñaranda is an associate professor at Queens College CUNY. Previously he was a senior researcher at the Santander Financial Institute, an assistant  professor at Universitat Pompeu Fabra and University of Alicante, and a research fellow at the London School of Economics. He works and teaches on Asset Pricing and Portfolio Management. His research has been published in the Journal of Econometrics, the Journal of Financial and Quantitative Analysis, and Management Science, among other scientific journals.'
    },
    {
        'id':'6',
        'name': 'Núria Rodríguez-Planas ',
        'title': 'Economics',
        'image': 'https://qcsocialsciences.org/wp-content/uploads/2021/01/nuria.jpg',
        'link': 'https://sites.google.com/site/nuriarodriguezplanas/',
        'bio': 'Núria Rodríguez-Planas  is a professor in Economics at City University of New York (CUNY), Queens College; Doctoral Faculty at the Graduate Center (CUNY) and managing editor of IZA Journal of Labor Policy This academic year, I am a Research Scholar at the Economics Department at Barnard College – Columbia University.Prior to moving to New York, I was Visiting Research Fellow at IZA in Bonn from 2011 to 2014, Visiting Professor at the Universitat Pompeu Fabra from 2012 to 2013, Assistant Professor at the Universitat Autònoma de Barcelona from 2004 to 2011, and Affiliated Professor at the Barcelona Graduate School of Economics from 2007 to 2012. I have also held positions in Washington DC as an Economist at Mathematica Policy Research from 2000 to 2004, the Board of Governors of the Federal Reserve System from 1998 to 2000, and the Brookings Institution from 1997 to 1998. I received my Ph.D. in Economics in 1999 from Boston University.'
    },
    {
        'id':'7',
        'name': 'Jennifer Roff',
        'title': 'Economics',
        'image': 'https://qcsocialsciences.org/wp-content/uploads/2021/01/Roff.jpg',
        'link':'https://sites.google.com/site/jenniferroffecon/',
        'bio':'Jennifer Roff is an associate professor at Queens College and the Graduate Center of the City University of New York and a Research Fellow at the IZA Institute of Labor Economics. Her research interests fall broadly within labor and economic demography, with a particular focus on the economics of the family. Recent work has focused on the empirical implications of marital matching for children as well as the effects of marriage laws on men’s household production. '
    },
    {
        'id':'8',
        'name': 'Kevin Shih',
        'title': 'Economics',
        'image': 'https://qcsocialsciences.org/wp-content/uploads/2021/01/shih.jpg',
        'link': 'http://kevinyshih.weebly.com/',
        'bio': 'Kevin Shih is an Assistant Professor in the Economics Department at Queens College. He is a labor economist who specializes in research on the economics of immigration. His work examines issues related to the causes and consequences of international migration flows. He has written articles on various topics, such as the impacts of skilled immigration via the H-1B visa program, the influence of DACA on the educational attainment of undocumented youth, and the implications of rising international student presence in US higher education.'
    },
    {
        'id':'9',
        'name': 'Suleyman Taspinar',
        'title': 'Economics',
        'image':'https://qcsocialsciences.org/wp-content/uploads/2020/10/taspinar.jpg',
        'link':'https://sites.google.com/site/gcsuleymantaspinar/',
        'bio':'Suleyman Taspinar, Assistant Professor and Director of the Quantitative Economics Program. He is an econometrician with the core area of research on estimation and inference problems in spatial econometric models with potential heterogeneity. He also works on estimation and inference problems in models of risk in finance. Separately from these two areas, he is interested in empirical research problems that analyze the behavior of economic agents when these agents are exposed to climate-change related extreme shocks.'
    },
    {
        'id':'10',
        'name': 'Tao Wang ',
        'title': 'Economics',
        'image':'https://qcsocialsciences.org/wp-content/uploads/2021/01/tao-wang.jpg',
        'link':'http://www.qc.edu/~twang',
        'bio':'Tao Wang in a Professor of Economics. His research interests include Financial Economics, Financial Econometrics, International Finance and Macroeconomics'
    }

    ]


}


app.config['SESSION_COOKIE_SECURE'] = False

@app.route('/pygments.css')
def pygments_css():
    return pygments_style_defs('tango'), 200, {'Content-Type': 'text/css'}

@freezer.register_generator
def url_generator():
    yield('/')
    yield('/programs/')
    yield('/faculty/')
    yield('/faculty/1/')
    yield('/faculty/2/')
    yield('/faculty/3/')
    yield('/faculty/4/')
    yield('/faculty/5/')
    yield('/faculty/6/')
    yield('/faculty/7/')
    yield('/faculty/8/')
    yield('/faculty/9/')
    yield('/faculty/10/')
    yield('/whyqc/')
    yield('/finance/')
    yield('/ib/')
    yield('/policy/')
    yield('/actuary/')
    yield('/quant/')
    yield('/econ/')
    yield('/accounting/')
    yield('/tax/')
    yield('/risk/')
    yield('/msaccounting/')

@app.route('/')
def index():
    return render_template('main.html', pages=pages)

@app.route('/whyqc/')
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
    return render_template('faculty.html',professors=professors)

@app.route('/faculty/<professor>/')
def prof_page(professor):
    for prof in professors['econ']:
        if prof['id'] == professor:
            return render_template('professor.html',professor=prof)

@app.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(port=8000)