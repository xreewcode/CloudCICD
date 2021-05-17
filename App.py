from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
app.secret_key = "Secret Key"

# SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Creating model table for our CRUD database
class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    evcckt = db.Column(db.String(100))
    port = db.Column(db.String(100))
    customer = db.Column(db.String(100))
    state = db.Column(db.String(100))
    market = db.Column(db.String(100))
    status = db.Column(db.String(100))

    def __init__(self, name, email, phone, evcckt, port, customer, state, market, status):
        self.name = name
        self.email = email
        self.phone = phone
        self.evcckt = evcckt
        self.port = port
        self.customer = customer
        self.state = state
        self.market = market
        self.status = status


# This is the index route where we are going to
# query on all our device data
@app.route('/')
def Index():
    all_data = Data.query.all()

    return render_template("index.html", devices=all_data)


# this route is for inserting data to mysql database via html forms
@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        evcckt = request.form['evcckt']
        port = request.form['port']
        customer = request.form['customer']
        state = request.form['state']
        market = request.form['market']
        status = request.form['status']

        my_data = Data(name, email, phone, evcckt, port, customer, state, market, status)
        db.session.add(my_data)
        db.session.commit()

        flash("Device Inserted Successfully")

        return redirect(url_for('Index'))


# this is our update route where we are going to update our device
@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        my_data = Data.query.get(request.form.get('id'))

        my_data.name = request.form['name']
        my_data.email = request.form['email']
        my_data.phone = request.form['phone']
        my_data.evcckt = request.form['evcckt']
        my_data.port = request.form['port']
        my_data.customer = request.form['customer']
        my_data.state = request.form['state']
        my_data.market = request.form['market']
        my_data.status = request.form['status']

        db.session.commit()
        flash("Device Updated Successfully")

        return redirect(url_for('Index'))


# This route is for deleting our device
@app.route('/delete/<id>/', methods=['GET', 'POST'])
def delete(id):
    my_data = Data.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Device Deleted Successfully")

    return redirect(url_for('Index'))


if __name__ == "__main__":
    app.run(debug=True)