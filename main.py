from Django_myanimelist import app
from flask import render_template

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def index():

    name = 'JJSakurai'
    return render_template(
        'index.html',
        name = name
    )