from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import string
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500))
    short_url = db.Column(db.String(10), unique=True)

def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choices(characters, k=6))
    link = URL.query.filter_by(short_url=short_url).first()

    if link:
        return generate_short_url()

    return short_url

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        original_url = request.form['original_url']
        if original_url:
            short_url = generate_short_url()
            new_link = URL(original_url=original_url, short_url=short_url)
            db.session.add(new_link)
            db.session.commit()

            return render_template('short_link.html', short_url=short_url)
    return render_template('home.html')

@app.route('/<short_url>')
def redirect_to_url(short_url):
    link = URL.query.filter_by(short_url=short_url).first()
    if link:
        return redirect(link.original_url)
    else:
        flash("Invalid URL")
        return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
