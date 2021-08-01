"""
Flaskサンプル
http://localhost:3500/

"""

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

def test():
    """
    Flask起動
    """
    
    app.run(host='localhost', port=3500)
