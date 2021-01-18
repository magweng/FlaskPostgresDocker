
from flask import jsonify, Flask, render_template, request, url_for, redirect
from project import app, db
from datetime import datetime as dt
from .models import LogMessage
from .forms import RegistrationForm


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        log_msg = LogMessage(datetime=dt.now(), message=form.message.data)
        # Db save
        db.session.add(log_msg)
        db.session.commit()

        return redirect(url_for('home'))

    return render_template('register.html', form=form)


@app.route("/")
@app.route("/home")
def home():
    ## DB query
    log_msg_list = LogMessage.query.all()
    return render_template(
        "home.html",
        messages=log_msg_list,       
    )

@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/contact/")
def contact():
    return render_template("contact.html")

