from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://qatraining:password@localhost/flaskdb"
db = SQLAlchemy(app)

class daily_workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

@app.route('/')
def index():
    # show all todos
        DailyWorkout_list = daily_workout.query.all()
    #getting all the data from the daily workout table
        return render_template('base.html', DailyWorkout_list=DailyWorkout_list)
#passing the data to the html (render template is going to get the html page and render the page)
@app.route("/add", methods=["POST","GET"])
def add():
        # add new item
        title = request.form.get("title")
        new_DailyWorkout = daily_workout(title=title, complete=False)
        db.session.add(new_DailyWorkout)
        db.session.commit()
        return redirect(url_for("index"))
# a post method used to pass the data to the flask (used to getting the name of the
#title and putting it into the data base and return it back to the index function
@app.route("/Done/<int:DailyWorkout_id>", methods=["POST","GET"])
def Done(DailyWorkout_id):
        # add new item
        doughnut = daily_workout.query.filter_by(id=DailyWorkout_id).first()
        doughnut.complete = not doughnut.complete
        db.session.commit()
        return redirect(url_for("index"))
#creating an id line 32
#used the name doughnut to avoid duplicate variables changing the workout data to true and updating that in the database
#line 35 do the opposite of what it is. i commited this and redirect it the url index

@app.route("/delete/<int:DailyWorkout_id>",methods=["POST"])
def delete(DailyWorkout_id):
        # delete item
        delete_workout = daily_workout.query.filter_by(id=DailyWorkout_id).first()
        db.session.delete(delete_workout)
        db.session.commit()
        return redirect(url_for("index"))
#i am using the daily workout db table to get the first table row to match the id then deleting this and commit this ans redirect to the index
if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0")

#db create all create database and run is to the db and show any errors that arise
