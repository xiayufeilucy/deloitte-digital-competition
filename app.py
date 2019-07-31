from flask import Flask, render_template, request, session, jsonify, send_file, Response, flash
from flask_bootstrap import Bootstrap
from wtforms import FloatField, SubmitField, StringField, PasswordField, BooleanField
from flask_wtf import Form, FlaskForm

app = Flask(__name__)
app.secret_key = "lucy"
Bootstrap(app)

#Search Form
class Search(FlaskForm):
    name = StringField('search')


@app.route('/',methods= ["GET", "POST"])
def search():
    form = Search(request.form)
    search = ""

    if request.method == 'POST':
        search = request.form['search']
        if search.lower() == 'attain':
            return  render_template('dashboard- summary.html')
        else:
            return render_template('404.html')


    return render_template('login-register.html', form = form)

@app.route('/summary')
def start_dashboard():
    return render_template('dashboard- summary.html')

@app.route('/algo')
def start_algo():
    return render_template('algo.html')

@app.route('/team')
def start_team():
    return render_template('team.html')


#@app.route('/')
#def trial():
    #return render_template('index2.html')


if __name__ == '__main__':
    app.run(port = 1234)