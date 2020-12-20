from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.htm")

@app.route('/My_Anganwadi')
def profile():


    return render_template("myangan.htm")

@app.route('/complain', methods=["POST","GET"])
def complain():




    return render_template('complain.htm')

@app.route('/login')
def login():
    name = 'current user'

    return render_template('login.htm',name = name)

    
app.run(debug=True)