from flask import Flask , render_template
from flask_flatpages import FlatPages
from datetime import datetime

app = Flask(__name__)
app.config['FLATPAGES_EXTENSION'] = '.md'
pages = FlatPages(app)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/blog')
def blog():
    posts = [p for p in pages if "date" in p.meta]
    sorted_pages=sorted(posts, reverse=True, key=lambda page: datetime.strptime(page.meta["date"], "%d %b %y"))
    return render_template('bloghome.html', pages=sorted_pages)

@app.route('/about')
def about():
    return "this is about section"

@app.route('/<path:path>.html')
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)



if __name__ == "__main__":
    app.run(debug=True)