from flask import Flask, render_template, request, redirect, url_for
from flask_debugtoolbar import DebugToolbarExtension
import os
import logging
import config
import db
import pprint
import auth

app = Flask(__name__)
app.debug = True
app.secret_key = 'development key'

toolbar = DebugToolbarExtension(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/edit", methods=['POST', 'GET'])
@auth.requires_auth
def edit():
    if request.method == 'POST':
        filename = None

        # Save file
        if 'photo' in request.files:
            file = request.files['photo']
            filename = file.filename
            file.save(config.upload_dir(filename))

        # Add item
        db.add_item(request.form['name'], filename)

    items = db.get_items()
    return render_template('edit.html', items=items)

@app.route('/remove/<id>')
def remove(id):
    db.remove_item(id)
    return redirect(url_for('edit'))

@app.route("/run", methods=['POST', 'GET'])
@auth.requires_auth
def run():
    if request.method == 'POST':
        db.set_message_before(request.form['message-before'])
        db.set_message_after(request.form['message-after'])
    return render_template('run.html', config=db.get_config())

@app.template_filter('upload_dir')
def prepend_upload_path(filename):
    return url_for('static', filename=os.path.join('upload', filename))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
