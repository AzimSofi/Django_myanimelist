from Django_myanimelist import app
from flask import Flask, render_template

app = Flask(__name__, template_folder='static/templates')

@app.route('/')
def index():
    name = 'JJSakurai'
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
