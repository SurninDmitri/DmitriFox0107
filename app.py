from flask import Flask, render_template, request, redirect, url_for
from database import get_all_items, add_item

app = Flask(__name__)

@app.route('/')
def index():
    items = get_all_items()
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    description = request.form['description']
    add_item(name, description)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
