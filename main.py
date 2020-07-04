
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session
#import mysql.connector
import os

app = Flask(__name__)
app.secret_key =os.urandom(24)

# conn =mysql.connector.connect(host="sql12.freemysqlhosting.net", user="sql12350872",password="hS481P6gxf",database="sql12350872")
#conn =mysql.connector.connect(host="localhost", user="root",password="",database="flask_app")
#cursor = conn.cursor()

@app.route("/")
def index():
    return render_template("Login.html")

@app.route("/home")
def home():
    # if 'user_id' in session:
    #     return render_template('home.html')

    # else:
         return render_template('menubar.html')



@app.route("/login", methods=['POST', 'GET'])
def login():
    
    
    if request.method == "POST":
        f = request.files['audio_data']
        with open('audio.wav', 'wb') as audio:
            f.save(audio)
        print('file uploaded successfully')

        # return render_template('Login.html', request="POST")
        return redirect("/home")
    else:
        # return render_template("Login.html")
        return redirect("/home")

@app.route("/register")
def register():
    
    return render_template("register.html")

'''
@app.route('/add_user',methods=['POST'])
def add_user():
    firstname = request.form.get('register-firstname')
    lastname = request.form.get('register-lastname')
    phone = request.form.get('register-phone')
    email = request.form.get('register-mail')
    password = request.form.get('register-pass')
    address1 = request.form.get('register-address1')
    address2 = request.form.get('register-address2')
    city = request.form.get('register-city')
    state = request.form.get('register-state')
    pin = request.form.get('register-pin')

    cursor.execute("""INSERT INTO `users` (`user_id`,`firstname`,`lastname`,`phone`,`email`,`password`,`address1`,`address2`,`city`,`state`,`pin`) VALUES 
    (NULL,'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')""".format(firstname,lastname,phone,email,password,address1,address2,city,state,pin))
    conn.commit()


    cursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}'""".format(email))
    myuser=cursor.fetchall()
    session['user_id']=myuser[0][0]
    return redirect('/home')




@app.route('/logout')
def logout():
    session.pop('user_id')
    return redirect ('/')
'''

if __name__ == "__main__":
    app.run(debug=True)