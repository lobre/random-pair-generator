from flask import Flask, render_template, request, redirect, url_for
import config
import controller
import db
import pprint

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/edit", methods=['POST', 'GET'])
def edit():
    if request.method == 'POST':
        db.add_item(request.form['item'])
    items = db.get_items()
    return render_template('edit.html', items=items)

@app.route('/remove/<id>')
def remove(id):
    db.remove_item(id)
    return redirect(url_for('edit'))

@app.route("/run")
def run():
    db.add_item('toto')
    return render_template('run.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
