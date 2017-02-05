from flask import Flask, render_template, request, redirect, url_for
import os
import logging
import config
import db
import auth
import gif

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/")
def index():
    return render_template('index.html', has_pairs=db.has_pairs(), config=db.get_config())

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
@auth.requires_auth
def remove(id):
    db.remove_item(id)
    return redirect(url_for('edit'))

@app.route("/run", methods=['POST', 'GET'])
@auth.requires_auth
def run():
    if request.method == 'POST':
        db.set_message_before(request.form['message-before'])
        db.set_message_after(request.form['message-after'])
    return render_template('run.html', config=db.get_config(), has_pairs=db.has_pairs())

@app.route('/generate')
@auth.requires_auth
def generate():
    db.add_pair({'test': True})
    gif.generate()
    return redirect(url_for('run'))

@app.route('/reset')
@auth.requires_auth
def reset():
    db.reset_pairs()
    gif.remove()
    return redirect(url_for('run'))

@app.template_filter('upload_dir')
def prepend_upload_path(filename):
    return url_for('static', filename=os.path.join('upload', filename))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
