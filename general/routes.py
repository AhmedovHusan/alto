from flask import render_template, url_for, request, flash, redirect
from general import db
from general.models import User
from general import app


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/data')
def data():
    return render_template('show_template.html', users=User.query.all())


@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['username'] or not request.form['address']:
            flash("Please, Enter the field required things!", 'error')
        else:
            user = User(
                request.form['username'], request.form['address'], request.form['password'])

            db.session.add(user)
            db.session.commit()

            flash("Record was successfully added")
            return redirect(url_for('data'))
    return render_template('new.html')
