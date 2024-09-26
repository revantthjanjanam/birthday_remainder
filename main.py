from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime, timedelta
from models import db, Birthday
from datetime import datetime
import urllib.parse 


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///birthday.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.template_filter('urlencode')
def urlencode_filter(s):
    return urllib.parse.quote(s)
# Home page (Today's birthdays)
@app.route('/')
def home():
    today = datetime.now().date()
    birthdays_today = Birthday.query.filter_by(dob=today).all()
    return render_template('index.html', birthdays=birthdays_today)

# Upcoming birthdays (Next 30 days)
@app.route('/upcoming-birthdays')
def upcoming_birthdays():
    today = datetime.now().date()
    end_date = today + timedelta(days=30)
    upcoming = Birthday.query.filter(Birthday.dob.between(today, end_date)).all()
    return render_template('upcoming.html', birthdays=upcoming)

# Add new birthday form
@app.route('/add-birthday', methods=['GET', 'POST'])
def add_birthday():
    if request.method == 'POST':
        name = request.form['name']
        dob_str = request.form['dob']
        dob = datetime.strptime(dob_str, '%Y-%m-%d').date()
        contact = request.form['contact']
        new_birthday = Birthday(name=name, dob=dob, contact=contact)
        db.session.add(new_birthday)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_birthday.html')

# Edit database (View, Edit, Delete Entries)
@app.route('/edit-database', methods=['GET', 'POST'])
def edit_database():
    birthdays = Birthday.query.all()
    if request.method == 'POST':
        if 'delete' in request.form:
            birthday_id = request.form['delete']
            Birthday.query.filter_by(id=birthday_id).delete()
            db.session.commit()
        elif 'edit' in request.form:
            birthday_id = request.form['edit']
            birthday = Birthday.query.get(birthday_id)
            return redirect(url_for('edit_entry', birthday_id=birthday.id))
    return render_template('edit_database.html', birthdays=birthdays)

# Edit specific entry
@app.route('/edit-entry/<int:birthday_id>', methods=['GET', 'POST'])
def edit_entry(birthday_id):
    birthday = Birthday.query.get(birthday_id)
    if request.method == 'POST':
        birthday.name = request.form['name']
        dob_str = request.form['dob']
        birthday.dob = datetime.strptime(dob_str, '%Y-%m-%d').date()
        birthday.contact = request.form['contact']
        db.session.commit()
        return redirect(url_for('edit_database'))
    return render_template('edit_entry.html', birthday=birthday)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Creates the database tables
    app.run(debug=True)
